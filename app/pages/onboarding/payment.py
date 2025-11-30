import reflex as rx
from app.states.onboarding_state import OnboardingState
from app.components.onboarding_stepper import onboarding_stepper


def payment_step() -> rx.Component:
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
                    "Passo 4: Pagamento", class_name="text-2xl font-bold text-[#8C1D2C]"
                ),
                rx.el.p(
                    "Simulação de checkout. Insira dados fictícios.",
                    class_name="mt-2 text-sm text-[#8C1D2C]/80",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Plano Escolhido", class_name="font-semibold text-[#8C1D2C]"
                        ),
                        rx.el.p(
                            OnboardingState.selected_plan,
                            class_name="capitalize font-bold text-lg text-[#8C1D2C]",
                        ),
                        class_name="flex justify-between items-center p-4 bg-[#FFF7E8] border border-[#F2C94C]/60 rounded-lg",
                    ),
                    class_name="mt-6",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Número do Cartão",
                            class_name="block text-sm font-medium text-[#4F3222]",
                        ),
                        rx.el.div(
                            rx.icon("credit-card", class_name="h-5 w-5 text-gray-400"),
                            rx.el.input(
                                placeholder="XXXX XXXX XXXX XXXX",
                                class_name="block w-full border-0 p-0 text-gray-900 placeholder-gray-400 focus:ring-0 sm:text-sm",
                            ),
                            class_name="relative mt-1 rounded-md shadow-sm flex items-center px-3 border border-gray-300 focus-within:ring-1 focus-within:ring-[#B3701A] focus-within:border-[#B3701A]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Validade",
                                class_name="block text-sm font-medium text-[#4F3222]",
                            ),
                            rx.el.input(
                                placeholder="MM/AA",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "CVC",
                                class_name="block text-sm font-medium text-[#4F3222]",
                            ),
                            rx.el.input(
                                placeholder="XXX",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                            ),
                        ),
                        class_name="grid grid-cols-2 gap-4 mt-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Nome no Cartão",
                            class_name="block text-sm font-medium text-[#4F3222]",
                        ),
                        rx.el.input(
                            placeholder="Nome Completo",
                            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                        ),
                        class_name="mt-4",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Voltar",
                            href="/onboarding/step-3-plan",
                            class_name="inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                        ),
                        rx.el.button(
                              rx.cond(
                                  OnboardingState.is_loading,
                                  rx.el.div(
                                      rx.spinner(class_name="h-4 w-4"),
                                      "Processando pagamento",
                                      class_name="flex items-center gap-2",
                                  ),
                                  "Finalizar e Pagar",
                              ),
                            type="submit",
                            is_disabled=OnboardingState.is_loading,
                            class_name="ml-4 inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140] disabled:bg-gray-400",
                        ),
                        class_name="flex justify-end mt-8",
                    ),
                    on_submit=OnboardingState.handle_payment_submit,
                ),
                class_name="max-w-2xl mx-auto p-8 mt-4 bg-white rounded-xl shadow-md border border-gray-200/80",
            ),
            class_name="pb-16",
        ),
        class_name="min-h-screen bg-[#FFF7E8]/30 font-['Inter']",
    )