import reflex as rx
from app.states.auth_state import AuthState


def signin_page() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "BotecoPro",
                    href="/",
                    class_name="text-2xl font-bold text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                ),
                class_name="py-8 px-4 sm:px-6 lg:px-8 bg-[#FFF7E8] border-b border-gray-200",
            ),
            rx.el.div(
                rx.el.h2("Entrar", class_name="text-2xl font-bold text-[#8C1D2C]"),
                rx.el.p(
                    "Informe o email usado na sua conta.",
                    class_name="mt-2 text-sm text-[#8C1D2C]/80",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label("Email", class_name="block text-sm font-medium text-[#8C1D2C]"),
                        rx.el.input(
                            placeholder="seu@email.com",
                            name="email",
                            type="email",
                            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                        ),
                        class_name="mt-4",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Entrar",
                            type="submit",
                            class_name="inline-flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140]",
                        ),
                        class_name="flex justify-end mt-8",
                    ),
                    on_submit=AuthState.signin,
                ),
                class_name="max-w-2xl mx-auto p-8 bg-white rounded-xl shadow-md border border-gray-200/80",
            ),
            class_name="pb-16",
        ),
        class_name="min-h-screen bg-[#FFF7E8]/30 font-['Inter']",
    )
