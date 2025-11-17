import reflex as rx
from app.components.header import header
from app.components.footer import footer


SECTIONS = [
    {
        "title": "Coleta de Dados",
        "items": [
            "Informações de conta e contato fornecidas diretamente por você.",
            "Registros de uso das soluções para monitorar desempenho.",
            "Dados enviados via integrações com PDV, delivery e estoque.",
        ],
    },
    {
        "title": "Uso dos Dados",
        "items": [
            "Prover os serviços contratados e personalizar recomendações.",
            "Emitir comunicações transacionais, notas fiscais e alertas.",
            "Manter segurança, auditoria e conformidade com a LGPD.",
        ],
    },
    {
        "title": "Seus Direitos",
        "items": [
            "Solicitar acesso, portabilidade ou exclusão dos dados.",
            "Revogar consentimentos de comunicação a qualquer momento.",
            "Reportar incidentes diretamente ao nosso DPO (privacidade@barnostri.com).",
        ],
    },
]


def legal_list(items: list[str]) -> rx.Component:
    return rx.el.ul(
        *(
            rx.el.li(item, class_name="text-base text-[#4F3222] opacity-80")
            for item in items
        ),
        class_name="mt-4 list-disc list-inside space-y-2",
    )


def privacy() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.span(
                    "Política de Privacidade",
                    class_name="text-sm font-semibold tracking-widest text-[#B3701A] uppercase",
                ),
                rx.el.h1(
                    "Como cuidamos dos seus dados",
                    class_name="mt-4 text-4xl md:text-5xl font-extrabold text-[#4F3222]",
                ),
                rx.el.p(
                    "Transparência total sobre coleta, uso e proteção das informações no ecossistema Barnostri.",
                    class_name="mt-4 text-lg text-[#4F3222] opacity-80",
                ),
                class_name="max-w-4xl mx-auto text-center",
            ),
            class_name="bg-[#F1DDAD]/80 py-20 px-4",
        ),
        rx.el.section(
            rx.el.div(
                *(
                    rx.el.article(
                        rx.el.h2(section["title"], class_name="text-2xl font-bold text-[#8B1E3F]"),
                        legal_list(section["items"]),
                        class_name="p-6 rounded-2xl bg-white shadow-lg border border-[#4F3222]/10",
                    )
                    for section in SECTIONS
                ),
                class_name="grid gap-8",
            ),
            class_name="max-w-4xl mx-auto py-16 px-4",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.h2(
                    "Contato do DPO",
                    class_name="text-3xl font-bold text-white",
                ),
                rx.el.p(
                    "Envie dúvidas ou solicitações para privacidade@barnostri.com e responderemos em até 48h úteis.",
                    class_name="mt-3 text-white/80",
                ),
                class_name="max-w-3xl mx-auto text-center",
            ),
            class_name="bg-[#8B1E3F] py-16 px-4",
        ),
        footer(),
        class_name="bg-[#FFF9F0] font-['Inter']",
    )
