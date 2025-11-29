import logging

import reflex as rx

from app.services.supabase_client import supabase_client
from app.states.onboarding_state import OnboardingState


class AuthState(rx.State):
    """Custom auth state to register/sign-in users into onboarding flow."""

    @rx.event
    async def register(self, form_data: dict):
        """Register a new account and start onboarding."""

        first_name = form_data.get("personal_first_name", "").strip()
        last_name = form_data.get("personal_last_name", "").strip()
        email = form_data.get("personal_email", "").strip()
        password = form_data.get("password", "").strip()
        tax_number = form_data.get("personal_tax_number", "").strip()
        birth_date = form_data.get("personal_birth_date", "").strip()
        country = form_data.get("personal_country", "Brasil").strip()
        postal_code = form_data.get("personal_postal_code", "").strip()
        house_number = form_data.get("personal_house_number", "").strip()

        if not all([first_name, last_name, email, password]):
            yield rx.toast.error("Preencha nome, sobrenome, email e senha.")
            return

        username = f"{first_name.lower()}.{last_name.lower()}{tax_number[:4]}" if tax_number else f"{first_name.lower()}.{last_name.lower()}"
        user_payload = {
            "email": email,
            "username": username,
            "tax_number": tax_number or "00000000000",
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date or "1990-01-01",
            "country": country or "Brasil",
            "postal_code": postal_code or "00000000",
            "house_number": house_number or "S/N",
            "is_owner": True,
        }

        try:
            created_user = await supabase_client.create_user(user_payload, password=password)
        except Exception as exc:
            logging.exception("Failed to register user: %s", exc)
            yield rx.toast.error("Falha ao criar conta. Tente novamente.")
            return

        OnboardingState.personal_first_name = created_user.get("first_name", "")
        OnboardingState.personal_last_name = created_user.get("last_name", "")
        OnboardingState.personal_email = created_user.get("email", "")
        OnboardingState.personal_tax_number = created_user.get("tax_number", "")
        OnboardingState.personal_birth_date = created_user.get("birth_date", "")
        OnboardingState.personal_country = created_user.get("country", "Brasil")
        OnboardingState.personal_postal_code = created_user.get("postal_code", "")
        OnboardingState.personal_house_number = created_user.get("house_number", "")
        OnboardingState.user_id = created_user.get("id")

        yield rx.redirect("/onboarding/step-1-personal")

    @rx.event
    async def signin(self, form_data: dict):
        """Sign-in by email. On success, preload onboarding details."""

        email = form_data.get("email", "").strip()
        if not email:
            yield rx.toast.error("Forneça um email para entrar.")
            return

        try:
            users = await supabase_client.get_user_by_email(email)
        except Exception as exc:
            logging.exception("Sign-in failed: %s", exc)
            yield rx.toast.error("Erro no login. Tente novamente.")
            return

        if not users:
            yield rx.toast.error("Usuário não encontrado. Por favor registre-se.")
            return

        user = users[0]
        OnboardingState.user_id = user.get("id")
        OnboardingState.personal_first_name = user.get("first_name", "")
        OnboardingState.personal_last_name = user.get("last_name", "")
        OnboardingState.personal_email = user.get("email", "")

        yield rx.redirect("/onboarding/step-1-personal")
