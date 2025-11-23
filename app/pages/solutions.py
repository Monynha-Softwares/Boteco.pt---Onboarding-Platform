import reflex as rx
from app.components.header import header
from app.components.footer import footer


def highlight_card(title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-xl font-semibold text-[#4F3222]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#4F3222] opacity-80"),
        class_name="p-6 bg-white rounded-xl shadow-md border border-gray-200/60",
    )


def solutions() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.p(
                    "SOLUÇÕES BOTECO.PT",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase text-center",
                ),
                rx.el.h1(
                    "Uma suíte completa para operar, crescer e encantar",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-center text-[#4F3222]",
                ),
                rx.el.p(
                    "Escolha apenas os módulos que precisa ou ative o pacote completo com operações, marketing e finanças integrados.",
                    class_name="mt-6 max-w-3xl mx-auto text-lg text-center text-[#4F3222] opacity-80",
                ),
                class_name="max-w-5xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/60 py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Operações sem atrito",
                    class_name="text-3xl font-bold text-[#8B1E3F]",
                ),
                rx.el.p(
                    "Automatize tarefas repetitivas e garanta consistência em todas as unidades.",
                    class_name="mt-4 text-base text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    highlight_card(
                        "Comandas e mesas conectadas",
                        "Controle em tempo real, divisão de contas e espelhos para cozinha com status visual.",
                    ),
                    highlight_card(
                        "Estoque e compras",
                        "Registre entradas, configure alertas e gere pedidos para fornecedores em poucos cliques.",
                    ),
                    highlight_card(
                        "Rotinas automatizadas",
                        "Checklists, lembretes e integrações com PDV para manter o padrão de serviço.",
                    ),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="bg-white py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Marketing e relacionamento",
                    class_name="text-3xl font-bold text-[#8B1E3F]",
                ),
                rx.el.p(
                    "Transforme visitantes em fãs com experiências personalizadas e comunicações segmentadas.",
                    class_name="mt-4 text-base text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    highlight_card(
                        "CRM para botecos",
                        "Cadastre preferências, aniversários e feedbacks para campanhas certeiras.",
                    ),
                    highlight_card(
                        "Automação omnichannel",
                        "Envie mensagens por WhatsApp, SMS e e-mail com base em eventos e metas.",
                    ),
                    highlight_card(
                        "Comunidade",
                        "Portal para clientes VIP, cupons e reservas especiais com confirmação automática.",
                    ),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="bg-[#F1DDAD]/40 py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Insights financeiros",
                    class_name="text-3xl font-bold text-[#8B1E3F]",
                ),
                rx.el.p(
                    "Saiba exatamente onde investir e quando agir para proteger sua margem.",
                    class_name="mt-4 text-base text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    highlight_card(
                        "CMV em tempo real",
                        "Compare custo, preço e lucro por item com alertas de ruptura e desperdício.",
                    ),
                    highlight_card(
                        "Relatórios contábeis",
                        "Exportações automáticas em formatos aceitos pelos principais escritórios.",
                    ),
                    highlight_card(
                        "Forecast inteligente",
                        "Projeções semanais de demanda com base em histórico, clima e eventos locais.",
                    ),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="bg-white py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h3(
                    "Precisa de algo ainda mais customizado?",
                    class_name="text-3xl font-bold text-white text-center",
                ),
                rx.el.p(
                    "Nosso time estratégico desenha fluxos sob medida, integra APIs e oferece squads dedicados.",
                    class_name="mt-4 text-white/90 text-center max-w-3xl mx-auto",
                ),
                rx.el.div(
                    rx.el.a(
                        "Converse com especialistas",
                        href="/contact",
                        class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-lg text-[#8B1E3F] bg-white hover:bg-gray-100",
                    ),
                    class_name="mt-8 flex justify-center",
                ),
                class_name="max-w-5xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4 sm:px-6 lg:px-8",
        ),
        footer(),
        class_name="bg-white font-['Inter']",
    )