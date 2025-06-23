from typing import Dict, List, Optional, Union

class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self

def create_person_list(people_data: List[Dict[str, U]()]()_
