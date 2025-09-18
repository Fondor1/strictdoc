import uuid
from typing import Optional


class MID(str):
    def __new__(cls, mid_value: str) -> "MID":
        assert isinstance(mid_value, str) and len(mid_value) > 0, mid_value
        return super().__new__(cls, mid_value)

    @staticmethod
    def create(
        *,
        deterministic: bool = False,
        node_uid: Optional[str] = None,
        node_title: Optional[str] = None,
        node_statement: Optional[str] = None,
    ) -> "MID":
        """
        Generate a MID. If deterministic is True, use uuid5 with node content.
        Otherwise, use uuid4 (random).
        """
        if deterministic:
            # Compose a string from node content
            content = (
                f"{node_uid or ''}|{node_title or ''}|{node_statement or ''}"
            )
            namespace = uuid.UUID("12345678-1234-5678-1234-567812345678")
            return MID(uuid.uuid5(namespace, content).hex)
        return MID(uuid.uuid4().hex)

    def get_string_value(self) -> str:
        return str(self)
