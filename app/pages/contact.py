import reflex as rx
from app.components.header import header
from app.components.footer import footer


CONTACT_CARDS = [
    {
        "title": "Suporte Comercial",
        "description": "Segunda a sexta, 9h às 19h",
        "icon": "message-circle",
        "link": "mailto:parcerias@barnostri.com",
    },
    {
        "title": "Sucesso do Cliente",
        "description": "Clientes ativos com SLA prioritário",
        "icon": "headphones",
        "link": "mailto:sucesso@barnostri.com",
    },
    {
        "title": "Whatsapp",
        "description": "+55 11 99999-0000",
        "icon": "phone",
        "link": "https://wa.me/5511999990000",
    },
]

FAQ = [
    {
        "question": "Preciso já ser cliente para falar com vocês?",
        "answer": "Não. Temos especialistas para tirar dúvidas de quem está avaliando a plataforma e para quem já utiliza.",
    },
    {
        "question": "Quanto tempo leva para receber um retorno?",
        "answer": "Respondemos em até 1 dia útil e priorizamos contatos com operações em andamento.",
    },
]


def contact_card(card: dict[str, str]) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=card["icon"], class_name="h-8 w-8 text-[#8B1E3F]"),
        rx.el.h3(card["title"], class_name="mt-4 text-xl font-semibold text-[#4F3222]"),
        rx.el.p(card["description"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#B3701A]",
        href=card["link"],
    )


def faq_block(item: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.h4(item["question"], class_name="text-lg font-semibold text-[#4F3222]"),
        rx.el.p(item["answer"], class_name="mt-2 text-base text-[#4F3222] opacity-80"),
        class_name="p-6 rounded-2xl bg-white border border-[#4F3222]/10",
    )


def contact() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.span(
                    "Fale com a Barnostri",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(
                    "Estamos prontos para ouvir seus desafios",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Escolha o canal preferido ou envie uma mensagem pelo formulário abaixo. Respondemos em pt-BR e mantemos a conversa registrada no painel.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(contact_card(card) for card in CONTACT_CARDS),
                class_name="grid gap-8 md:grid-cols-3",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Envie uma mensagem",
                        class_name="text-3xl font-bold text-[#8B1E3F]",
                    ),
                    rx.el.p(
                        "Compartilhe detalhes do seu projeto e retornaremos com um plano em até 1 dia útil.",
                        class_name="mt-2 text-base text-[#4F3222] opacity-80",
                    ),
                ),
                rx.el.form(
                    rx.el.label(
                        "Nome",
                        class_name="text-sm font-medium text-[#4F3222]",
                        html_for="name",
                    ),
                    rx.el.input(
                        id="name",
                        name="name",
                        required=True,
                        placeholder="Nome completo",
                        class_name="mt-1 w-full rounded-lg border border-[#4F3222]/20 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#B3701A]",
                    ),
                    rx.el.label(
                        "Email",
                        class_name="mt-4 text-sm font-medium text-[#4F3222]",
                        html_for="email",
                    ),
                    rx.el.input(
                        id="email",
                        name="email",
                        type="email",
                        required=True,
                        placeholder="seuemail@empresa.com",
                        class_name="mt-1 w-full rounded-lg border border-[#4F3222]/20 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#B3701A]",
                    ),
                    rx.el.label(
                        "Mensagem",
                        class_name="mt-4 text-sm font-medium text-[#4F3222]",
                        html_for="message",
                    ),
                    rx.el.textarea(
                        id="message",
                        name="message",
                        rows=5,
                        placeholder="Conte um pouco sobre o momento do seu boteco...",
                        class_name="mt-1 w-full rounded-lg border border-[#4F3222]/20 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#B3701A]",
                    ),
                    rx.el.button(
                        "Enviar contato",
                        type="submit",
                        class_name="mt-6 inline-flex items-center justify-center px-6 py-3 rounded-lg bg-[#8B1E3F] text-white font-semibold",
                    ),
                    class_name="mt-6 grid",
                ),
                class_name="grid gap-12 md:grid-cols-2",
            ),
            class_name="bg-white py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(faq_block(item) for item in FAQ),
                class_name="grid gap-6 md:grid-cols-2",
            ),
            class_name="max-w-6xl mx-auto py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
