import reflex as rx
from app.components.header import header
from app.components.footer import footer


SHOWCASE = [
    {
        "title": "Catálogo compartilhado",
        "description": "Atualize listas de produtos, unidades de medida e preços diretamente com seus fornecedores.",
    },
    {
        "title": "Aprovação em um clique",
        "description": "Receba alertas de reposição, compare propostas e aprove compras sem sair do app.",
    },
    {
        "title": "Histórico transparente",
        "description": "Registre negociações, prazos e documentos fiscais para auditorias rápidas.",
    },
]

STATS = [
    ("12h", "média de tempo ganho em cotações semanais"),
    ("-18%", "redução de custos em compras recorrentes"),
    ("3x", "mais previsibilidade nas entregas"),
]


def stat_block(value: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(value, class_name="text-3xl font-bold text-[#8B1E3F]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#4F3222] opacity-80"),
        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10 text-center",
    )


def suppliers() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Centralize fornecedores e negociações",
                    class_name="text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Automatize cotações, controle pedidos e mantenha seu estoque sempre abastecido com parceiros confiáveis.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Começar agora",
                        href="/contact",
                        class_name="inline-flex items-center justify-center px-6 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold shadow-lg hover:bg-[#7a1a37]",
                    ),
                    rx.el.a(
                        "Voltar às soluções",
                        href="/solutions",
                        class_name="ml-4 inline-flex items-center justify-center px-6 py-3 rounded-lg border border-[#8B1E3F] text-[#8B1E3F] font-semibold hover:bg-[#8B1E3F]/10",
                    ),
                    class_name="mt-6 flex flex-wrap",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(rx.el.div(
                    rx.el.h3(item["title"], class_name="text-xl font-semibold text-[#4F3222]"),
                    rx.el.p(item["description"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
                    class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
                ) for item in SHOWCASE),
                class_name="grid gap-8 md:grid-cols-3",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Números que importam",
                    class_name="text-3xl font-bold text-center text-[#8B1E3F]",
                ),
                rx.el.div(
                    *(stat_block(value, description) for value, description in STATS),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-6xl mx-auto",
            ),
            class_name="bg-white py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Fluxo de aprovação colaborativo",
                        class_name="text-3xl font-bold text-white",
                    ),
                    rx.el.p(
                        "Envie cotações para fornecedores favoritos, gere contratos e acompanhe entregas com alertas automáticos.",
                        class_name="mt-4 text-white/80",
                    ),
                ),
                rx.el.div(
                    rx.el.ul(
                        rx.el.li("Pedidos com anexos fiscais", class_name="text-white"),
                        rx.el.li("Auditoria com linha do tempo", class_name="mt-2 text-white"),
                        rx.el.li("Integração com financeiro", class_name="mt-2 text-white"),
                        class_name="mt-6 space-y-2 text-base",
                    ),
                ),
                class_name="max-w-5xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-20 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
