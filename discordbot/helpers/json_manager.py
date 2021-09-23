import json

def add_user_to_whitelist(user_id: int):
    with open("whitelist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
    with open("whitelist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


def remove_user_from_whitelist(user_id: int):
    with open("whitelist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
    with open("whitelist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)