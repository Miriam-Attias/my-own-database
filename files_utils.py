import json
import os
from typing import List, Any, Dict

from pathlib import Path

DB_ROOT = Path('db_files')


def is_file_exist(file_name):
    return os.path.isfile(file_name)


def insert_to_dict(table_name: str, key_field_name: str, fields: List[Any]) -> None:
    with open(DB_ROOT / 'tables.json', 'r') as dict_file:
        dictionary = json.load(dict_file)

    if table_name not in dictionary:
        with open(DB_ROOT / 'tables.json', 'w') as dict_file:

            dictionary[table_name] = {"key_field_name": key_field_name,
                                      "fields": [i.name for i in fields if i.name != key_field_name]}
            json.dump(dictionary, dict_file)
    else:
        raise ValueError


def insert_dict_to_file(table_name: str) -> None:
    with open(DB_ROOT / (table_name + '.json'), 'w') as file:
        json.dump({}, file)


def read_file(file_name: str) -> Dict:
    with open(DB_ROOT / file_name, 'r') as dict_file:
        dict_ = json.load(dict_file)
        return dict_


def write_to_file(data: Any, file_name: str) -> None:
    with open(DB_ROOT / file_name, 'w') as file:
        json.dump(data, file)
