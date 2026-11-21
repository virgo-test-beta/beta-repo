from datetime import datetime

audit_log: list[dict[str, object]] = []


def check_login(users: dict[str, str], username: str, password: str) -> bool:
    is_successful = users.get(username) == password
    audit_log.append({"username": username, "time": datetime.now(), "is_successful": is_successful})
    return is_successful
