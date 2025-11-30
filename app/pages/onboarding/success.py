import reflex as rx


def success_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("party-popper", class_name="h-16 w-16 text-[#B3701A]"),
                    class_name="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-[#F1DDAD]",
                ),
                rx.el.div(
                    rx.el.h1(
                        "Parabéns! Seu boteco está pronto!",
                        class_name="mt-4 text-center text-3xl font-extrabold text-[#8C1D2C]",
                    ),
                    rx.el.p(
                        "Tudo foi configurado com sucesso. Agora você está pronto para gerenciar seu negócio como um profissional.",
                        class_name="mt-2 text-center text-md text-[#8C1D2C]/80",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Ir para o Dashboard",
                            href="/app",
                            class_name="inline-flex items-center justify-center px-6 py-3 mt-8 border border-transparent text-base font-medium rounded-lg text-white bg-[#8C1D2C] hover:bg-[#AA3140] shadow-lg",
                        ),
                        class_name="flex justify-center",
                    ),
                    class_name="mt-4",
                ),
            ),
            class_name="max-w-md mx-auto p-8 bg-white rounded-2xl shadow-xl border border-gray-200/80",
        ),
        class_name="min-h-screen flex items-center justify-center bg-[#FFF7E8]/50 font-['Inter']",
    )