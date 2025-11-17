import reflex as rx
from app.components.header import header
from app.components.footer import footer


BENEFITS = [
    "Atualizações ilimitadas em tempo real com controle de estoque integrado.",
    "Pedidos por QR Code com pagamento antecipado ou na conta.",
    "Traduções automáticas para turistas e personalização por unidade.",
]

WORKFLOW = [
    "Cadastre pratos e fotos com editor visual.",
    "Sincronize disponibilidade conforme saída de estoque.",
    "Receba pedidos diretamente no tablet da equipe ou no PDV integrado.",
]


def highlight_item(text: str) -> rx.Component:
    return rx.el.li(
        rx.icon(tag="check", class_name="h-5 w-5 text-[#8B1E3F]"),
        rx.el.span(text, class_name="ml-3 text-base text-[#4F3222]"),
        class_name="flex items-start",
    )


def digital_menu() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Menu digital pensado para botecos brasileiros",
                    class_name="text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Ative pedidos por QR Code, destaque promoções e integre fotos autênticas do seu cardápio sem depender de terceiros.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Solicitar demonstração",
                        href="/contact",
                        class_name="inline-flex items-center justify-center px-6 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold shadow-lg hover:bg-[#7a1a37]",
                    ),
                    rx.el.a(
                        "Ver todas as soluções",
                        href="/solutions",
                        class_name="ml-4 inline-flex items-center justify-center px-6 py-3 rounded-lg border border-[#8B1E3F] text-[#8B1E3F] font-semibold hover:bg-[#8B1E3F]/10",
                    ),
                    class_name="mt-6 flex flex-wrap",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD] py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Benefícios imediatos",
                        class_name="text-3xl font-bold text-[#8B1E3F]",
                    ),
                    rx.el.ul(
                        *(highlight_item(benefit) for benefit in BENEFITS),
                        class_name="mt-6 space-y-4",
                    ),
                ),
                rx.el.div(
                    rx.el.h3(
                        "Fluxo simplificado",
                        class_name="text-2xl font-semibold text-[#4F3222]",
                    ),
                    rx.el.ol(
                        *(rx.el.li(step, class_name="text-base text-[#4F3222] opacity-80") for step in WORKFLOW),
                        class_name="mt-4 list-decimal list-inside space-y-2",
                    ),
                ),
                class_name="grid gap-12 md:grid-cols-2",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Funcionalidades inclusas",
                        class_name="text-3xl font-bold text-white",
                    ),
                    rx.el.p(
                        "Painel responsivo, layouts sazonais, sugestões automatizadas e acompanhamento de performance de pratos.",
                        class_name="mt-3 text-white/80",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Modo foto + texto",
                            class_name="text-sm font-semibold text-[#8B1E3F]",
                        ),
                        rx.el.p(
                            "Combine imagens autorais com descrições detalhadas e traduções para até 4 idiomas.",
                            class_name="mt-2 text-base text-[#4F3222]",
                        ),
                        class_name="p-6 rounded-2xl bg-white shadow-lg",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "Campanhas diárias",
                            class_name="text-sm font-semibold text-[#8B1E3F]",
                        ),
                        rx.el.p(
                            "Programe promoções relâmpago e destaque automaticamente itens com maior margem.",
                            class_name="mt-2 text-base text-[#4F3222]",
                        ),
                        class_name="p-6 rounded-2xl bg-white shadow-lg",
                    ),
                    class_name="grid gap-6 md:grid-cols-2 mt-10",
                ),
                class_name="max-w-5xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Integração com o restante da plataforma",
                    class_name="text-3xl font-bold text-[#4F3222]",
                ),
                rx.el.p(
                    "Sincronize automaticamente estoque, planos de fidelidade e relatórios do Barnostri para manter a comunicação coerente em todos os canais.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-white py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
