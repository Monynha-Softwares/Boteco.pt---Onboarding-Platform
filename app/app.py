import os

import reflex as rx
import reflex_clerk_api as clerk

from app.api.provision import api_app
from app.pages.about import about
from app.pages.auth.signin import signin_page
from app.pages.auth.signup import signup_page
from app.pages.contact import contact
from app.pages.dashboard import dashboard
from app.pages.index import index
from app.pages.onboarding.business import business_step
from app.pages.onboarding.payment import payment_step
from app.pages.onboarding.personal import personal_step
from app.pages.onboarding.plan import plan_step
from app.pages.onboarding.success import success_page
from app.pages.pricing import pricing
from app.pages.solutions import solutions

base_app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.title("Boteco.pt | Plataforma completa para botecos modernos"),
        rx.el.meta(
            name="description",
            content=(
                "Boteco.pt ajuda bares e botecos brasileiros a profissionalizarem operações com gestão "
                "integrada, marketing e insights financeiros."
            ),
        ),
        rx.el.meta(name="og:title", content="Boteco.pt"),
        rx.el.meta(
            name="og:description",
            content="Transforme o seu boteco com operações inteligentes, marketing integrado e suporte local.",
        ),
        rx.el.meta(name="og:image", content="/placeholder.svg"),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
    ],
)

app = clerk.wrap_app(
    base_app,
    publishable_key=os.getenv("CLERK_PUBLISHABLE_KEY"),
    secret_key=os.getenv("CLERK_SECRET_KEY"),
    register_user_state=True,
    # Custom sign-up/sign-in flow is implemented in app.states.auth_state.
    # Clerk-hosted pages remain disabled in favor of the onboarding experience.
)

app.api = api_app
app.add_page(index, route="/")
app.add_page(pricing, route="/pricing")
app.add_page(about, route="/about")
app.add_page(solutions, route="/solutions")
app.add_page(contact, route="/contact")
app.add_page(personal_step, route="/onboarding/step-1-personal")
app.add_page(business_step, route="/onboarding/step-2-business")
app.add_page(plan_step, route="/onboarding/step-3-plan")
app.add_page(payment_step, route="/onboarding/step-4-payment")
app.add_page(success_page, route="/onboarding/success")
app.add_page(dashboard, route="/app", on_load=clerk.protect)
app.add_page(signup_page, route="/signup")
app.add_page(signin_page, route="/signin")
