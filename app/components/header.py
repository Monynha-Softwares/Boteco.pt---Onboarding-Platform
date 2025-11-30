import reflex as rx
import reflex_clerk_api as clerk

from app.states.base_state import BaseState


PRIMARY = "#8C1D2C"
SECONDARY = "#AA3140"
BACKGROUND = "#FFF7E8"


def nav_link(
    text: str, href: str, on_click: rx.event.EventHandler = None
) -> rx.Component:
    """A navigation link component."""
    return rx.el.a(
        text,
        href=href,
        on_click=on_click,
        class_name="text-base font-medium text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
    )


def header() -> rx.Component:
    """A shared header component with responsive navigation and Clerk auth."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        "BotecoPro",
                        href="/",
                        class_name="text-2xl font-bold text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                    ),
                    rx.el.span(
                        "Powered by Monynha Softwares",
                        class_name="text-xs font-semibold text-[#AA3140]",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    nav_link("Início", "/"),
                    nav_link("Planos", "/pricing"),
                    nav_link("Sobre", "/about"),
                    nav_link("Soluções", "/solutions"),
                    nav_link("Contato", "/contact"),
                    class_name="hidden md:flex items-center space-x-8",
                ),
                class_name="flex items-center space-x-8",
            ),
            rx.el.div(
                clerk.signed_in(
                    rx.el.div(
                        rx.el.a(
                            "Dashboard",
                            href="/app",
                            class_name="text-base font-medium text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        clerk.user_button(after_sign_out_url="/"),
                        class_name="items-center space-x-4",
                    )
                ),
                clerk.signed_out(
                    rx.el.div(
                        rx.el.a(
                            "Entrar",
                            href="/signin",
                            class_name="text-base font-medium text-[#8C1D2C] hover:text-[#AA3140] transition-colors",
                        ),
                        rx.el.a(
                            "Criar Conta",
                            href="/signup",
                            class_name="ml-4 inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-lg shadow-sm text-base font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140] transition-colors",
                        ),
                        class_name="items-center",
                    )
                ),
                class_name="hidden md:flex items-center",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(tag="menu", class_name="h-6 w-6"),
                    on_click=BaseState.toggle_mobile_menu,
                    class_name="md:hidden inline-flex items-center justify-center p-2 rounded-md text-[#8C1D2C] hover:text-[#AA3140] hover:bg-[#FFF7E8] focus:outline-none focus:ring-2 focus:ring-inset focus:ring-[#AA3140]",
                ),
                class_name="flex md:hidden",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-20",
        ),
        rx.cond(
            BaseState.show_mobile_menu,
            rx.el.div(
                rx.el.div(
                    nav_link("Início", "/", on_click=BaseState.toggle_mobile_menu),
                    nav_link("Planos", "/pricing", on_click=BaseState.toggle_mobile_menu),
                    nav_link("Sobre", "/about", on_click=BaseState.toggle_mobile_menu),
                    nav_link("Soluções", "/solutions", on_click=BaseState.toggle_mobile_menu),
                    nav_link("Contato", "/contact", on_click=BaseState.toggle_mobile_menu),
                    class_name="px-2 pt-2 pb-3 space-y-1",
                ),
                rx.el.div(
                    clerk.signed_in(
                        rx.el.a(
                            "Dashboard",
                            href="/app",
                            class_name="block px-3 py-2 rounded-md text-base font-medium text-[#8C1D2C] hover:text-[#AA3140] hover:bg-[#FFF7E8]",
                        )
                    ),
                    clerk.signed_out(
                        rx.el.div(
                            rx.el.a(
                                "Entrar",
                                href="/signin",
                                class_name="block px-3 py-2 rounded-md text-base font-medium text-[#8C1D2C] hover:text-[#AA3140] hover:bg-[#FFF7E8]",
                            ),
                            rx.el.a(
                                "Criar Conta",
                                href="/signup",
                                class_name="mt-1 block w-full text-left px-3 py-2 rounded-md text-base font-medium text-white bg-[#8C1D2C] hover:bg-[#AA3140]",
                            ),
                        )
                    ),
                    class_name="pt-4 pb-3 border-t border-gray-200",
                ),
                class_name="md:hidden bg-white shadow-lg rounded-b-lg",
            ),
        ),
        class_name="sticky top-0 z-50 w-full bg-[#FFF7E8]/85 backdrop-blur-md",
    )
