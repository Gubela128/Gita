import ast


def display_file(file_address):
    with open(file_address, 'r') as file:
        content = file.read()
        print(content)


def read_file(file_address):
    with open(file_address, 'r') as file:
        content = file.read()
        return content


def update_file(file_address, new_content):
    with open(file_address, 'w') as file:
        file.write(new_content)


def write_dict_to_file(file_address, new_data):
    with open(file_address, 'r') as file:
        content = file.read()
        players_list = ast.literal_eval(content)

    players_list.extend(new_data)

    with open(file_address, 'w') as file:
        file.write(str(players_list))


if __name__ == "__main__":
    file_address = "path/to/your/file.txt"

    # 1. Display File Content
    display_file(file_address)

    # 2. Read File Content
    content = read_file(file_address)
    print(content)

    # 3. Update File Content
    new_content = "chess_players = [\n  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},\n  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},\n  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'ratin...  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},\n]"
    update_file(file_address, new_content)

    # 4. Write/Update Dictionary to File
    new_players = [
        {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
        {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
    ]
    write_dict_to_file(file_address, new_players)
