import reflex as rx
from app.components.header import header
from app.components.footer import footer


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    """Card for 'How it Works' section."""
    return rx.el.div(
        rx.icon(tag=icon, class_name="h-10 w-10 text-[#B3701A]"),
        rx.el.h3(title, class_name="mt-5 text-lg font-semibold text-[#4F3222]"),
        rx.el.p(description, class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        class_name="p-6 bg-white rounded-xl shadow-md border border-gray-200/50 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def plan_preview_card(
    title: str, description: str, tag: str | None = None
) -> rx.Component:
    """Card for 'Plans Preview' section."""
    return rx.el.div(
        rx.cond(
            tag is not None,
            rx.el.span(
                tag,
                class_name="absolute top-0 right-0 -mt-3 mr-3 px-3 py-1 bg-[#B3701A] text-white text-xs font-bold rounded-full uppercase",
            ),
        ),
        rx.el.h3(title, class_name="text-xl font-bold text-[#8B1E3F]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#4F3222] opacity-80 h-12"),
        class_name="relative p-6 bg-white rounded-xl shadow-md border border-gray-200/50 h-full",
    )


def solution_card(title: str, description: str, items: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-xl font-bold text-[#4F3222]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#4F3222] opacity-80"),
        rx.el.ul(
            rx.foreach(
                items,
                lambda item: rx.el.li(
                    rx.icon(tag="check", class_name="h-4 w-4 text-[#8B1E3F]"),
                    rx.el.span(item, class_name="ml-2 text-sm text-[#4F3222]"),
                    class_name="flex items-center",
                ),
            ),
            class_name="mt-4 space-y-2",
        ),
        class_name="p-6 bg-white rounded-xl shadow-md border border-gray-200/70",
    )


def faq_item(question: str, answer: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(question, class_name="text-lg font-semibold text-[#4F3222]"),
        rx.el.p(answer, class_name="mt-2 text-sm text-[#4F3222] opacity-80"),
        class_name="p-6 rounded-xl border border-gray-200/80 bg-white shadow-sm",
    )


def index() -> rx.Component:
    """The landing page of the application."""
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Boteco.pt: gestão completa com a cara do Brasil",
                        class_name="text-4xl md:text-6xl font-extrabold text-[#4F3222] tracking-tight",
                    ),
                    rx.el.p(
                        "Digitalize operações, reduza desperdícios e encante clientes com uma central única para comandas, estoque, reservas e marketing.",
                        class_name="mt-4 max-w-2xl text-lg text-[#4F3222] opacity-90",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Comece Agora",
                            href="/sign-up",
                            class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-gradient-to-r from-[#8B1E3F] to-[#a13b5a] hover:from-[#7a1a37] hover:to-[#8B1E3F] shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300",
                        ),
                        rx.el.a(
                            "Ver Planos",
                            href="/pricing",
                            class_name="ml-4 inline-flex items-center justify-center px-8 py-3 border border-[#B3701A] text-base font-medium rounded-lg text-[#B3701A] bg-white/80 hover:bg-white transition-colors shadow-md hover:shadow-lg transform hover:-translate-y-0.5",
                        ),
                        class_name="mt-8 flex flex-wrap gap-4",
                    ),
                ),
                rx.el.div(
                    rx.image(
                        src="/placeholder.svg",
                        alt="Interface Boteco.pt sendo exibida em um tablet",
                        class_name="rounded-xl shadow-2xl w-full h-auto object-cover",
                    ),
                    class_name="hidden lg:block mt-12 lg:mt-0 lg:ml-12 w-full lg:w-1/2",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24 grid lg:grid-cols-2 items-center gap-12",
            ),
            class_name="bg-[#F1DDAD]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Como funciona",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.p(
                    "Comece a operar em 4 passos simples.",
                    class_name="mt-4 text-lg text-center text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    feature_card(
                        "user-plus",
                        "1. Cadastre-se",
                        "Crie sua conta em minutos. Informações básicas para começar a sua jornada.",
                    ),
                    feature_card(
                        "store",
                        "2. Configure seu Boteco",
                        "Adicione cardápios, horários, mesas e estoque em uma única tela responsiva.",
                    ),
                    feature_card(
                        "credit-card",
                        "3. Escolha seu Plano",
                        "Selecione o plano que acompanha o ritmo do seu crescimento, sem taxas escondidas.",
                    ),
                    feature_card(
                        "rocket",
                        "4. Comece a Operar",
                        "Acesse dashboards em tempo real e acompanhe tudo do bar ao delivery.",
                    ),
                    class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-4",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-white",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Soluções sob medida para cada etapa",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.p(
                    "Combine módulos operacionais, financeiros e de relacionamento para manter sua casa cheia todos os dias.",
                    class_name="mt-4 text-lg text-center text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    solution_card(
                        "Operações inteligentes",
                        "Padronize processos e reduza erros com fluxos integrados.",
                        [
                            "Gestão de mesas e comandas digitais",
                            "Controle de estoque com alertas de ruptura",
                            "Checklist diário com lembretes automáticos",
                        ],
                    ),
                    solution_card(
                        "Marketing e relacionamento",
                        "Crie experiências memoráveis para cada cliente.",
                        [
                            "Programas de fidelidade e listas VIP",
                            "Campanhas segmentadas por WhatsApp ou e-mail",
                            "Avaliações em tempo real para agir rápido",
                        ],
                    ),
                    solution_card(
                        "Insights financeiros",
                        "Decida com base em dados acessíveis em qualquer dispositivo.",
                        [
                            "Dashboards de margem e CMV",
                            "Previsão de demanda com IA leve",
                            "Relatórios exportáveis para o contador",
                        ],
                    ),
                    class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-3",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#F1DDAD]/40",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Planos para todos os tamanhos de sede",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.p(
                    "Do boteco da esquina à rede de bares, temos a solução certa.",
                    class_name="mt-4 text-lg text-center text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    plan_preview_card(
                        "Boteco (Básico)",
                        "Ideal para organizar comandas e reduzir espera.",
                    ),
                    plan_preview_card(
                        "Boteco Pro (Recomendado)",
                        "Controle financeiro, estoque e campanhas em um só lugar.",
                        tag="Recomendado",
                    ),
                    plan_preview_card(
                        "Boteco Patrão",
                        "Relatórios avançados, multiusuários e integrações.",
                    ),
                    plan_preview_card(
                        "Boteco Babadeiro",
                        "Suporte dedicado, multiunidades e customização.",
                    ),
                    class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-4",
                ),
                rx.el.div(
                    rx.el.a(
                        "Ver todos os detalhes dos planos",
                        href="/pricing",
                        class_name="inline-flex items-center text-[#8B1E3F] font-semibold hover:text-[#B3701A] transition-colors",
                    ),
                    class_name="mt-12 text-center",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#F1DDAD]/60",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Nossa missão", class_name="text-3xl font-bold text-[#4F3222]"
                    ),
                    rx.el.p(
                        "A Boteco.pt nasceu dentro de cozinhas apertadas e balcões cheios. Criamos tecnologia que conversa com a rotina real dos bares brasileiros, com foco em simplicidade, segurança e resultado.",
                        class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                    ),
                    rx.el.a(
                        "Saiba mais sobre nós",
                        href="/about",
                        class_name="mt-6 inline-flex items-center text-base font-semibold text-[#8B1E3F] hover:text-[#B3701A] transition-colors",
                    ),
                ),
                rx.el.div(
                    rx.image(
                        src="/placeholder.svg",
                        alt="Foto da equipe Boteco.pt",
                        class_name="rounded-xl shadow-lg w-full h-auto object-cover",
                    ),
                    class_name="hidden md:block w-full md:w-1/2",
                ),
                class_name="max-w-7xl mx-auto grid md:grid-cols-2 gap-12 items-center py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-white",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Pronto para brindar ao próximo passo?",
                        class_name="text-3xl font-bold text-white text-center",
                    ),
                    rx.el.p(
                        "Fale com especialistas Boteco.pt e receba um diagnóstico gratuito do seu fluxo atual.",
                        class_name="mt-4 text-base text-white/90 text-center",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Falar com o time",
                            href="/contact",
                            class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-lg text-[#8B1E3F] bg-white hover:bg-gray-100",
                        ),
                        class_name="mt-8 flex justify-center",
                    ),
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Perguntas frequentes",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.p(
                    "Respondemos as dúvidas mais comuns antes de você assinar.",
                    class_name="mt-4 text-lg text-center text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    faq_item(
                        "Quanto tempo demora para colocar o Boteco.pt para rodar?",
                        "Em média 48 horas. Importamos cardápios via planilha, configuramos usuários e treinamos o time em sessões rápidas.",
                    ),
                    faq_item(
                        "Preciso de hardware específico?",
                        "Não. A plataforma é 100% web e responsiva; funciona em tablets, celulares e computadores já usados no salão.",
                    ),
                    faq_item(
                        "O suporte é realmente em português?",
                        "Sim. Nosso time atende em português todos os dias, com plantões especiais em datas de grande movimento.",
                    ),
                    faq_item(
                        "Consigo integrar com sistemas legados?",
                        "As APIs abertas permitem integrar ERPs, PDVs e plataformas de delivery. Oferecemos suporte técnico durante a configuração.",
                    ),
                    class_name="mt-12 grid gap-6 md:grid-cols-2",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#F1DDAD]/40",
        ),
        footer(),
        class_name="font-['Inter']",
    )