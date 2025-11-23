import re


def validate_username(username: str) -> bool:
    """Validates if the username contains only alphanumeric characters and underscores."""
    if not username:
        return False
    pattern = "^[a-zA-Z0-9_]{3,30}$"
    return bool(re.match(pattern, username))


def validate_cpf_cnpj(tax_number: str) -> bool:
    """Validates the format of CPF (11 digits) or CNPJ (14 digits)."""
    if not tax_number:
        return False
    clean_number = re.sub("\\D", "", tax_number)
    return len(clean_number) in [11, 14]


def validate_postal_code(postal_code: str) -> bool:
    """Validates Brazilian postal code format (8 digits)."""
    if not postal_code:
        return False
    clean_cep = re.sub("\\D", "", postal_code)
    return len(clean_cep) == 8