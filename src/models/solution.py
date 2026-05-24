from src.models.provenance import Provenance

from pydantic import BaseModel


class Solution(BaseModel):
    """
    Detailed solution/explanation.
    """

    content_tex: str

    provenance: Provenance

    is_verified: bool = False