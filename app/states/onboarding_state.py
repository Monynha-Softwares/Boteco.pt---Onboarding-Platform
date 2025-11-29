import logging

import reflex as rx

from app.services.supabase_client import supabase_client
from app.utils.validators import (
    validate_cpf_cnpj,
    validate_postal_code,
    validate_username,
)


class OnboardingState(rx.State):
    """State to manage the multi-step onboarding flow."""

    current_step: int = 1
    is_loading: bool = False
    personal_first_name: str = ""
    personal_last_name: str = ""
    personal_email: str = ""
    personal_tax_number: str = ""
    personal_birth_date: str = ""
    personal_country: str = "Brasil"
    personal_postal_code: str = ""
    personal_house_number: str = ""
    user_id: str | None = None
    business_public_name: str = ""
    business_username: str = ""
    business_tax_number: str = ""
    business_service_category: str = ""
    business_country: str = "Brasil"
    business_postal_code: str = ""
    business_vibe_tags: str = ""
    selected_plan: str = ""

    @rx.event
    async def handle_personal_submit(self, form_data: dict):
        self.personal_first_name = form_data.get("personal_first_name", "")
        self.personal_last_name = form_data.get("personal_last_name", "")
        self.personal_email = form_data.get("personal_email", "")
        self.personal_tax_number = form_data.get("personal_tax_number", "")
        self.personal_birth_date = form_data.get("personal_birth_date", "")
        self.personal_country = form_data.get("personal_country", "Brasil")
        self.personal_postal_code = form_data.get("personal_postal_code", "")
        self.personal_house_number = form_data.get("personal_house_number", "")

        if not all(
            [
                self.personal_first_name,
                self.personal_last_name,
                self.personal_email,
                self.personal_tax_number,
                self.personal_birth_date,
                self.personal_country,
                self.personal_postal_code,
                self.personal_house_number,
            ]
        ):
            yield rx.toast.error("Por favor, preencha todos os campos.")
            return
        if not validate_cpf_cnpj(self.personal_tax_number):
            yield rx.toast.error("CPF ou CNPJ inválido. Verifique os números.")
            return
        if not validate_postal_code(self.personal_postal_code):
            yield rx.toast.error("CEP inválido. Use o formato com 8 dígitos.")
            return
        self.is_loading = True
        yield
        try:
            user_data = {
                "email": self.personal_email,
                "username": f"{self.personal_first_name.lower()}.{self.personal_last_name.lower()}{self.personal_tax_number[:4]}",
                "tax_number": self.personal_tax_number,
                "first_name": self.personal_first_name,
                "last_name": self.personal_last_name,
                "birth_date": self.personal_birth_date,
                "country": self.personal_country,
                "postal_code": self.personal_postal_code,
                "house_number": self.personal_house_number,
                "is_owner": True,
            }
            created_user = await supabase_client.upsert_user(user_data)
            self.user_id = created_user.get("id")
            self.current_step = 2
            self.is_loading = False
            yield rx.redirect("/onboarding/step-2-business")
            return
        except Exception as exc:
            logging.exception("Error during personal data submission: %s", exc)
            self.is_loading = False
            yield rx.toast.error("Erro ao salvar dados. Tente novamente.")
            return

    def _validate_business_data(self) -> bool:
        return all(
            [
                self.business_public_name,
                self.business_username,
                self.business_tax_number,
                self.business_service_category,
                self.business_country,
                self.business_postal_code,
            ]
        )

    @rx.event
    async def handle_business_submit(self, form_data: dict):
        self.business_public_name = form_data.get("business_public_name", self.business_public_name)
        self.business_username = form_data.get("business_username", self.business_username)
        self.business_tax_number = form_data.get("business_tax_number", self.business_tax_number)
        self.business_service_category = form_data.get("business_service_category", self.business_service_category)
        self.business_country = form_data.get("business_country", self.business_country)
        self.business_postal_code = form_data.get("business_postal_code", self.business_postal_code)
        self.business_vibe_tags = form_data.get("business_vibe_tags", self.business_vibe_tags)

        if not self._validate_business_data():
            yield rx.toast.error("Por favor, preencha todos os campos.")
            return
        if not validate_username(self.business_username):
            yield rx.toast.error(
                "Username inválido. Use apenas letras, números e underline (min 3 caracteres)."
            )
            return
        if not validate_cpf_cnpj(self.business_tax_number):
            yield rx.toast.error("CNPJ do estabelecimento inválido.")
            return
        if not validate_postal_code(self.business_postal_code):
            yield rx.toast.error("CEP do estabelecimento inválido.")
            return
        self.current_step = 3
        yield rx.redirect("/onboarding/step-3-plan")

    @rx.event
    def handle_plan_submit(self):
        if not self.selected_plan:
            return rx.toast.error("Por favor, selecione um plano.")
        self.current_step = 4
        return rx.redirect("/onboarding/step-4-payment")

    @rx.event
    async def handle_payment_submit(self, form_data: dict):
        if not self.user_id:
            yield rx.toast.error(
                "ID do usuário não encontrado. Por favor, volte ao passo 1."
            )
            return
        self.is_loading = True
        yield
        created_boteco_id = None
        try:
            boteco_data = {
                "public_name": self.business_public_name,
                "username": self.business_username,
                "service_category": self.business_service_category,
                "vibe_tags": [
                    tag.strip()
                    for tag in self.business_vibe_tags.split(",")
                    if tag.strip()
                ],
                "establishment_tax_number": self.business_tax_number,
                "country": self.business_country,
                "postal_code": self.business_postal_code,
                "owner_tax_number": self.personal_tax_number,
                "created_by_email": self.personal_email,
                "created_by_user_id": self.user_id,
            }
            user_boteco_data = {
                "user_id": self.user_id,
                "assigned_role": "owner",
                "plan": self.selected_plan,
            }
            boteco, _ = await supabase_client.create_boteco_and_associate_user(
                boteco_data, user_boteco_data
            )
            created_boteco_id = boteco.get("id")
            try:
                await supabase_client.provision_schema(self.business_username)
                logging.info(
                    "Schema provisioning triggered for: %s", self.business_username
                )
            except Exception as provision_error:
                logging.exception(
                    "Provisioning failed, rolling back DB records: %s", provision_error
                )
                if created_boteco_id:
                    await supabase_client.delete_boteco(created_boteco_id)
                raise provision_error
            self.is_loading = False
            self.current_step = 1
            self.selected_plan = ""
            yield rx.redirect("/onboarding/success")
            return
        except Exception as exc:
            logging.exception("Error during payment/provisioning: %s", exc)
            self.is_loading = False
            yield rx.toast.error(
                f"Erro na finalização: {str(exc)}. Tente novamente."
            )
            return
