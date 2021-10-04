from dataclasses import dataclass


@dataclass
class Password:
    user_id: int
    passwd: str

    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, user_id: int) -> None:
        self.user_id = user_id

    def get_passwd(self) -> str:
        return self.passwd

    def set_passwd(self, passwd: str) -> None:
        self.passwd = passwd
