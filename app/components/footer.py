import reflex as rx


def footer() -> rx.Component:
    """A shared footer component for the public pages."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "BotecoPro", class_name="text-2xl font-bold text-[#8C1D2C]"
                    ),
                    rx.el.p(
                        "Plataforma de gestão para bares e restaurantes, com tecnologia global e inclusiva.",
                        class_name="mt-2 text-sm text-[#8C1D2C] opacity-80",
                    ),
                    rx.el.a(
                        "Powered by Monynha Softwares — monynha.com",
                        href="https://monynha.com",
                        target="_blank",
                        rel="noreferrer",
                        class_name="mt-3 inline-flex text-sm font-semibold text-[#AA3140] hover:text-[#8C1D2C]",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "Navegação", class_name="font-semibold text-[#8C1D2C]"
                        ),
                        rx.el.a(
                            "Início",
                            href="/",
                            class_name="mt-4 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Planos",
                            href="/pricing",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Sobre",
                            href="/about",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Soluções",
                            href="/solutions",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Contato",
                            href="/contact",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4("Legal", class_name="font-semibold text-[#8C1D2C]"),
                        rx.el.a(
                            "Termos de Serviço",
                            href="#",
                            class_name="mt-4 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Política de Privacidade",
                            href="#",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Marca registrada",
                            href="#",
                            class_name="mt-2 block text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4("Contato", class_name="font-semibold text-[#8C1D2C]"),
                        rx.el.p("contato@botecopro.com", class_name="mt-4 text-[#8C1D2C]"),
                        rx.el.a(
                            "Monynha Softwares",
                            href="https://monynha.com",
                            target="_blank",
                            rel="noreferrer",
                            class_name="mt-2 inline-flex text-sm font-semibold text-[#AA3140] hover:text-[#8C1D2C]",
                        ),
                        rx.el.div(
                            rx.el.a(
                                rx.icon(
                                    tag="facebook",
                                    class_name="h-6 w-6 text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                                ),
                                href="https://facebook.com/boteco.pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Facebook BotecoPro",
                            ),
                            rx.el.a(
                                rx.icon(
                                    tag="instagram",
                                    class_name="h-6 w-6 text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                                ),
                                href="https://instagram.com/boteco.pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Instagram BotecoPro",
                            ),
                            rx.el.a(
                                rx.icon(
                                    tag="twitter",
                                    class_name="h-6 w-6 text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                                ),
                                href="https://x.com/boteco_pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Twitter BotecoPro",
                            ),
                            class_name="flex mt-4 space-x-4",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
                ),
                class_name="grid md:grid-cols-2 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2025 BotecoPro — Desenvolvido e distribuído com tecnologia Monynha Softwares",
                    class_name="text-sm text-[#8C1D2C] opacity-80",
                ),
                rx.el.p(
                    "Powered by Monynha Softwares — https://monynha.com",
                    class_name="text-xs text-[#AA3140] mt-1",
                ),
                class_name="mt-12 pt-8 border-t border-[#8C1D2C]/10 text-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-[#FFF7E8]",
    )