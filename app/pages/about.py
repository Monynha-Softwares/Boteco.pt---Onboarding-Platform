import reflex as rx

from app.components.footer import footer
from app.components.header import header


def info_card(icon: str, title: str, description: str) -> rx.Component:
    """A card for displaying company values."""
    return rx.el.div(
        rx.icon(tag=icon, class_name="h-10 w-10 text-[#F2C94C]"),
        rx.el.h3(title, class_name="mt-4 text-xl font-semibold text-[#8C1D2C]"),
        rx.el.p(description, class_name="mt-2 text-base text-[#8C1D2C] opacity-80"),
        class_name="p-8 bg-white rounded-xl shadow-md border border-[#FFF7E8]/60 hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def team_member_card(name: str, role: str, image_url: str) -> rx.Component:
    """A card for displaying a team member."""
    initials = "".join((n[0] for n in name.split()))[:2].upper()
    return rx.el.div(
        rx.cond(
            image_url == "/placeholder.svg",
            rx.el.div(
                rx.el.span(initials, class_name="text-3xl font-bold text-[#8C1D2C]"),
                class_name="h-32 w-32 rounded-full mx-auto bg-[#FFF7E8] flex items-center justify-center border-2 border-[#8C1D2C]/20",
            ),
            rx.image(
                src=image_url,
                alt=name,
                class_name="h-32 w-32 rounded-full mx-auto object-cover",
            ),
        ),
        rx.el.h3(name, class_name="mt-4 text-lg font-medium text-[#8C1D2C]"),
        rx.el.p(role, class_name="text-[#AA3140] text-sm font-semibold"),
        class_name="text-center",
    )


def about() -> rx.Component:
    """The About Us page."""
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Sobre o BotecoPro",
                    class_name="text-4xl md:text-5xl font-extrabold text-[#8C1D2C] tracking-tight text-center",
                ),
                rx.el.p(
                    "Plataforma de gestão desenvolvida e mantida pela Monynha Softwares, combinando operações multi-tenant, acessibilidade e suporte humano para bares e restaurantes em múltiplas regiões.",
                    class_name="mt-6 max-w-3xl mx-auto text-lg text-[#8C1D2C] text-center opacity-90",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#FFF7E8]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Nossa História", class_name="text-3xl font-bold text-[#8C1D2C]"
                    ),
                    rx.el.p(
                        "A Monynha Softwares nasceu da paixão por tecnologia, inclusão e pelo setor de alimentos e bebidas. O nome ‘Monynha’ representa resiliência, criatividade e diversidade — valores fundamentais que inspiram cada produto que desenvolvemos.",
                        class_name="mt-4 text-lg text-[#8C1D2C] opacity-85",
                    ),
                    rx.el.p(
                        "O BotecoPro foi criado para empoderar empreendedores com ferramentas modernas, confiáveis e intuitivas, respeitando a identidade de cada casa e oferecendo suporte próximo e multilíngue.",
                        class_name="mt-4 text-lg text-[#8C1D2C] opacity-85",
                    ),
                ),
                class_name="max-w-4xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Parceiro tecnológico oficial",
                        class_name="text-3xl font-bold text-[#8C1D2C]",
                    ),
                    rx.el.p(
                        "A Monynha Softwares é um estúdio global e inclusivo de tecnologia, especializado em plataformas web e mobile, sistemas multi-tenant e multi-região, integrações e APIs, experiência do desenvolvedor, soluções com IA e consultoria técnica.",
                        class_name="mt-4 text-base text-[#8C1D2C] opacity-85",
                    ),
                    rx.el.p(
                        "BotecoPro é Powered by Monynha Softwares — https://monynha.com",
                        class_name="mt-3 text-sm font-semibold text-[#AA3140]",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Presença internacional",
                            class_name="text-xl font-semibold text-[#8C1D2C] mt-6",
                        ),
                        rx.el.ul(
                            rx.el.li("Brasil — soluções adaptadas ao mercado local"),
                            rx.el.li("Portugal — conformidade com normas da União Europeia e suporte multilíngue"),
                            rx.el.li("Suíça — clientes de alta exigência e padrões empresariais"),
                            class_name="mt-3 space-y-2 text-[#8C1D2C]",
                        ),
                        class_name="bg-white p-6 rounded-xl shadow-sm border border-[#FFF7E8]/70",
                    ),
                ),
                class_name="max-w-5xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-white",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Nossos Valores",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.div(
                    info_card(
                        "sparkle",
                        "Orgulho na Diversidade",
                        "Celebramos equipes plurais e construímos produtos que respeitam diferentes culturas e contextos de atendimento.",
                    ),
                    info_card(
                        "activity",
                        "Resiliência & Inovação",
                        "Iteramos rápido, aprendemos com cada operação e mantemos estabilidade para quem depende do BotecoPro todos os dias.",
                    ),
                    info_card(
                        "handshake",
                        "Colaboração & Transparência",
                        "Trabalhamos lado a lado com clientes e parceiros, compartilhando dados e decisões com clareza.",
                    ),
                    info_card(
                        "heart",
                        "Tecnologia Centrada no Humano",
                        "Escolhas de produto orientadas por impacto real em quem opera na linha de frente e em quem consome no balcão.",
                    ),
                    info_card(
                        "accessibility",
                        "Acessibilidade por Padrão",
                        "Accessibility by Design em cada fluxo, garantindo experiências inclusivas em todas as telas e idiomas.",
                    ),
                    class_name="mt-12 grid gap-8 md:grid-cols-2 lg:grid-cols-3",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#FFF7E8]",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Conheça o time",
                    class_name="text-3xl font-bold text-[#8C1D2C] text-center",
                ),
                rx.el.div(
                    team_member_card("Marcelo Santos", "Fundador", "/placeholder.svg"),
                    team_member_card(
                        "Tércio Barretoyan", "Diretor Estratégico", "/placeholder.svg"
                    ),
                    team_member_card(
                        "Sofia Reis", "Head de Design", "/placeholder.svg"
                    ),
                    team_member_card(
                        "Millena Martins",
                        "Head de Relações Públicas",
                        "/placeholder.svg",
                    ),
                    class_name="mt-12 grid gap-12 sm:grid-cols-2 lg:grid-cols-4",
                ),
                class_name="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Pronto para transformar seu negócio?",
                    class_name="text-3xl font-extrabold text-white",
                ),
                rx.el.a(
                    "Veja nossos planos",
                    href="/pricing",
                    class_name="mt-8 w-full inline-flex items-center justify-center px-6 py-3 border border-transparent rounded-md shadow-sm text-base font-medium text-[#8C1D2C] bg-white hover:bg-[#FFF7E8] sm:w-auto transition-colors",
                ),
                class_name="max-w-2xl mx-auto text-center py-16 px-4 sm:py-20 sm:px-6 lg:px-8",
            ),
            class_name="bg-[#8C1D2C]",
        ),
        footer(),
        class_name="bg-white font-['Inter']",
    )