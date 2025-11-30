import reflex as rx
import reflex as rx

from app.states.auth_state import AuthState
from app.states.onboarding_state import OnboardingState
from app.components.onboarding_stepper import onboarding_stepper


def form_field(
    label: str,
    placeholder: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
    name: str,
    field_type: str = "text",
    ) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-[#8C1D2C]"),
        rx.el.input(
            placeholder=placeholder,
            on_change=on_change,
            name=name,
            type=field_type,
            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-[#AA3140] focus:border-[#AA3140] sm:text-sm",
            default_value=value,
        ),
        class_name="col-span-6 sm:col-span-3",
    )


def signup_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "BotecoPro",
                    href="/",
                    class_name="text-2xl font-bold text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                ),
                class_name="py-8 px-4 sm:px-6 lg:px-8 bg-[#FFF7E8] border-b border-gray-200",
            ),
            # Use the global onboarding state so the stepper renders correctly
            # (rx.var(0) caused a runtime compile error in the Reflex compiler).
            onboarding_stepper(OnboardingState.current_step),
            rx.el.div(
                rx.el.h2("Criar Conta", class_name="text-2xl font-bold text-[#8C1D2C]"),
                rx.el.p(
                    "Crie sua conta pessoal para começar o onboarding.",
                    class_name="mt-2 text-sm text-[#8C1D2C]/80",
                ),
                rx.el.form(
                    rx.el.div(
                        form_field(
                            "Nome",
                            "",
                            OnboardingState.personal_first_name,
                            OnboardingState.set_personal_first_name,
                            name="personal_first_name",
                        ),
                        form_field(
                            "Sobrenome",
                            "",
                            OnboardingState.personal_last_name,
                            OnboardingState.set_personal_last_name,
                            name="personal_last_name",
                        ),
                        form_field(
                            "Email",
                            "",
                            OnboardingState.personal_email,
                            OnboardingState.set_personal_email,
                            name="personal_email",
                            field_type="email",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Senha",
                                class_name="block text-sm font-medium text-[#8C1D2C]",
                            ),
                            rx.el.input(
                                placeholder="Crie uma senha segura",
                                name="password",
                                type="password",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-[#AA3140] focus:border-[#AA3140] sm:text-sm",
                            ),
                            class_name="col-span-6 sm:col-span-3",
                        ),
                        form_field(
                            "CPF",
                            "",
                            OnboardingState.personal_tax_number,
                            OnboardingState.set_personal_tax_number,
                            name="personal_tax_number",
                        ),
                        form_field(
                            "Data de Nascimento",
                            "",
                            OnboardingState.personal_birth_date,
                            OnboardingState.set_personal_birth_date,
                            name="personal_birth_date",
                            field_type="date",
                        ),
                        form_field(
                            "CEP",
                            "",
                            OnboardingState.personal_postal_code,
                            OnboardingState.set_personal_postal_code,
                            name="personal_postal_code",
                        ),
                        form_field(
                            "Número da Casa/Apto",
                            "",
                            OnboardingState.personal_house_number,
                            OnboardingState.set_personal_house_number,
                            name="personal_house_number",
                        ),
                        class_name="grid grid-cols-6 gap-6 mt-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Criar Conta e Iniciar Onboarding",
                            type="submit",
                            class_name="inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140]",
                        ),
                        class_name="flex justify-end mt-8",
                    ),
                    on_submit=AuthState.register,
                ),
                class_name="max-w-2xl mx-auto p-8 bg-white rounded-xl shadow-md border border-gray-200/80",
            ),
            class_name="pb-16",
        ),
        class_name="min-h-screen bg-[#FFF7E8]/30 font-['Inter']",
    )
