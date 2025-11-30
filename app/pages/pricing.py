import reflex as rx
from app.components.header import header
from app.components.footer import footer


def plan_card(
    plan_name: str, price: str, features: list[str], recommended: bool = False
) -> rx.Component:
    """A card for displaying a pricing plan."""
    return rx.el.div(
        rx.el.div(
            rx.el.h3(plan_name, class_name="text-2xl font-bold text-[#8C1D2C]"),
            rx.cond(
                recommended,
                rx.el.span(
                    "Recomendado",
                    class_name="ml-3 px-3 py-1 text-xs font-semibold tracking-wide text-[#8C1D2C] bg-[#F2C94C] rounded-full",
                ),
            ),
            class_name="flex items-center",
        ),
        rx.el.p(
            rx.el.span(
                f"R$ {price}", class_name="text-4xl font-extrabold text-[#8C1D2C]"
            ),
            rx.el.span(
                "/mês", class_name="text-base font-medium text-[#8C1D2C] opacity-70"
            ),
            class_name="mt-4 flex items-baseline",
        ),
        rx.el.a(
            "Escolher Plano",
            href="/signup",
            class_name=rx.cond(
                recommended,
                "mt-8 block w-full bg-gradient-to-r from-[#8C1D2C] to-[#AA3140] border border-transparent rounded-lg py-3 text-lg font-semibold text-white text-center hover:from-[#AA3140] hover:to-[#8C1D2C] transition-all shadow-md hover:shadow-lg",
                "mt-8 block w-full bg-white border border-[#8C1D2C] rounded-lg py-3 text-lg font-semibold text-[#8C1D2C] text-center hover:bg-[#FFF7E8] transition-colors shadow-sm hover:shadow-md",
            ),
        ),
        rx.el.ul(
            rx.foreach(
                features,
                lambda feature: rx.el.li(
                    rx.icon(
                        tag="check", class_name="flex-shrink-0 h-6 w-6 text-[#4CAF50]"
                    ),
                    rx.el.span(
                        feature, class_name="ml-3 text-base text-[#8C1D2C] opacity-90"
                    ),
                    class_name="flex",
                ),
            ),
            role="list",
            class_name="mt-8 space-y-4",
        ),
        class_name=rx.cond(
            recommended,
            "relative p-8 bg-[#FFF7E8] rounded-2xl shadow-2xl border-2 border-[#F2C94C] transform hover:-translate-y-2 transition-transform duration-300",
            "p-8 bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-[#FFF7E8]/80 hover:-translate-y-1 transition-transform duration-300",
        ),
    )


def comparison_row(feature: str, plans: list[bool]) -> rx.Component:
    """A row in the feature comparison table."""
    return rx.el.tr(
        rx.el.th(
            feature,
            scope="row",
            class_name="py-5 px-6 text-sm font-medium text-[#8C1D2C] text-left",
        ),
        rx.foreach(
            plans,
            lambda available: rx.el.td(
                rx.cond(
                    available,
                    rx.icon(tag="check", class_name="h-6 w-6 text-green-500 mx-auto"),
                    rx.icon(tag="minus", class_name="h-6 w-6 text-gray-400 mx-auto"),
                ),
                class_name="py-5 px-6",
            ),
        ),
    )


def pricing() -> rx.Component:
    """The pricing page."""
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Planos que cabem no seu balcão",
                    class_name="text-4xl md:text-5xl font-extrabold text-center text-[#8C1D2C]",
                ),
                rx.el.p(
                    "Escolha o plano ideal para o seu momento. Cancele quando quiser.",
                    class_name="mt-4 max-w-2xl mx-auto text-center text-lg text-[#8C1D2C] opacity-90",
                ),
                rx.el.div(
                    plan_card(
                        "Boteco",
                        "49",
                        [
                            "Gerenciamento básico de mesas",
                            "Catálogo de produtos",
                            "Pedidos simples",
                            "1 usuário",
                        ],
                    ),
                    plan_card(
                        "Boteco Pro",
                        "99",
                        [
                            "Tudo do Boteco+",
                            "Receitas e produção interna",
                            "Controle de estoque avançado",
                            "Dashboard em tempo real",
                            "Até 5 usuários",
                        ],
                        recommended=True,
                    ),
                    plan_card(
                        "Boteco Patrão",
                        "199",
                        [
                            "Tudo do Pro+",
                            "Múltiplos usuários/cargos",
                            "Relatórios avançados",
                            "Integração com fornecedores",
                            "Até 15 usuários",
                        ],
                    ),
                    plan_card(
                        "Boteco Babadeiro",
                        "399",
                        [
                            "Tudo do Patrão+",
                            "Suporte prioritário 24/7",
                            "Customizações e integrações",
                            "Gestão de multi-unidades",
                            "Usuários ilimitados",
                        ],
                    ),
                    class_name="mt-16 max-w-7xl mx-auto grid gap-12 lg:grid-cols-4 items-start",
                ),
                class_name="py-16 sm:py-24 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#FFF7E8]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Compare os Planos",
                    class_name="text-3xl font-bold text-center text-[#8C1D2C]",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Funcionalidade",
                                    scope="col",
                                    class_name="py-3 px-6",
                                ),
                                rx.el.th(
                                    "Boteco", scope="col", class_name="py-3 px-6 w-40"
                                ),
                                rx.el.th(
                                    "Boteco Pro",
                                    scope="col",
                                    class_name="py-3 px-6 w-40",
                                ),
                                rx.el.th(
                                    "Boteco Patrão",
                                    scope="col",
                                    class_name="py-3 px-6 w-40",
                                ),
                                rx.el.th(
                                    "Boteco Babadeiro",
                                    scope="col",
                                    class_name="py-3 px-6 w-40",
                                ),
                            ),
                            class_name="text-sm font-semibold text-[#8C1D2C] bg-[#FFF7E8]/80",
                        ),
                        rx.el.tbody(
                            comparison_row(
                                "Gerenciamento de Mesas", [True, True, True, True]
                            ),
                            comparison_row(
                                "Catálogo de Produtos", [True, True, True, True]
                            ),
                            comparison_row(
                                "Controle de Estoque", [False, True, True, True]
                            ),
                            comparison_row(
                                "Dashboard em Tempo Real", [False, True, True, True]
                            ),
                            comparison_row(
                                "Relatórios Avançados", [False, False, True, True]
                            ),
                            comparison_row(
                                "Gestão de Fornecedores", [False, False, True, True]
                            ),
                            comparison_row(
                                "Suporte Prioritário", [False, False, False, True]
                            ),
                            comparison_row(
                                "Gestão Multi-unidades", [False, False, False, True]
                            ),
                            class_name="divide-y divide-gray-200 bg-white",
                        ),
                        class_name="min-w-full table-auto",
                    ),
                    class_name="mt-12 shadow-lg rounded-xl overflow-hidden border border-gray-200",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            )
        ),
        footer(),
        class_name="bg-white font-['Inter']",
    )