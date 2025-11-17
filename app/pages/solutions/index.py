import reflex as rx
from app.components.header import header
from app.components.footer import footer


SOLUTIONS = [
    {
        "title": "Menu Digital Interativo",
        "description": "Atualize pratos, fotos e ofertas em tempo real e permita pedidos diretamente pela mesa.",
        "icon": "tablet-smartphone",
        "href": "/solutions/digital-menu",
    },
    {
        "title": "Gestão de Fornecedores",
        "description": "Negocie, aprove pedidos e acompanhe entregas com transparência em um só painel.",
        "icon": "truck",
        "href": "/solutions/suppliers",
    },
    {
        "title": "Integrações Inteligentes",
        "description": "Conecte o Barnostri ao PDV, delivery e estoque para manter todos os dados sincronizados.",
        "icon": "git-merge",
        "href": "/solutions/integrations",
    },
]

BENEFITS = [
    {
        "title": "Processos mais rápidos",
        "description": "Fluxos automatizados reduzem esperas e liberam sua equipe para encantar clientes.",
    },
    {
        "title": "Visão completa",
        "description": "Dashboards unificados mostram vendas, custos e alertas em tempo real.",
    },
    {
        "title": "Escalabilidade",
        "description": "Adicione novas unidades ou parceiros sem reinventar processos internos.",
    },
]

FAQ = [
    {
        "question": "Posso contratar apenas um dos módulos?",
        "answer": "Sim. Cada solução possui assinatura independente e pode ser combinada com outras quando fizer sentido.",
    },
    {
        "question": "Existe suporte para treinar minha equipe?",
        "answer": "Oferecemos sessões remotas e materiais gravados em português para acelerar o onboarding.",
    },
    {
        "question": "As integrações cobrem quais sistemas?",
        "answer": "Mantemos conectores prontos para os principais PDVs, ERPs de estoque e apps de entrega do mercado brasileiro.",
    },
]


def solution_card(solution: dict[str, str]) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=solution["icon"], class_name="h-10 w-10 text-[#8B1E3F]"),
        rx.el.h3(solution["title"], class_name="mt-4 text-xl font-semibold text-[#4F3222]"),
        rx.el.p(solution["description"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        rx.el.span(
            "Ver detalhes",
            class_name="mt-4 inline-flex items-center text-sm font-semibold text-[#8B1E3F]",
        ),
        href=solution["href"],
        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10 hover:-translate-y-1 hover:shadow-xl transition-all focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#B3701A]",
    )


def benefit_card(benefit: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.h4(benefit["title"], class_name="text-lg font-semibold text-[#8B1E3F]"),
        rx.el.p(benefit["description"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        class_name="p-5 rounded-xl bg-[#F1DDAD]/60 border border-[#4F3222]/10",
    )


def faq_item(item: dict[str, str]) -> rx.Component:
    return rx.el.details(
        rx.el.summary(item["question"], class_name="cursor-pointer text-lg font-semibold text-[#4F3222]"),
        rx.el.p(item["answer"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        class_name="p-4 rounded-xl bg-white border border-[#4F3222]/10",
    )


def solutions_overview() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.p(
                    "Suite modular Barnostri",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(
                    "Escolha a solução que acelera seu boteco",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Combine menu digital, fornecedores e integrações para padronizar operações sem perder a essência brasileira.",
                    class_name="mt-6 text-lg text-[#4F3222] opacity-80 max-w-2xl",
                ),
                rx.el.div(
                    rx.el.a(
                        "Falar com especialistas",
                        href="/contact",
                        class_name="inline-flex items-center justify-center px-6 py-3 rounded-lg text-white bg-[#8B1E3F] font-semibold shadow-lg hover:bg-[#7a1a37]",
                    ),
                    rx.el.a(
                        "Explorar o blog",
                        href="/blog",
                        class_name="ml-4 inline-flex items-center justify-center px-6 py-3 rounded-lg border border-[#8B1E3F] text-[#8B1E3F] font-semibold hover:bg-[#8B1E3F]/10",
                    ),
                    class_name="mt-8 flex flex-wrap",
                ),
                class_name="max-w-5xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(solution_card(solution) for solution in SOLUTIONS),
                class_name="grid gap-8 md:grid-cols-3",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Por que centralizar com a Barnostri?",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.p(
                    "A mesma experiência visual, suporte e dados compartilhados, independente do módulo escolhido.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80 text-center",
                ),
                rx.el.div(
                    *(benefit_card(benefit) for benefit in BENEFITS),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
                class_name="max-w-6xl mx-auto",
            ),
            class_name="bg-white py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Perguntas frequentes",
                    class_name="text-3xl font-bold text-[#4F3222] text-center",
                ),
                rx.el.div(
                    *(faq_item(item) for item in FAQ),
                    class_name="mt-10 space-y-4",
                ),
                class_name="max-w-4xl mx-auto",
            ),
            class_name="bg-[#F1DDAD]/60 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Pronto para montar seu mix ideal?",
                    class_name="text-3xl font-bold text-white",
                ),
                rx.el.p(
                    "Nossa equipe mapeia processos atuais, indica módulos e entrega um plano de ativação em até 7 dias.",
                    class_name="mt-3 text-white/80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Agendar conversa",
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
