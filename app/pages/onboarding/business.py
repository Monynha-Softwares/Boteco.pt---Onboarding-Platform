import reflex as rx
import reflex as rx

from app.states.onboarding_state import OnboardingState
from app.components.onboarding_stepper import onboarding_stepper


def form_field(
    label: str,
    placeholder: str,
    value: rx.Var,
    on_change: rx.event.EventHandler,
    field_type: str = "text",
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-[#8C1D2C]"),
        rx.el.input(
            placeholder=placeholder,
            on_change=on_change,
            type=field_type,
            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-[#AA3140] focus:border-[#AA3140] sm:text-sm",
            default_value=value,
        ),
        class_name="col-span-6 sm:col-span-3",
    )


def business_step() -> rx.Component:
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
            onboarding_stepper(OnboardingState.current_step),
            rx.el.div(
                rx.el.h2(
                    "Passo 2: Dados do seu Negócio",
                    class_name="text-2xl font-bold text-[#8C1D2C]",
                ),
                rx.el.p(
                    "Agora, conte-nos um pouco sobre o seu boteco.",
                    class_name="mt-2 text-sm text-[#8C1D2C]/80",
                ),
                rx.el.form(
                    rx.el.div(
                        form_field(
                            "Nome Público do Boteco",
                            "Ex: Bar do Jonas",
                            OnboardingState.business_public_name,
                            OnboardingState.set_business_public_name,
                        ),
                        form_field(
                            "Username (@)",
                            "Ex: bardojonas",
                            OnboardingState.business_username,
                            OnboardingState.set_business_username,
                        ),
                        form_field(
                            "CNPJ do Estabelecimento",
                            "XX.XXX.XXX/XXXX-XX",
                            OnboardingState.business_tax_number,
                            OnboardingState.set_business_tax_number,
                        ),
                        form_field(
                            "Categoria de Serviço",
                            "Ex: Bar, Restaurante",
                            OnboardingState.business_service_category,
                            OnboardingState.set_business_service_category,
                        ),
                        form_field(
                            "País",
                            "Brasil",
                            OnboardingState.business_country,
                            OnboardingState.set_business_country,
                        ),
                        form_field(
                            "CEP",
                            "XXXXX-XXX",
                            OnboardingState.business_postal_code,
                            OnboardingState.set_business_postal_code,
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Tags de Vibe (separadas por vírgula)",
                                class_name="block text-sm font-medium text-[#8C1D2C]",
                            ),
                            rx.el.input(
                                placeholder="Ex: descontraído, música ao vivo, cerveja artesanal",
                                name="business_vibe_tags",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-[#AA3140] focus:border-[#AA3140] sm:text-sm",
                                default_value=OnboardingState.business_vibe_tags,
                            ),
                            class_name="col-span-6",
                        ),
                        class_name="grid grid-cols-6 gap-6 mt-6",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Voltar",
                            href="/onboarding/step-1-personal",
                            class_name="inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                        ),
                        rx.el.button(
                            "Continuar",
                            type="submit",
                            class_name="ml-4 inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140]",
                        ),
                        class_name="flex justify-end mt-8",
                    ),
                    on_submit=OnboardingState.handle_business_submit,
                ),
                class_name="max-w-2xl mx-auto p-8 bg-white rounded-xl shadow-md border border-gray-200/80",
            ),
            class_name="pb-16",
        ),
        class_name="min-h-screen bg-[#FFF7E8]/30 font-['Inter']",
    )