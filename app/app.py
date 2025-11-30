import json
import os

import reflex as rx
import reflex_clerk_api as clerk
from app.pages.index import index
from app.pages.pricing import pricing
from app.pages.about import about
from app.pages.solutions import solutions
from app.pages.contact import contact
from app.pages.onboarding.personal import personal_step
from app.pages.onboarding.business import business_step
from app.pages.onboarding.plan import plan_step
from app.pages.onboarding.payment import payment_step
from app.pages.onboarding.success import success_page
from app.pages.dashboard import dashboard
from app.api.provision import api_app
from app.pages.auth.signup import signup_page
from app.pages.auth.signin import signin_page

base_app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.title(
            "BotecoPro | Plataforma global de gestão para bares e restaurantes"
        ),
        rx.el.meta(
            name="description",
            content="BotecoPro — plataforma de gestão para bares e restaurantes desenvolvida pela Monynha Softwares. Operações multi-tenant, multi-região e suporte inclusivo para equipes modernas.",
        ),
        rx.el.meta(name="og:title", content="BotecoPro"),
        rx.el.meta(
            name="og:description",
            content="BotecoPro une tecnologia intuitiva, acessível e global da Monynha Softwares para impulsionar bares e restaurantes.",
        ),
        rx.el.meta(name="og:image", content="/placeholder.svg"),
        rx.el.meta(name="og:url", content="https://monynha.com"),
        rx.el.meta(name="og:site_name", content="BotecoPro"),
        rx.el.meta(name="twitter:card", content="summary_large_image"),
        rx.el.meta(name="twitter:title", content="BotecoPro by Monynha Softwares"),
        rx.el.meta(
            name="twitter:description",
            content="Powered by Monynha Softwares — BotecoPro é a plataforma de gestão inclusiva para bares e restaurantes.",
        ),
        rx.el.meta(name="twitter:image", content="/placeholder.svg"),
        rx.el.link(
            rel="canonical",
            href="https://monynha.com",
        ),
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.script(
            type_="application/ld+json",
            children=json.dumps(
                {
                    "@context": "https://schema.org",
                    "@type": "Organization",
                    "name": "BotecoPro",
                    "url": "https://monynha.com",
                    "brand": "Monynha Softwares",
                    "sameAs": ["https://monynha.com"],
                    "description": "BotecoPro — plataforma de gestão para bares e restaurantes desenvolvida pela Monynha Softwares.",
                }
            ),
        ),
        rx.script(
            """
            (() => {
                const scrollToTop = () => {
                    window.scrollTo({ top: 0, behavior: "smooth" });
                };

                const dispatchScroll = () => window.dispatchEvent(new Event("locationchange"));

                const patchHistoryMethod = (methodName) => {
                    const original = history[methodName];
                    history[methodName] = function (...args) {
                        const result = original.apply(this, args);
                        dispatchScroll();
                        return result;
                    };
                };

                patchHistoryMethod("pushState");
                patchHistoryMethod("replaceState");

                window.addEventListener("popstate", dispatchScroll);
                window.addEventListener("locationchange", scrollToTop);

                // Initial load
                scrollToTop();
            })();
            """
        ),
    ],
)
app = clerk.wrap_app(
    base_app,
    publishable_key=os.getenv("CLERK_PUBLISHABLE_KEY"),
    secret_key=os.getenv("CLERK_SECRET_KEY"),
    register_user_state=True,
    # The project originally enabled Clerk-hosted sign-in/sign-up pages here.
    # We are moving to a custom sign-up/sign-in flow for onboarding.
    # add_clerk_pages=True,
)
app.api = api_app
app.add_page(index, route="/")
app.add_page(pricing, route="/pricing")
app.add_page(about, route="/about")
app.add_page(solutions, route="/solutions")
app.add_page(contact, route="/contact")
app.add_page(personal_step, route="/onboarding/step-1-personal")
# app.add_page(personal_step, route="/onboarding/step-1-personal", on_load=clerk.protect)
app.add_page(business_step, route="/onboarding/step-2-business")
# app.add_page(business_step, route="/onboarding/step-2-business", on_load=clerk.protect)
app.add_page(plan_step, route="/onboarding/step-3-plan")
# app.add_page(plan_step, route="/onboarding/step-3-plan", on_load=clerk.protect)
app.add_page(payment_step, route="/onboarding/step-4-payment")
# app.add_page(payment_step, route="/onboarding/step-4-payment", on_load=clerk.protect)
app.add_page(success_page, route="/onboarding/success")
# app.add_page(success_page, route="/onboarding/success", on_load=clerk.protect)
app.add_page(dashboard, route="/app", on_load=clerk.protect)
app.add_page(signup_page, route="/signup")
app.add_page(signin_page, route="/signin")