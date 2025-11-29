import asyncio
import pathlib
import sys

import pytest
import reflex as rx

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.states import auth_state as auth_module
from app.states.auth_state import AuthState
from app.states.onboarding_state import OnboardingState


def _consume_events(async_gen) -> list[rx.event.EventSpec]:
    events: list[rx.event.EventSpec] = []

    async def _runner():
        async for effect in async_gen:
            events.append(effect)

    asyncio.run(_runner())
    return events


def _make_state() -> AuthState:
    """Bypass Reflex runtime guard for direct instantiation in tests."""

    return object.__new__(AuthState)


def test_register_populates_onboarding_state(monkeypatch):
    class FakeSupabase:
        async def create_user(self, user_data: dict, password: str | None = None):
            return {"id": "user-123", **user_data}

    monkeypatch.setattr(auth_module, "supabase_client", FakeSupabase())
    # reset onboarding state
    OnboardingState.user_id = None
    OnboardingState.personal_first_name = ""
    OnboardingState.personal_last_name = ""
    OnboardingState.personal_email = ""

    form_data = {
        "personal_first_name": "Ana",
        "personal_last_name": "Silva",
        "personal_email": "ana@boteco.pt",
        "password": "secret",
        "personal_tax_number": "12345678900",
        "personal_birth_date": "1990-01-01",
        "personal_postal_code": "12345678",
        "personal_house_number": "10",
    }

    state = _make_state()
    events = _consume_events(state.register(form_data))

    assert OnboardingState.user_id == "user-123"
    assert OnboardingState.personal_first_name == "Ana"
    assert OnboardingState.personal_email == "ana@boteco.pt"
    assert events, "register should trigger at least one client effect"

def test_signin_populates_onboarding_state(monkeypatch):
    class FakeSupabase:
        async def get_user_by_email(self, email: str):
            return [
                {
                    "id": "existing-1",
                    "first_name": "Jon",
                    "last_name": "Doe",
                    "email": email,
                }
            ]

    monkeypatch.setattr(auth_module, "supabase_client", FakeSupabase())
    OnboardingState.user_id = None
    OnboardingState.personal_first_name = ""
    OnboardingState.personal_last_name = ""
    OnboardingState.personal_email = ""

    state = _make_state()
    events = _consume_events(state.signin({"email": "jon@boteco.pt"}))

    assert OnboardingState.user_id == "existing-1"
    assert OnboardingState.personal_first_name == "Jon"
    assert events, "signin should trigger a client redirect or toast"

def test_signin_handles_missing_user(monkeypatch):
    class FakeSupabase:
        async def get_user_by_email(self, email: str):
            return []

    monkeypatch.setattr(auth_module, "supabase_client", FakeSupabase())
    OnboardingState.user_id = None
    state = _make_state()
    events = _consume_events(state.signin({"email": "missing@boteco.pt"}))

    assert events, "missing user path should notify the client"
    assert OnboardingState.user_id is None
