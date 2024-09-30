import hashlib
from config import settings


def sign_payload_dict(payload_dict: dict) -> dict:

    COMPANY_TOKEN: str = settings.company.token

    sorted_dict_values = "".join(
        str(value) for _, value in sorted(payload_dict.items())
    )
    signature = hashlib.sha512(
        (sorted_dict_values + COMPANY_TOKEN).encode("utf-8")
    ).hexdigest()

    payload_dict["signature"] = signature

    return payload_dict
