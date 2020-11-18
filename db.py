
import os
from dataclasses import dataclass
from typing import List, Any, Dict

from dataclasses_json import dataclass_json

from db_api import DBTable, DBField, SelectionCriteria
from files_utils import insert_to_dict, insert_dict_to_file, read_file, DB_ROOT, write_to_file, is_file_exist

num_tables_ = 0


@dataclass_json
@dataclass
class DataBase:
    def __init__(self):

        if not is_file_exist(f"{DB_ROOT}/tables.json"):
            insert_dict_to_file('tables')

    def create_table(self,
                     table_name: str,
                     fields: List[DBField],
                     key_field_name: str) -> DBTable:
        table_fields = [field.name for field in fields]

        if key_field_name not in table_fields:
            raise ValueError
        if os.path.isfile(f"db_files/{table_name}.json"):
            raise ValueError

        global num_tables_
        db_table = DBTable(table_name, fields, key_field_name)
        insert_to_dict(db_table.name, db_table.key_field_name, db_table.fields)
        insert_dict_to_file(db_table.name)
        num_tables_ += 1
        return db_table

    def num_tables(self) -> int:
        return num_tables_

    def get_table(self, table_name: str) -> DBTable:
        table = read_file(table_name + '.json')

        counter = len(table.keys()) if {} != table else 0

        dictionary = read_file('tables.json')
        return DBTable(table_name, dictionary[table_name]['fields'], dictionary[table_name]['key_field_name'], counter)

    def delete_table(self, table_name: str) -> None:
        global num_tables_
        os.remove(DB_ROOT / (table_name + '.json'))
        dictionary = read_file('tables.json')
        dictionary.pop(table_name, None)

        if num_tables_ > 0:
            num_tables_ -= 1
        write_to_file(dictionary, table_name + '.json')

    def get_tables_names(self) -> List[Any]:
        dictionary = read_file('tables.json')
        return list(dictionary.keys())

    def query_multiple_tables(
            self,
            tables: List[str],
            fields_and_values_list: List[List[SelectionCriteria]],
            fields_to_join_by: List[str]
    ) -> List[Dict[str, Any]]:
        raise NotImplementedError
