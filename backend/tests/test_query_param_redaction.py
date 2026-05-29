from starlette.datastructures import QueryParams

from src.main import REDACTED_VALUE, redact_query_params


def test_redact_query_params_masks_sensitive_values():
    params = QueryParams(
        "token=abc123&signature=sig-value&secret=sauce&password=pw&page=2"
    )

    redacted = redact_query_params(params)

    assert redacted["token"] == REDACTED_VALUE
    assert redacted["signature"] == REDACTED_VALUE
    assert redacted["secret"] == REDACTED_VALUE
    assert redacted["password"] == REDACTED_VALUE
    assert redacted["page"] == "2"


def test_redact_query_params_preserves_repeated_non_sensitive_values():
    params = QueryParams("status=active&status=pending&token=abc123")

    redacted = redact_query_params(params)

    assert redacted["status"] == ["active", "pending"]
    assert redacted["token"] == REDACTED_VALUE
