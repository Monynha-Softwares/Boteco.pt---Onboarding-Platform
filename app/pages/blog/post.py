import reflex as rx
from app.components.header import header
from app.components.footer import footer


def format_slug(slug: str | None) -> str:
    if not slug:
        return "Artigo do Blog"
    words = slug.replace("-", " ").split()
    return " ".join(word.capitalize() for word in words)


def paragraph(text: str) -> rx.Component:
    return rx.el.p(text, class_name="mt-4 text-lg text-[#4F3222] opacity-80")


def blog_post(slug: str | None = None) -> rx.Component:
    title = format_slug(slug)
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.span(
                    "Blog Barnostri",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(title, class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]"),
                rx.el.p(
                    "Publicado em tempo real diretamente da nossa equipe editorial. Este é um stub pronto para receber conteúdo CMS.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.article(
                paragraph(
                    "Utilize este template para inserir parágrafos, imagens e citações do seu CMS favorito mantendo o padrão visual Barnostri.",
                ),
                paragraph(
                    "A rota suporta URLs em inglês no formato /blog/[slug] e renderiza automaticamente o título com copy em pt-BR.",
                ),
                paragraph(
                    "Adicione listas, tabelas e métricas conforme necessário. A estrutura abaixo serve como guia inicial para futuros autores.",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Estrutura sugerida",
                        class_name="text-2xl font-bold text-[#8B1E3F] mt-10",
                    ),
                    rx.el.ul(
                        rx.el.li("Introdução contextual", class_name="text-[#4F3222]"),
                        rx.el.li("Passo a passo com dados", class_name="mt-2 text-[#4F3222]"),
                        rx.el.li("Checklist acionável", class_name="mt-2 text-[#4F3222]"),
                        class_name="mt-4 list-disc list-inside space-y-1",
                    ),
                    class_name="mt-6",
                ),
                class_name="max-w-3xl mx-auto",
            ),
            class_name="bg-white py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Precisa de ajuda para aplicar este conteúdo?",
                    class_name="text-3xl font-bold text-white",
                ),
                rx.el.p(
                    "Converse com nosso time de sucesso do cliente e descubra como ativar as funcionalidades citadas no artigo.",
                    class_name="mt-3 text-white/80",
                ),
                rx.el.a(
                    "Falar com especialistas",
                    href="/contact",
                    class_name="mt-6 inline-flex items-center justify-center px-6 py-3 rounded-lg bg-white text-[#8B1E3F] font-semibold",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
