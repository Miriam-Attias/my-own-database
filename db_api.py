from dataclasses import dataclass

from typing import Any, Dict, List, Type

from dataclasses_json import dataclass_json

from files_utils import read_file, write_to_file, DB_ROOT

COMPARISONS = {
    '==': lambda a, b: a == b,
    '=': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
}


@dataclass_json
@dataclass
class DBField:
    name: str
    type: Type


@dataclass_json
@dataclass
class SelectionCriteria:
    field_name: str
    operator: str
    value: Any


@dataclass_json
@dataclass
class DBTable:
    name: str
    fields: List[DBField]
    key_field_name: str
    records_counter: int = 0

    def count(self) -> int:
        return self.records_counter

    def insert_record(self, values: Dict[str, Any]) -> None:
        dictionary = read_file(self.name + '.json')

        if str(values[self.key_field_name]) in dictionary.keys():
            raise ValueError

        dictionary[values[self.key_field_name]] = {k: str(v) for k, v in values.items()}  # ?????????
        write_to_file(dictionary, self.name + '.json')
        self.records_counter += 1

    def delete_record(self, key: Any) -> None:
        dictionary = read_file(self.name + '.json')

        if str(key) not in dictionary.keys():
            raise ValueError
        dictionary.pop(str(key), None)
        write_to_file(dictionary, self.name + '.json')
        self.records_counter -= 1

    def delete_records(self, criteria: List[SelectionCriteria]) -> None:
        dictionary = read_file(self.name + '.json')
        list_ = self.query_table(criteria)

        for key in list_:
            dictionary.pop(key[self.key_field_name], None)
            self.records_counter -= 1
        write_to_file(dictionary, self.name + '.json')

    def get_record(self, key: Any) -> Dict[str, Any]:
        dictionary = read_file(self.name + '.json')
        return dictionary[str(key)]

    def update_record(self, key: Any, values: Dict[str, Any]) -> None:
        dictionary = read_file(self.name + '.json')
        dictionary[key] = values
        write_to_file(dictionary, self.name + '.json')

    def query_table(self, criteria: List[SelectionCriteria]) \
            -> List[Dict[str, Any]]:

        dictionary = read_file(self.name + '.json')
        list_ = []

        for row_key in dictionary:
            for criterion in criteria:
                if not COMPARISONS[criterion.operator](str(dictionary[row_key][criterion.field_name]), str(criterion.value)):
                    break
            else:
                list_.append(dictionary[row_key])
        return list_

    def create_index(self, field_to_index: str) -> None:
        raise NotImplementedError
