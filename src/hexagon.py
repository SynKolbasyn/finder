import os
import aiogram
import user


def create_new_user(msg: aiogram.types.Message) -> user.User:
    user_data = user.User(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.full_name)
    user_data.update_data()
    return user_data


def create_exist_user(msg: aiogram.types.Message) -> user.User:
    user_data = user.get_dict_from_json(f"{msg.from_user.id}.json")
    return user.User(user_data["ID"], user_data["first_name"], user_data["last_name"], user_data["username"])


def except_new_user(msg: aiogram.types.Message) -> user.User:
    if f"{id}.json" in os.listdir("../users/"):
        return create_exist_user(msg)
    return create_new_user(msg)


def get_unswer(msg: aiogram.types.Message) -> str:
    user_data = except_new_user(msg)
    return user_data.message_process(msg.text)
