"""Application-wide design tokens and Radix theme configuration."""

from __future__ import annotations

import reflex as rx


class Colors:
    """Brand color palette used across the application."""

    primary: str = "#FF5F13"
    secondary: str = "#101828"
    tertiary: str = "#1D4ED8"
    background: str = "#F8FAFC"
    surface: str = "#FFFFFF"
    muted: str = "#475467"


class Fonts:
    """Typography scale for body and headings."""

    body: str = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    display: str = "'Space Grotesk', 'Inter', -apple-system, 'Segoe UI', sans-serif"


class Radii:
    """Border radius tokens for rounded surfaces."""

    none: str = "0px"
    sm: str = "0.25rem"
    md: str = "0.5rem"
    lg: str = "1rem"
    pill: str = "999px"


class Space:
    """Consistent spacing scale for layout primitives."""

    xs: str = "0.25rem"
    sm: str = "0.5rem"
    md: str = "0.75rem"
    lg: str = "1rem"
    xl: str = "1.5rem"
    xxl: str = "2.5rem"
    section: str = "4rem"


tokens = rx.theme(
    appearance="light",
    has_background=True,
    accent_color="amber",
    gray_color="sand",
    panel_background="translucent",
    radius="large",
    scaling="100%",
)

__all__ = [
    "Colors",
    "Fonts",
    "Radii",
    "Space",
    "tokens",
]
