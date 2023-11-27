import json


def get_dict_from_json(file_name: str) -> dict:
    return json.load(open(file_name, "r", encoding="utf-8"))


class User:
    def __init__(self, ID: int, first_name: str, last_name: str, username: str):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def get_dict_data(self) -> dict:
        return {
            "ID": self.ID,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username
        }

    def update_data(self):
        json.dump(
            self.get_dict_data(),
            open(f"../users/{self.ID}.json", "w", encoding="utf-8"),
            indent=2,
            ensure_ascii=False
        )

    def command_start(self) -> str:
        return "There should be a welcome message here"

    def command_help(self) -> str:
        return "There should be a text explaining how to use the bot"

    def message_process(self, msg: str) -> str:
        match msg:
            case "/start":
                return self.command_start()
            case _:
                return self.command_help()
