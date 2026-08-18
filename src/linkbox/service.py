"""Business logic for creating and resolving links."""

from __future__ import annotations

from dataclasses import replace
from datetime import datetime

from linkbox.models import Link


def create_link(
    target_url: str,
    short_code: str,
    now: datetime,
    expires_at: datetime | None = None,
) -> Link:
    """Build a new link record.

    The caller is responsible for supplying a unique ``short_code`` and
    for persisting the returned ``Link`` if needed; this function only
    assembles the record.

    Args:
        target_url: The destination URL the short code should point to.
        short_code: The short identifier to associate with the target URL.
        now: The creation timestamp.
        expires_at: Optional expiry timestamp. If ``None``, the link
            never expires.

    Returns:
        A new ``Link`` with ``click_count`` initialized to zero.
    """
    return Link(
        short_code=short_code,
        target_url=target_url,
        created_at=now,
        expires_at=expires_at,
        click_count=0,
    )


def resolve_link(link: Link, now: datetime) -> Link | None:
    """Resolve a link, recording a click if it is still valid.

    A link with no ``expires_at`` never expires and always resolves.
    A link is considered expired once ``now`` reaches or passes its
    ``expires_at`` timestamp, in which case resolution fails.

    Args:
        link: The link to resolve.
        now: The timestamp at which resolution is attempted.

    Returns:
        A copy of ``link`` with ``click_count`` incremented by one if
        the link is still valid, or ``None`` if the link has expired.
    """
    if link.expires_at is not None and now > link.expires_at:
        return None

    return replace(link, click_count=link.click_count + 1)
