"""
source.py

Purpose:
Store original source information.

Responsibilities:

- Track original file location
- Preserve raw source content
- Support import tracing

Notes:

Source information is metadata only.

It does NOT represent question content itself.
"""

from pydantic import BaseModel


class Source(BaseModel):
    """
    Original source information.
    """

    file_path: str

    raw_tex: str