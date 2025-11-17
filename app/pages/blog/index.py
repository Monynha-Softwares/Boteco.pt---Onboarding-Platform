import reflex as rx
from app.components.header import header
from app.components.footer import footer


POSTS = [
    {
        "title": "Checklist para digitalizar seu cardápio em 7 dias",
        "summary": "Como preparar fotos, descrição e preços para reduzir erros na migração.",
        "slug": "checklist-cardapio-digital",
        "category": "Menu Digital",
    },
    {
        "title": "Guia de negociação com fornecedores locais",
        "summary": "Estratégias para melhorar prazos e garantir produtos frescos sem inflar custos.",
        "slug": "negociacao-fornecedores-boteco",
        "category": "Operações",
    },
    {
        "title": "Integrações essenciais para botecos com delivery",
        "summary": "Como conectar Barnostri aos principais marketplaces e manter estoque atualizado.",
        "slug": "integracoes-delivery-boteco",
        "category": "Tecnologia",
    },
]


CATEGORY_COLORS = {
    "Menu Digital": "bg-[#F1DDAD]/70 text-[#8B1E3F]",
    "Operações": "bg-[#8B1E3F]/10 text-[#8B1E3F]",
    "Tecnologia": "bg-[#B3701A]/10 text-[#B3701A]",
}


def post_card(post: dict[str, str]) -> rx.Component:
    return rx.el.article(
        rx.el.span(
            post["category"],
            class_name=f"text-xs font-semibold px-3 py-1 rounded-full {CATEGORY_COLORS.get(post['category'], 'bg-[#F1DDAD]/70 text-[#4F3222]')}",
        ),
        rx.el.h3(post["title"], class_name="mt-4 text-2xl font-bold text-[#4F3222]"),
        rx.el.p(post["summary"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        rx.el.a(
            "Ler artigo",
            href=f"/blog/{post['slug']}",
            class_name="mt-4 inline-flex items-center text-[#8B1E3F] font-semibold",
        ),
        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
    )


def blog_index() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.p(
                    "Blog Barnostri",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(
                    "Histórias, guias e inspirações para botecos profissionais",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Artigos práticos com foco em operação, experiência do cliente e tecnologia acessível.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(post_card(post) for post in POSTS),
                class_name="grid gap-8 md:grid-cols-3",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Assine a newsletter",
                    class_name="text-3xl font-bold text-[#8B1E3F] text-center",
                ),
                rx.el.form(
                    rx.el.input(
                        placeholder="Seu email profissional",
                        type="email",
                        required=True,
                        class_name="w-full px-4 py-3 rounded-lg border border-[#4F3222]/20 focus:outline-none focus:ring-2 focus:ring-[#B3701A]",
                    ),
                    rx.el.button(
                        "Quero receber conteúdos",
                        type="submit",
                        class_name="mt-4 w-full px-4 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold",
                    ),
                    class_name="mt-6 max-w-xl mx-auto",
                ),
                class_name="max-w-3xl mx-auto",
            ),
            class_name="bg-white py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
