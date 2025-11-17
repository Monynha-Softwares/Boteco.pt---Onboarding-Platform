import reflex as rx
from app.components.header import header
from app.components.footer import footer


CLAUSES = [
    {
        "title": "1. Aceite",
        "body": "Ao utilizar a plataforma Barnostri você concorda com estes termos e com a Política de Privacidade vigente.",
    },
    {
        "title": "2. Serviços",
        "body": "Disponibilizamos módulos de menu digital, fornecedores e integrações conforme plano contratado em reais.",
    },
    {
        "title": "3. Obrigações do Cliente",
        "body": "Fornecer informações verídicas, manter credenciais seguras e utilizar o sistema conforme a legislação aplicável.",
    },
    {
        "title": "4. Pagamentos",
        "body": "As assinaturas são mensais, com renovação automática e possibilidade de cancelamento com aviso de 30 dias.",
    },
    {
        "title": "5. Suporte",
        "body": "Canais oficiais: email, portal do cliente e Whatsapp corporativo dentro dos prazos definidos por plano.",
    },
    {
        "title": "6. Limitação de Responsabilidade",
        "body": "Não respondemos por indisponibilidade causada por terceiros, manutenção programada ou uso inadequado do produto.",
    },
]


def clause_block(clause: dict[str, str]) -> rx.Component:
    return rx.el.article(
        rx.el.h2(clause["title"], class_name="text-2xl font-bold text-[#8B1E3F]"),
        rx.el.p(
            clause["body"],
            class_name="mt-2 text-base text-[#4F3222] opacity-80",
        ),
        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
    )


def terms() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.span(
                    "Termos de Serviço",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(
                    "Condições de uso da plataforma",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Leia atentamente antes de contratar ou utilizar qualquer solução Barnostri.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(clause_block(clause) for clause in CLAUSES),
                class_name="grid gap-8",
            ),
            class_name="max-w-4xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.p(
                    "Em caso de dúvidas sobre estes termos, entre em contato pelo email juridico@barnostri.com.",
                    class_name="text-base text-white/90",
                ),
                class_name="max-w-3xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
