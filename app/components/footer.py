import reflex as rx


def footer() -> rx.Component:
    """A shared footer component for the public pages."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Boteco.pt", class_name="text-2xl font-bold text-[#8B1E3F]"
                    ),
                    rx.el.p(
                        "Tecnologia inteligente para bares independentes.",
                        class_name="mt-2 text-sm text-[#4F3222] opacity-80",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "Navegação", class_name="font-semibold text-[#4F3222]"
                        ),
                        rx.el.a(
                            "Início",
                            href="/",
                            class_name="mt-4 block text-[#4F3222] hover:text-[#B3701A] transition-colors",
                        ),
                        rx.el.a(
                            "Planos",
                            href="/pricing",
                            class_name="mt-2 block text-[#4F3222] hover:text-[#B3701A] transition-colors",
                        ),
                        rx.el.a(
                            "Sobre",
                            href="/about",
                            class_name="mt-2 block text-[#4F3222] hover:text-[#B3701A] transition-colors",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4("Legal", class_name="font-semibold text-[#4F3222]"),
                        rx.el.a(
                            "Termos de Serviço",
                            href="#",
                            class_name="mt-4 block text-[#4F3222] hover:text-[#B3701A] transition-colors",
                        ),
                        rx.el.a(
                            "Política de Privacidade",
                            href="#",
                            class_name="mt-2 block text-[#4F3222] hover:text-[#B3701A] transition-colors",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4("Contato", class_name="font-semibold text-[#4F3222]"),
                        rx.el.p("contato@boteco.pt", class_name="mt-4 text-[#4F3222]"),
                        rx.el.div(
                            rx.el.a(
                                rx.icon(
                                    tag="facebook",
                                    class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                                ),
                                href="https://facebook.com/boteco.pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Facebook Boteco.pt",
                            ),
                            rx.el.a(
                                rx.icon(
                                    tag="instagram",
                                    class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                                ),
                                href="https://instagram.com/boteco.pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Instagram Boteco.pt",
                            ),
                            rx.el.a(
                                rx.icon(
                                    tag="twitter",
                                    class_name="h-6 w-6 text-[#4F3222] hover:text-[#8B1E3F] transition-colors",
                                ),
                                href="https://x.com/boteco_pt",
                                target="_blank",
                                rel="noreferrer",
                                aria_label="Twitter Boteco.pt",
                            ),
                            class_name="flex mt-4 space-x-4",
                        ),
                    ),
                    class_name="grid grid-cols-2 md:grid-cols-3 gap-8",
                ),
                class_name="grid md:grid-cols-2 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    f"© {2024} Boteco.pt. Todos os direitos reservados.",
                    class_name="text-sm text-[#4F3222] opacity-70",
                ),
                class_name="mt-12 pt-8 border-t border-[#4F3222]/10 text-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-[#F1DDAD]/50",
    )