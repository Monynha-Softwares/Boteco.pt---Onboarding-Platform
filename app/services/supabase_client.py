import os
from supabase import create_client, Client
from postgrest import APIResponse
import logging
import httpx


class SupabaseClient:
    """A helper class to interact with the Supabase backend."""

    def __init__(self):
        self.url: str | None = os.environ.get("SUPABASE_URL")
        self.key: str | None = os.environ.get(
            "SUPABASE_SERVICE_ROLE_KEY"
        ) or os.environ.get("SUPABASE_KEY")
        self.client: Client | None = self._initialize_client()

    def _initialize_client(self) -> Client | None:
        if self.url and self.key:
            try:
                return create_client(self.url, self.key)
            except Exception as e:
                logging.exception(f"Error initializing Supabase client: {e}")
        return None

    def get_client(self) -> Client | None:
        """Returns the Supabase client instance."""
        return self.client

    async def upsert_user(self, user_data: dict) -> APIResponse:
        """Insert or update a user record."""
        if not self.client:
            raise ConnectionError("Supabase client not initialized.")
        return (
            await self.client.table("users")
            .upsert(user_data, on_conflict="email")
            .execute()
        )

    async def create_boteco_and_associate_user(
        self, boteco_data: dict, user_boteco_data: dict
    ) -> tuple[APIResponse, APIResponse]:
        """Creates a boteco and associates a user to it."""
        if not self.client:
            raise ConnectionError("Supabase client not initialized.")
        boteco_response = (
            await self.client.table("boteco").insert(boteco_data).execute()
        )
        if not boteco_response.data:
            raise Exception(
                f"Failed to create boteco: {(boteco_response.error.message if boteco_response.error else 'Unknown error')}"
            )
        boteco_id = boteco_response.data[0]["id"]
        user_boteco_data["boteco_id"] = boteco_id
        user_boteco_response = (
            await self.client.table("user_boteco").insert(user_boteco_data).execute()
        )
        if not user_boteco_response.data:
            logging.error(
                "Failed to associate user with boteco, boteco record remains."
            )
            raise Exception(
                f"Failed to associate user to boteco: {(user_boteco_response.error.message if user_boteco_response.error else 'Unknown error')}"
            )
        return (boteco_response, user_boteco_response)

    async def provision_schema(self, boteco_username: str) -> httpx.Response:
        """Calls the internal API to provision a new schema for the boteco."""
        api_url = "http://localhost:8000/api/provision_org"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                api_url, json={"boteco_username": boteco_username}
            )
            response.raise_for_status()
            return response

    async def check_user_has_boteco(self, user_id: str) -> bool:
        """Check if a user is associated with any boteco."""
        if not self.client:
            raise ConnectionError("Supabase client not initialized.")
        response = (
            await self.client.table("user_boteco")
            .select("id", count="exact")
            .eq("user_id", user_id)
            .limit(1)
            .execute()
        )
        return response.count > 0


supabase_client = SupabaseClient()