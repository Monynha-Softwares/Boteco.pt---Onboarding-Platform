import reflex as rx

NAV_SECTIONS: tuple[dict[str, object], ...] = (
    {
        "title": "Institucional",
        "links": (
            ("Início", "/"),
            ("Sobre", "/about"),
            ("Blog", "/blog"),
            ("Contato", "/contact"),
        ),
    },
    {
        "title": "Soluções",
        "links": (
            ("Visão geral", "/solutions"),
            ("Menu Digital", "/solutions/digital-menu"),
            ("Fornecedores", "/solutions/suppliers"),
            ("Integrações", "/solutions/integrations"),
            ("Planos", "/pricing"),
        ),
    },
    {
        "title": "Legal",
        "links": (
            ("Termos de Serviço", "/legal/terms"),
            ("Política de Privacidade", "/legal/privacy"),
        ),
    },
)


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="mt-2 block text-[#4F3222] hover:text-[#B3701A] transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#B3701A] rounded",
    )


def footer() -> rx.Component:
    """A shared footer component for the public pages."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Barnostri", class_name="text-2xl font-bold text-[#8B1E3F]"
                    ),
                    rx.el.p(
                        "Modernizando o boteco brasileiro.",
                        class_name="mt-2 text-sm text-[#4F3222] opacity-80",
                    ),
                ),
                rx.el.div(
                    *(
                        rx.el.div(
                            rx.el.h4(
                                section["title"], class_name="font-semibold text-[#4F3222]"
                            ),
                            *(footer_link(text, href) for text, href in section["links"]),
                            class_name="space-y-2",
                        )
                        for section in NAV_SECTIONS
                    ),
                    rx.el.div(
                        rx.el.h4("Contato", class_name="font-semibold text-[#4F3222]"),
                        rx.el.p(
                            "contato@barnostri.com", class_name="mt-4 text-[#4F3222]"
                        ),
                        rx.el.div(
                            rx.icon(
                                tag="facebook",
                                class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                            ),
                            rx.icon(
                                tag="instagram",
                                class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                            ),
                            rx.icon(
                                tag="twitter",
                                class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                            ),
                            class_name="flex mt-4 space-x-4",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
                ),
                class_name="grid md:grid-cols-2 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    f"© {2024} Barnostri. Todos os direitos reservados.",
                    class_name="text-sm text-[#4F3222] opacity-70",
                ),
                class_name="mt-12 pt-8 border-t border-[#4F3222]/10 text-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-[#F1DDAD]/50",
    )