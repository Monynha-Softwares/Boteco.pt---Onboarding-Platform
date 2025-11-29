import asyncio
import logging
import os
from typing import Any, Iterable

import httpx
from supabase import Client, ClientOptions, create_client

logger = logging.getLogger(__name__)


class SupabaseClient:
    """Helper wrapper around Supabase client with safe async helpers."""

    def __init__(self) -> None:
        self.url: str | None = os.getenv("SUPABASE_URL")
        self.key: str | None = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv(
            "SUPABASE_KEY"
        )
        self.client: Client | None = self._initialize_client()

    def _initialize_client(self) -> Client | None:
        if not self.url or not self.key:
            logger.warning("Supabase credentials not configured. Skipping client init.")
            return None
        try:
            return create_client(
                self.url,
                self.key,
                options=ClientOptions(schema="reflex"),
            )
        except Exception as exc:  # pragma: no cover - defensive
            logger.exception("Error initializing Supabase client: %s", exc)
            return None

    def _ensure_client(self) -> Client:
        if not self.client:
            raise ConnectionError("Supabase client not initialized.")
        return self.client

    async def _run(self, func, *args, **kwargs):
        """Execute a potentially blocking Supabase call asynchronously."""

        return await asyncio.to_thread(func, *args, **kwargs)

    def _extract_first(self, response: Any) -> dict:
        data: Iterable[dict] = getattr(response, "data", None) or []
        if not data:
            raise ValueError("Nenhum dado retornado pelo Supabase.")
        return list(data)[0]

    async def create_user(self, user_data: dict, password: str | None = None) -> dict:
        """Create a new user row and optionally register auth credentials."""

        client = self._ensure_client()
        try:
            response = await self._run(
                lambda: client.table("users").insert(user_data).execute()
            )
            created_user = self._extract_first(response)
        except Exception as exc:
            logger.exception("Falha ao criar usuário: %s", exc)
            raise

        # Try to create an auth user if password provided (best-effort)
        if password:
            try:
                admin = getattr(getattr(client, "auth", None), "admin", None)
                if admin and hasattr(admin, "create_user"):
                    await self._run(
                        lambda: admin.create_user({
                            "email": user_data.get("email"),
                            "password": password,
                            "email_confirm": True,
                        })
                    )
                else:  # pragma: no cover - depends on supabase version
                    logger.info("Supabase auth admin not available; skipped auth user creation.")
            except Exception as exc:  # pragma: no cover - best-effort
                logger.exception("Auth user creation failed (continuing): %s", exc)
        return created_user

    async def upsert_user(self, user_data: dict) -> dict:
        """Insert or update a user record by email."""

        client = self._ensure_client()
        try:
            response = await self._run(
                lambda: client.table("users")
                .upsert(user_data, on_conflict="email")
                .execute()
            )
            return self._extract_first(response)
        except Exception as exc:
            logger.exception("Erro ao salvar usuário: %s", exc)
            raise

    async def delete_boteco(self, boteco_id: str) -> None:
        client = self._ensure_client()
        try:
            await self._run(
                lambda: client.table("boteco").delete().eq("id", boteco_id).execute()
            )
        except Exception as exc:
            logger.exception("Erro ao remover boteco: %s", exc)
            raise

    async def create_boteco_and_associate_user(
        self, boteco_data: dict, user_boteco_data: dict
    ) -> tuple[dict, dict]:
        """Create a boteco and associate a user with rollback on failure."""

        client = self._ensure_client()
        boteco_response = await self._run(
            lambda: client.table("boteco").insert(boteco_data).execute()
        )
        boteco = self._extract_first(boteco_response)
        try:
            user_boteco_data["boteco_id"] = boteco["id"]
            user_boteco_response = await self._run(
                lambda: client.table("user_boteco")
                .insert(user_boteco_data)
                .execute()
            )
            user_boteco = self._extract_first(user_boteco_response)
            return boteco, user_boteco
        except Exception as exc:
            logger.exception("Association failed; rolling back boteco creation: %s", exc)
            await self.delete_boteco(boteco["id"])
            raise

    async def provision_schema(self, boteco_username: str) -> httpx.Response:
        """Call internal API to provision schema for a new boteco."""

        api_url = os.getenv("API_URL") or "http://localhost:8000"
        endpoint = f"{api_url.rstrip('/')}/api/provision_org"
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(endpoint, json={"boteco_username": boteco_username})
                response.raise_for_status()
                return response
        except httpx.HTTPError as exc:
            logger.exception("Erro ao provisionar schema: %s", exc)
            raise

    async def check_user_has_boteco(self, user_id: str) -> bool:
        client = self._ensure_client()
        response = await self._run(
            lambda: client.table("user_boteco")
            .select("id", count="exact")
            .eq("user_id", user_id)
            .limit(1)
            .execute()
        )
        return bool(getattr(response, "count", 0))

    async def get_user_by_email(self, email: str) -> list[dict]:
        client = self._ensure_client()
        response = await self._run(
            lambda: client.table("users").select("*").eq("email", email).limit(1).execute()
        )
        return list(getattr(response, "data", []) or [])


supabase_client = SupabaseClient()
