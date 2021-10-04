from dataclasses import dataclass
from .role import Role


@dataclass
class User:
    id: int
    name: str
    role: Role

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int) -> None:
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_role(self) -> Role:
        return self.role

    def set_role(self, role: Role) -> None:
        self.role = role

