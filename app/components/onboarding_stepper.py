import reflex as rx


import reflex as rx


def step_item(step_number: int, label: str, current_step: rx.Var[int]) -> rx.Component:
    """A single step in the progress stepper."""
    is_completed = step_number < current_step
    is_current = step_number == current_step
    return rx.el.li(
        rx.el.div(
            rx.cond(
                is_completed,
                rx.el.div(
                    rx.icon("check", class_name="h-5 w-5 text-white"),
                    class_name="w-8 h-8 rounded-full bg-[#8C1D2C] flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.span(
                        f"{step_number}",
                        class_name=rx.cond(
                            is_current, "text-[#8C1D2C]", "text-[#8C1D2C]/50"
                        ),
                    ),
                    class_name=rx.cond(
                        is_current,
                        "w-8 h-8 rounded-full border-2 border-[#AA3140] flex items-center justify-center",
                        "w-8 h-8 rounded-full border-2 border-[#8C1D2C]/30 flex items-center justify-center",
                    ),
                ),
            ),
            rx.el.p(
                label,
                class_name=rx.cond(
                    is_current,
                    "text-[#AA3140] font-semibold text-sm mt-2",
                    "text-[#8C1D2C]/80 text-sm mt-2",
                ),
            ),
            class_name="flex flex-col items-center",
        ),
        class_name="flex-1",
    )


def onboarding_stepper(current_step: rx.Var[int]) -> rx.Component:
    """The stepper component for the onboarding flow."""
    steps = [
        (1, "Dados Pessoais"),
        (2, "Dados do Negócio"),
        (3, "Plano"),
        (4, "Pagamento"),
    ]
    return rx.el.div(
        rx.el.ul(
            rx.el.div(
                rx.foreach(
                    steps, lambda step: step_item(step[0], step[1], current_step)
                ),
                class_name="relative flex items-start justify-between w-full",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="absolute top-4 left-0 w-full h-0.5 bg-[#8C1D2C]/20 -z-10"
                ),
                rx.el.div(
                    class_name="absolute top-4 left-0 h-0.5 bg-[#AA3140] -z-10",
                    width=((current_step - 1) / (len(steps) - 1) * 100).to_string()
                    + "%",
                ),
            ),
            class_name="relative",
        ),
        class_name="w-full max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
    )