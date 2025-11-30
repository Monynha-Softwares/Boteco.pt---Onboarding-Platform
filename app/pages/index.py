import reflex as rx
from app.components.header import header
from app.components.footer import footer


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    """Card for 'How it Works' section."""
    return rx.el.div(
        rx.icon(tag=icon, class_name="h-10 w-10 text-[#F2C94C]"),
        rx.el.h3(title, class_name="mt-5 text-lg font-semibold text-[#8C1D2C]"),
        rx.el.p(description, class_name="mt-2 text-base text-[#8C1D2C] opacity-80"),
        class_name="p-6 bg-white rounded-xl shadow-md border border-[#FFF7E8]/60 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
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
                class_name="absolute top-0 right-0 -mt-3 mr-3 px-3 py-1 bg-[#F2C94C] text-[#8C1D2C] text-xs font-bold rounded-full uppercase",
            ),
        ),
        rx.el.h3(title, class_name="text-xl font-bold text-[#8C1D2C]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#8C1D2C] opacity-80 h-12"),
        class_name="relative p-6 bg-white rounded-xl shadow-md border border-[#FFF7E8]/70 h-full",
    )


def solution_card(title: str, description: str, items: list[str]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-xl font-bold text-[#8C1D2C]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#8C1D2C] opacity-80"),
        rx.el.ul(
            rx.foreach(
                items,
                lambda item: rx.el.li(
                    rx.icon(tag="check", class_name="h-4 w-4 text-[#4CAF50]"),
                    rx.el.span(item, class_name="ml-2 text-sm text-[#8C1D2C]"),
                    class_name="flex items-center",
                ),
            ),
            class_name="mt-4 space-y-2",
        ),
        class_name="p-6 bg-white rounded-xl shadow-md border border-[#FFF7E8]/70",
    )


def faq_item(question: str, answer: str) -> rx.Component:
    return rx.el.div(
        rx.el.h3(question, class_name="text-lg font-semibold text-[#8C1D2C]"),
        rx.el.p(answer, class_name="mt-2 text-sm text-[#8C1D2C] opacity-80"),
        class_name="p-6 rounded-xl border border-[#FFF7E8]/80 bg-white shadow-sm",
    )


def index() -> rx.Component:
    """The landing page of the application."""
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "BotecoPro: gestão global e inclusiva para bares e restaurantes",
                        class_name="text-4xl md:text-6xl font-extrabold text-[#8C1D2C] tracking-tight",
                    ),
                    rx.el.p(
                        "Digitalize operações, reduza desperdícios e encante clientes com uma plataforma multi-tenant e multi-região desenvolvida pela Monynha Softwares.",
                        class_name="mt-4 max-w-2xl text-lg text-[#8C1D2C] opacity-90",
                    ),
                    rx.el.p(
                        "Powered by Monynha Softwares — https://monynha.com",
                        class_name="mt-2 text-sm font-semibold text-[#AA3140]",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Comece Agora",
                            href="/signup",
                            class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-gradient-to-r from-[#8C1D2C] to-[#AA3140] hover:from-[#AA3140] hover:to-[#8C1D2C] shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all duration-300",
                        ),
                        rx.el.a(
                            "Ver Planos",
                            href="/pricing",
                            class_name="ml-4 inline-flex items-center justify-center px-8 py-3 border border-[#AA3140] text-base font-medium rounded-lg text-[#AA3140] bg-white/80 hover:bg-white transition-colors shadow-md hover:shadow-lg transform hover:-translate-y-0.5",
                        ),
                        class_name="mt-8 flex flex-wrap gap-4",
                    ),
                ),
                rx.el.div(
                    rx.image(
                        src="/placeholder.svg",
                        alt="Interface BotecoPro sendo exibida em um tablet",
                        class_name="rounded-xl shadow-2xl w-full h-auto object-cover",
                    ),
                    class_name="hidden lg:block mt-12 lg:mt-0 lg:ml-12 w-full lg:w-1/2",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24 grid lg:grid-cols-2 items-center gap-12",
            ),
            class_name="bg-[#FFF7E8]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Como funciona",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.p(
                    "Comece a operar em 4 passos simples.",
                    class_name="mt-4 text-lg text-center text-[#8C1D2C] opacity-80",
                ),
                rx.el.div(
                    feature_card(
                        "user-plus",
                        "1. Cadastre-se",
                        "Crie sua conta em minutos. Informações básicas para começar a sua jornada.",
                    ),
                    feature_card(
                        "store",
                        "2. Configure seu BotecoPro",
                        "Adicione cardápios, horários, mesas e estoque em uma única tela responsiva, com governança multi-unidade.",
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
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.p(
                    "Combine módulos operacionais, financeiros e de relacionamento para manter sua casa cheia todos os dias.",
                    class_name="mt-4 text-lg text-center text-[#8C1D2C] opacity-80",
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
            class_name="bg-[#FFF7E8]/60",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Planos para todos os tamanhos de sede",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.p(
                    "Do boteco da esquina à rede de bares, temos a solução certa.",
                    class_name="mt-4 text-lg text-center text-[#8C1D2C] opacity-80",
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
                        class_name="inline-flex items-center text-[#8C1D2C] font-semibold hover:text-[#AA3140] transition-colors",
                    ),
                    class_name="mt-12 text-center",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#FFF7E8]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Missão, visão e valores",
                        class_name="text-3xl font-bold text-[#8C1D2C]",
                    ),
                    rx.el.p(
                        "Missão: Empoderar bares e restaurantes através de tecnologia intuitiva, eficiente e inclusiva.",
                        class_name="mt-4 text-lg text-[#8C1D2C] opacity-90",
                    ),
                    rx.el.p(
                        "Visão: Tornar-se a principal plataforma de gestão para o setor gastronômico, reconhecida internacionalmente pela inovação, acessibilidade e forte suporte ao cliente.",
                        class_name="mt-3 text-lg text-[#8C1D2C] opacity-85",
                    ),
                    rx.el.p(
                        "BotecoPro é desenvolvido e mantido pela Monynha Softwares, um estúdio global e inclusivo de tecnologia especializado em plataformas web e mobile, integrações, DX e soluções com IA.",
                        class_name="mt-3 text-base text-[#8C1D2C] opacity-85",
                    ),
                    rx.el.ul(
                        rx.el.li("Orgulho na Diversidade", class_name="font-semibold text-[#AA3140]"),
                        rx.el.li("Resiliência & Inovação", class_name="font-semibold text-[#AA3140]"),
                        rx.el.li("Colaboração & Transparência", class_name="font-semibold text-[#AA3140]"),
                        rx.el.li("Tecnologia Centrada no Humano", class_name="font-semibold text-[#AA3140]"),
                        rx.el.li("Acessibilidade por Padrão (Accessibility by Design)", class_name="font-semibold text-[#AA3140]"),
                        class_name="mt-6 space-y-2 text-sm text-[#8C1D2C]",
                    ),
                    rx.el.a(
                        "Saiba mais sobre nós",
                        href="/about",
                        class_name="mt-8 inline-flex items-center text-base font-semibold text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                    ),
                ),
                rx.el.div(
                    rx.image(
                        src="/placeholder.svg",
                        alt="Equipe BotecoPro e Monynha Softwares", 
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
                rx.el.h2(
                    "Presença global com cuidado local",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.p(
                    "BotecoPro e Monynha Softwares operam em múltiplos mercados com conformidade regional e suporte multilíngue.",
                    class_name="mt-4 text-base text-center text-[#8C1D2C] opacity-85",
                ),
                rx.el.div(
                    feature_card(
                        "map-pin",
                        "Brasil",
                        "Soluções adaptadas ao mercado local e às rotinas intensas de bares e restaurantes brasileiros.",
                    ),
                    feature_card(
                        "globe-2",
                        "Portugal",
                        "Operação em conformidade com normas da União Europeia e suporte multilíngue para equipes diversas.",
                    ),
                    feature_card(
                        "shield",
                        "Suíça",
                        "Clientes com alta exigência de qualidade, segurança e padrões corporativos internacionais.",
                    ),
                    class_name="mt-10 grid gap-6 md:grid-cols-3",
                ),
            ),
            class_name="bg-[#FFF7E8] py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Pronto para brindar ao próximo passo?",
                        class_name="text-3xl font-bold text-white text-center",
                    ),
                    rx.el.p(
                        "Fale com especialistas BotecoPro e Monynha Softwares e receba um diagnóstico gratuito do seu fluxo atual.",
                        class_name="mt-4 text-base text-white/90 text-center",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Falar com o time",
                            href="/contact",
                            class_name="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-lg text-[#8C1D2C] bg-white hover:bg-[#FFF7E8]",
                        ),
                        class_name="mt-8 flex justify-center",
                    ),
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#8C1D2C] py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Perguntas frequentes",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.p(
                    "Respondemos as dúvidas mais comuns antes de você assinar.",
                    class_name="mt-4 text-lg text-center text-[#8C1D2C] opacity-80",
                ),
                rx.el.div(
                    faq_item(
                        "Quanto tempo demora para colocar o BotecoPro para rodar?",
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
            class_name="bg-[#FFF7E8]/60",
        ),
        footer(),
        class_name="font-['Inter']",
    )