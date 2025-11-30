import reflex as rx
import reflex as rx

from app.components.header import header
from app.components.footer import footer


def contact_card(title: str, description: str, action: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.h3(title, class_name="text-xl font-semibold text-[#8C1D2C]"),
        rx.el.p(description, class_name="mt-2 text-sm text-[#8C1D2C] opacity-80"),
        action,
        class_name="p-6 rounded-xl border border-[#FFF7E8]/70 bg-white shadow-sm",
    )


def contact() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Vamos conversar",
                    class_name="text-4xl md:text-5xl font-extrabold text-center text-[#8C1D2C]",
                ),
                rx.el.p(
                    "Conte para o BotecoPro, powered by Monynha Softwares, os desafios do seu negócio e receba um plano personalizado em até 24 horas úteis.",
                    class_name="mt-4 max-w-3xl mx-auto text-lg text-center text-[#8C1D2C] opacity-80",
                ),
                rx.el.p(
                    "Brasil, Portugal e Suíça contam com suporte multilíngue, acessível e alinhado às normas locais.",
                    class_name="mt-2 max-w-2xl mx-auto text-sm text-center text-[#AA3140]",
                ),
                class_name="max-w-4xl mx-auto",
            ),
            class_name="bg-[#FFF7E8] py-16 px-4 sm:px-6 lg:px-8",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    contact_card(
                        "Atendimento comercial",
                        "Horário: segunda a sexta, 9h às 19h (horário de Brasília).",
                        rx.el.a(
                            "contact@boteco.pt",
                            href="mailto:contact@boteco.pt",
                            class_name="mt-4 inline-flex text-[#8C1D2C] font-semibold hover:text-[#AA3140]",
                        ),
                    ),
                    contact_card(
                        "Suporte prioritário",
                        "Clientes ativos contam com plantão via WhatsApp e canais multilíngues em dias de grande movimento.",
                        rx.el.a(
                            "Abrir chamado",
                            href="https://painel.boteco.pt/support",
                            target="_blank",
                            rel="noreferrer",
                            class_name="mt-4 inline-flex text-[#8C1D2C] font-semibold hover:text-[#AA3140]",
                        ),
                    ),
                    contact_card(
                        "Visitas presenciais",
                        "Disponíveis nas capitais brasileiras, em Portugal e na Suíça mediante agendamento com o time estratégico.",
                        rx.el.p(
                            "Envie datas sugeridas no e-mail e retornaremos com a confirmação.",
                            class_name="mt-4 text-sm text-[#8C1D2C]",
                        ),
                    ),
                    class_name="grid gap-6 md:grid-cols-3",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Formulário rápido",
                        class_name="text-2xl font-bold text-[#8C1D2C]",
                    ),
                    rx.el.p(
                        "Preferimos conversar com pessoas reais, mas este formulário agiliza o contato inicial.",
                        class_name="mt-2 text-sm text-[#8C1D2C] opacity-80",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Nome completo",
                                class_name="block text-sm font-medium text-[#8C1D2C]",
                            ),
                            rx.el.input(
                                placeholder="Seu nome",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Email",
                                class_name="block text-sm font-medium text-[#8C1D2C]",
                            ),
                            rx.el.input(
                                type="email",
                                placeholder="voce@boteco.com",
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Mensagem",
                                class_name="block text-sm font-medium text-[#8C1D2C]",
                            ),
                            rx.el.textarea(
                                placeholder="Conte o que está buscando em detalhes",
                                rows=4,
                                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm",
                            ),
                        ),
                        rx.el.button(
                            "Enviar mensagem",
                            type="submit",
                            class_name="mt-4 inline-flex justify-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-[#8C1D2C] hover:bg-[#AA3140]",
                        ),
                        class_name="space-y-4 mt-6",
                    ),
                    class_name="mt-12 p-8 bg-white rounded-2xl shadow-xl border border-[#FFF7E8]/80",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="py-16 px-4 sm:px-6 lg:px-8 bg-white",
        ),
        footer(),
        class_name="bg-white font-['Inter']",
    )
