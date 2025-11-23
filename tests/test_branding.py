from __future__ import annotations
from pathlib import Path


def test_branding_name_updated():
    app_dir = Path("app")
    banned_term = "Barnostri"
    files_with_term: list[Path] = []
    for file_path in app_dir.rglob("*.py"):
        if banned_term in file_path.read_text(encoding="utf-8"):
            files_with_term.append(file_path)
    assert not files_with_term, (
        f"Brand term '{banned_term}' ainda presente em: {files_with_term}"
    )