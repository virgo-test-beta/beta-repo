import secrets
from datetime import datetime, timedelta

RESET_TOKEN_LIFETIME = timedelta(minutes=30)


def issue_reset_token(username: str) -> dict[str, object]:
    return {"username": username, "token": secrets.token_urlsafe(32), "issued_at": datetime.now()}


def is_reset_token_valid(reset_token: dict[str, object]) -> bool:
    issued_at = reset_token["issued_at"]
    assert isinstance(issued_at, datetime)
    return datetime.now() - issued_at < RESET_TOKEN_LIFETIME
