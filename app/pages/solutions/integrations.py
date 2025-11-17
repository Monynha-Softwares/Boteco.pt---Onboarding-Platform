import reflex as rx
from app.components.header import header
from app.components.footer import footer


INTEGRATIONS = [
    {"name": "PDVs", "description": "Sincronize pedidos, cancelamentos e impressão de contas."},
    {"name": "Delivery", "description": "Receba pedidos dos apps em um só painel."},
    {"name": "Estoque/ERP", "description": "Atualize custos automaticamente e controle centros de distribuição."},
]

TIMELINE = [
    ("Dia 1", "Mapeamos sistemas atuais e usuários envolvidos."),
    ("Dia 3", "Configuramos conectores e ambientes de homologação."),
    ("Dia 7", "Liberamos check-list de testes e validamos com sua equipe."),
]


def integrations() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Integrações para manter dados em sincronia",
                    class_name="text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Conectamos Barnostri aos principais sistemas do mercado brasileiro com monitoramento 24/7.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                rx.el.a(
                    "Solicitar consultoria",
                    href="/contact",
                    class_name="mt-6 inline-flex items-center justify-center px-6 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold shadow-lg hover:bg-[#7a1a37]",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(
                    rx.el.div(
                        rx.el.h3(item["name"], class_name="text-xl font-semibold text-[#8B1E3F]"),
                        rx.el.p(item["description"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
                        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
                    )
                    for item in INTEGRATIONS
                ),
                class_name="grid gap-8 md:grid-cols-3",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Cronograma de ativação",
                    class_name="text-3xl font-bold text-[#4F3222] text-center",
                ),
                rx.el.div(
                    *(
                        rx.el.div(
                            rx.el.span(step[0], class_name="text-sm font-semibold text-[#B3701A] uppercase"),
                            rx.el.p(step[1], class_name="mt-2 text-base text-[#4F3222]"),
                            class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
                        )
                        for step in TIMELINE
                    ),
                    class_name="mt-8 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="bg-white py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Monitoramento proativo",
                    class_name="text-3xl font-bold text-white",
                ),
                rx.el.p(
                    "Alertas em tempo real, fila de reconciliação e suporte dedicado garantem continuidade mesmo em períodos de pico.",
                    class_name="mt-3 text-white/80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Falar com especialista",
                        href="/contact",
                        class_name="inline-flex items-center justify-center px-6 py-3 rounded-lg bg-white text-[#8B1E3F] font-semibold",
                    ),
                    class_name="mt-6",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
