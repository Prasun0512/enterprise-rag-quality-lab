from rag_quality_lab.redaction import redact_pii


def test_redact_pii_masks_email_and_phone() -> None:
    text = "Contact prasun@example.com or +91 8793147065 for details."
    redacted = redact_pii(text)

    assert "prasun@example.com" not in redacted
    assert "8793147065" not in redacted
    assert "[EMAIL]" in redacted
    assert "[PHONE]" in redacted
