def read_data(source:str) -> dict:
    with open(source, 'r', encoding='utf-8') as file:
        ret_dict = {i: line.split(',') for i, line in enumerate(file.read().splitlines())}
    return ret_dict