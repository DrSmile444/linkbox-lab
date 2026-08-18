"""Tests for linkbox.service."""

from datetime import datetime, timedelta

from linkbox.service import create_link, resolve_link


def test_create_link_builds_link_with_zero_clicks():
    now = datetime(2026, 1, 1, 12, 0, 0)
    expires_at = now + timedelta(days=7)

    link = create_link(
        target_url="https://example.com/article",
        short_code="abc123",
        now=now,
        expires_at=expires_at,
    )

    assert link.short_code == "abc123"
    assert link.target_url == "https://example.com/article"
    assert link.created_at == now
    assert link.expires_at == expires_at
    assert link.click_count == 0


def test_resolve_link_resolves_when_not_expired():
    created_at = datetime(2026, 1, 1, 12, 0, 0)
    expires_at = created_at + timedelta(days=7)

    link_with_expiry = create_link(
        target_url="https://example.com",
        short_code="abc123",
        now=created_at,
        expires_at=expires_at,
    )
    resolved = resolve_link(link_with_expiry, now=created_at + timedelta(days=1))
    assert resolved is not None
    assert resolved.click_count == 1

    link_never_expires = create_link(
        target_url="https://example.com",
        short_code="xyz789",
        now=created_at,
        expires_at=None,
    )
    resolved_forever = resolve_link(link_never_expires, now=created_at + timedelta(days=365))
    assert resolved_forever is not None
    assert resolved_forever.click_count == 1


def test_resolve_link_well_after_expiry_returns_none():
    created_at = datetime(2026, 1, 1, 12, 0, 0)
    expires_at = created_at + timedelta(days=7)
    link = create_link(
        target_url="https://example.com",
        short_code="abc123",
        now=created_at,
        expires_at=expires_at,
    )

    resolved = resolve_link(link, now=expires_at + timedelta(days=1))

    assert resolved is None


def test_resolve_link_exactly_at_expiry_returns_none():
    created_at = datetime(2026, 1, 1, 12, 0, 0)
    expires_at = created_at + timedelta(days=7)
    link = create_link(
        target_url="https://example.com",
        short_code="abc123",
        now=created_at,
        expires_at=expires_at,
    )

    resolved = resolve_link(link, now=expires_at)

    assert resolved is None
