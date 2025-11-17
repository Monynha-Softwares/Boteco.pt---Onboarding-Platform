import reflex as rx
import reflex_clerk_api as clerk
import os
from app.pages.index import index
from app.pages.pricing import pricing
from app.pages.about import about
from app.pages.solutions.index import solutions_overview
from app.pages.solutions.digital_menu import digital_menu
from app.pages.solutions.suppliers import suppliers
from app.pages.solutions.integrations import integrations
from app.pages.blog.index import blog_index
from app.pages.blog.post import blog_post
from app.pages.contact import contact
from app.pages.legal.privacy import privacy
from app.pages.legal.terms import terms
from app.pages.not_found import not_found_page
from app.pages.onboarding.personal import personal_step
from app.pages.onboarding.business import business_step
from app.pages.onboarding.plan import plan_step
from app.pages.onboarding.payment import payment_step
from app.pages.onboarding.success import success_page
from app.pages.dashboard import dashboard
from app.api.provision import api_app

base_app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
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
    add_clerk_pages=True,
)
app.api = api_app
app.add_page(index, route="/")
app.add_page(pricing, route="/pricing")
app.add_page(about, route="/about")
app.add_page(solutions_overview, route="/solutions")
app.add_page(digital_menu, route="/solutions/digital-menu")
app.add_page(suppliers, route="/solutions/suppliers")
app.add_page(integrations, route="/solutions/integrations")
app.add_page(blog_index, route="/blog")
app.add_page(blog_post, route="/blog/[slug]")
app.add_page(contact, route="/contact")
app.add_page(privacy, route="/legal/privacy")
app.add_page(terms, route="/legal/terms")
app.add_page(not_found_page, route="/404")
app.add_page(personal_step, route="/onboarding/step-1-personal", on_load=clerk.protect)
app.add_page(business_step, route="/onboarding/step-2-business", on_load=clerk.protect)
app.add_page(plan_step, route="/onboarding/step-3-plan", on_load=clerk.protect)
app.add_page(payment_step, route="/onboarding/step-4-payment", on_load=clerk.protect)
app.add_page(success_page, route="/onboarding/success", on_load=clerk.protect)
app.add_page(dashboard, route="/app", on_load=clerk.protect)
