import reflex as rx

from app.components.onboarding_stepper import onboarding_stepper
from app.states.onboarding_state import OnboardingState


def plan_onboarding_card(
    plan_name: str,
    price: str,
    features: list[str],
    plan_id: str,
    recommended: bool = False,
) -> rx.Component:
    is_selected = OnboardingState.selected_plan == plan_id
    return rx.el.div(
        rx.el.div(
            rx.el.h3(plan_name, class_name="text-xl font-bold text-[#8B1E3F]"),
            rx.cond(
                recommended,
                rx.el.span(
                    "Recomendado",
                    class_name="ml-3 px-2 py-0.5 text-xs font-semibold tracking-wide text-white bg-[#B3701A] rounded-full",
                ),
            ),
            class_name="flex items-center",
        ),
        rx.el.p(
            rx.el.span(
                f"R$ {price}", class_name="text-3xl font-extrabold text-[#4F3222]"
            ),
            rx.el.span(
                "/mês", class_name="text-sm font-medium text-[#4F3222] opacity-70"
            ),
            class_name="mt-2 flex items-baseline",
        ),
        rx.el.ul(
            rx.foreach(
                features,
                lambda feature: rx.el.li(
                    rx.icon(
                        tag="check", class_name="flex-shrink-0 h-5 w-5 text-green-500"
                    ),
                    rx.el.span(
                        feature, class_name="ml-2 text-sm text-[#4F3222] opacity-90"
                    ),
                    class_name="flex items-center",
                ),
            ),
            role="list",
            class_name="mt-4 space-y-2",
        ),
        class_name=rx.cond(
            is_selected,
            rx.cond(
                recommended,
                "relative p-6 bg-yellow-50/50 rounded-xl shadow-2xl border-2 border-[#B3701A] transform scale-105 transition-all",
                "relative p-6 bg-white rounded-xl shadow-lg border-2 border-[#8B1E3F] transition-all",
            ),
            rx.cond(
                recommended,
                "relative p-6 bg-white rounded-xl shadow-lg border-2 border-[#B3701A] hover:shadow-xl hover:border-[#a66a18] transition-all cursor-pointer",
                "relative p-6 bg-white/70 rounded-xl shadow-md border border-gray-200/80 hover:shadow-lg hover:border-gray-300 transition-all cursor-pointer",
            ),
        ),
        on_click=lambda: OnboardingState.set_selected_plan(plan_id),
    )


def plan_step() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "Boteco.pt",
                    href="/",
                    class_name="text-2xl font-bold text-[#8B1E3F] hover:opacity-90 transition-opacity",
                ),
                class_name="py-8 px-4 sm:px-6 lg:px-8 bg-[#F1DDAD]/50 border-b border-gray-200",
            ),
            onboarding_stepper(OnboardingState.current_step),
            rx.el.div(
                rx.el.h2(
                    "Passo 3: Escolha seu Plano",
                    class_name="text-2xl font-bold text-center text-[#4F3222]",
                ),
                rx.el.p(
                    "Selecione o plano que melhor se encaixa no seu negócio.",
                    class_name="mt-2 text-sm text-center text-[#4F3222]/80",
                ),
                rx.el.div(
                    plan_onboarding_card(
                        "Boteco",
                        "49",
                        ["Gestão de mesas", "Catálogo de produtos", "1 usuário"],
                        "boteco",
                    ),
                    plan_onboarding_card(
                        "Boteco Pro",
                        "99",
                        ["Tudo do Boteco+", "Controle de estoque", "Dashboard"],
                        "boteco_pro",
                        recommended=True,
                    ),
                    plan_onboarding_card(
                        "Boteco Patrão",
                        "199",
                        ["Tudo do Pro+", "Relatórios", "Multi-usuários"],
                        "boteco_patrao",
                    ),
                    plan_onboarding_card(
                        "Boteco Babadeiro",
                        "399",
                        ["Tudo do Patrão+", "Suporte VIP", "Multi-unidades"],
                        "boteco_babadeiro",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8 max-w-7xl mx-auto",
                ),
                rx.el.div(
                    rx.el.a(
                        "Voltar",
                        href="/onboarding/step-2-business",
                        class_name="inline-flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50",
                    ),
                    rx.el.button(
                        "Continuar para Pagamento",
                        on_click=OnboardingState.handle_plan_submit,
                        is_disabled=OnboardingState.selected_plan == "",
                        class_name="ml-4 inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8B1E3F] hover:bg-[#7a1a37] disabled:bg-gray-400 disabled:cursor-not-allowed",
                    ),
                    class_name="flex justify-center mt-12",
                ),
                class_name="w-full mx-auto px-4 sm:px-6 lg:px-8 py-8",
            ),
            class_name="pb-16",
        ),
        class_name="min-h-screen bg-[#F1DDAD]/30 font-['Inter']",
    )
