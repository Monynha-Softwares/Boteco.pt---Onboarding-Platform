import reflex as rx
from app.components.header import header
from app.components.footer import footer


def not_found_page() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.span("Erro 404", class_name="text-sm font-semibold text-[#B3701A] uppercase"),
                rx.el.h1(
                    "Página não encontrada",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "O link acessado não existe ou foi movido. Continue navegando pelos nossos conteúdos.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                rx.el.div(
                    rx.el.a(
                        "Voltar ao início",
                        href="/",
                        class_name="inline-flex items-center justify-center px-6 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold",
                    ),
                    rx.el.a(
                        "Explorar soluções",
                        href="/solutions",
                        class_name="mt-4 inline-flex items-center justify-center px-6 py-3 rounded-lg border border-[#8B1E3F] text-[#8B1E3F] font-semibold",
                    ),
                    class_name="mt-8 flex flex-col md:flex-row md:space-x-4",
                ),
                class_name="max-w-3xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-24 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] min-h-screen font-['Inter']",
    )
