import pytest
from pydantic import ValidationError

from src.config import DEFAULT_WEBHOOK_SECRET_KEY, Settings


def test_production_rejects_default_webhook_secret():
    with pytest.raises(ValidationError) as exc:
        Settings(environment="production", webhook_secret_key=DEFAULT_WEBHOOK_SECRET_KEY)

    message = str(exc.value)
    assert "webhook_secret_key must be configured for production" in message
    assert DEFAULT_WEBHOOK_SECRET_KEY not in message


def test_development_allows_default_webhook_secret():
    settings = Settings(environment="development", webhook_secret_key=DEFAULT_WEBHOOK_SECRET_KEY)

    assert settings.webhook_secret_key == DEFAULT_WEBHOOK_SECRET_KEY


def test_production_accepts_custom_webhook_secret():
    settings = Settings(environment="production", webhook_secret_key="custom-webhook-secret")

    assert settings.webhook_secret_key == "custom-webhook-secret"
