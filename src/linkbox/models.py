"""Domain models for linkbox."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Link:
    """A shortened link and its click-tracking state.

    Attributes:
        short_code: The short identifier used to reach the target URL.
        target_url: The destination URL the short code redirects to.
        created_at: When the link was created.
        expires_at: When the link stops being resolvable, or ``None``
            if the link never expires.
        click_count: How many times the link has been successfully
            resolved. Starts at zero.
    """

    short_code: str
    target_url: str
    created_at: datetime
    expires_at: datetime | None = None
    click_count: int = 0
