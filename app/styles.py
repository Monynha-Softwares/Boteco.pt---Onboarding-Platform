"""Shared styling helpers and global CSS utilities."""

from __future__ import annotations

import reflex as rx

from app.theme import Colors, Fonts, Radii, Space


def globals() -> list[rx.Component]:
    """Return the shared head components for fonts and global styles."""

    font_link = (
        "https://fonts.googleapis.com/css2?"
        "family=Inter:wght@400;500;600;700;800;900&"
        "family=Space+Grotesk:wght@400;500;600;700&display=swap"
    )

    return [
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(href=font_link, rel="stylesheet"),
        rx.el.style(
            f"""
            :root {{
                --font-body: {Fonts.body};
                --font-display: {Fonts.display};
                --color-primary: {Colors.primary};
                --color-secondary: {Colors.secondary};
                --color-tertiary: {Colors.tertiary};
                --color-surface: {Colors.surface};
                --color-muted: {Colors.muted};
                --space-xs: {Space.xs};
                --space-sm: {Space.sm};
                --space-md: {Space.md};
                --space-lg: {Space.lg};
                --space-xl: {Space.xl};
                --space-xxl: {Space.xxl};
                --space-section: {Space.section};
                --radius-sm: {Radii.sm};
                --radius-md: {Radii.md};
                --radius-lg: {Radii.lg};
                --radius-pill: {Radii.pill};
            }}

            * {{
                box-sizing: border-box;
            }}

            body {{
                font-family: var(--font-body);
                background-color: {Colors.background};
                color: {Colors.secondary};
                margin: 0;
                min-height: 100vh;
            }}

            h1, h2, h3, h4, h5, h6 {{
                font-family: var(--font-display);
                color: var(--color-primary);
                letter-spacing: -0.02em;
            }}

            button, [role="button"], .rx-button {{
                font-family: var(--font-display);
            }}

            p {{
                line-height: 1.6;
            }}
            """
        ),
    ]


def section_container(*children: rx.Component, **props) -> rx.Component:
    """Wrapper that centers the content and applies responsive padding."""

    defaults = dict(
        width="100%",
        max_width="1200px",
        margin_x="auto",
        padding_x=Space.xl,
        padding_y=Space.xl,
    )
    style = {**defaults, **props}
    return rx.box(*children, **style)


def surface(*children: rx.Component, **props) -> rx.Component:
    """Card-like surface helper with shared padding and elevation."""

    defaults = dict(
        background_color=Colors.surface,
        border_radius=Radii.lg,
        padding=Space.lg,
        box_shadow="0 20px 45px rgba(16, 24, 40, 0.08)",
    )
    style = {**defaults, **props}
    return rx.box(*children, **style)


def stack_gap(size: str = "md") -> dict[str, str]:
    """Utility helper returning a consistent gap value for stacks."""

    size_map = {
        "xs": Space.xs,
        "sm": Space.sm,
        "md": Space.md,
        "lg": Space.lg,
        "xl": Space.xl,
        "xxl": Space.xxl,
    }
    return {"gap": size_map.get(size, Space.md)}


__all__ = [
    "globals",
    "section_container",
    "stack_gap",
    "surface",
]
