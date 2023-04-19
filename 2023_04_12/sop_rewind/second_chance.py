"""
Test data
 - (2)(5)(4)(3)(6)(5)(4)(3)(6)(8)(4)(3)(2)(1)(2)(6)(5)(2)(1)(8)
 - (5)(1)(6)(2)(7)(5)(4)(8)(5)(3)(6)(3)(8)(1)(8)(5)(2)(1)(8)(6)
"""

from pydantic import BaseModel
from typing import List
import re


class MemCell(BaseModel):
    value: int
    is_protected: bool = True

    def update(self, new_value):
        self.value = new_value
        self.is_protected = True

    def __str__(self):
        return f"{self.value}({int(self.is_protected)})"


class Process(BaseModel):
    cells: List[MemCell] = []
    last_insert_index = 0
    max_cells: int
    page_faults_count: int = 0

    def mutate(self, new_value):
        for cell in self.cells:
            if new_value == cell.value:
                cell.is_protected = True
                return

        if len(self.cells) < self.max_cells:
            self.cells.append(MemCell(value=value, is_protected=True))
            self.last_insert_index = (self.last_insert_index + 1) % self.max_cells
            self.page_faults_count += 1
            return

        current_index = self.last_insert_index % self.max_cells
        while True:
            if not self.cells[current_index].is_protected:
                self.cells[current_index].update(value)
                self.last_insert_index = (current_index + 1) % self.max_cells
                self.page_faults_count += 1
                return
            else:
                self.cells[current_index].is_protected = False

            current_index = (current_index + 1) % self.max_cells

    def __str__(self):
        return " ".join([str(cell) for cell in self.cells])


frames_num = int(input("Enter the number of frames: "))
user_input = input("Enter the reference string: ")

if not re.match(r'^(\(\d\))+$', user_input):
    raise Exception('Input is not valid! Input should be like this: (4)(3)(6)(8)(4)(3)(2)')

page_array = list(map(int, user_input.strip().replace('(', '').replace(')', ' ').split()))

frame = Process(max_cells=frames_num)

for i, value in enumerate(page_array):
    frame.mutate(value)
    print(i + 1, f'->{value}', frame, sep='\t')

print('Page faults:', frame.page_faults_count)
