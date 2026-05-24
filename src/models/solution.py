"""
solution.py

Purpose:
Store question solutions.

Responsibilities:

- Preserve detailed explanations
- Support AI-generated solutions
- Track verification status

Notes:

Solutions may require teacher review.
"""


from src.models.provenance import Provenance
from pydantic import BaseModel

class Solution(BaseModel):
    """
    Detailed solution/explanation.
    """

    content_tex: str

    provenance: Provenance

    is_verified: bool = False