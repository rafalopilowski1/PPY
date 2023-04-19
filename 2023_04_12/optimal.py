"""
Test data
 - (2)(5)(4)(3)(6)(5)(4)(3)(6)(8)(4)(3)(2)(1)(2)(6)(5)(2)(1)(8)
 - (5)(1)(6)(2)(7)(5)(4)(8)(5)(3)(6)(3)(8)(1)(8)(5)(2)(1)(8)(6)
"""

from lib.algorithms.optimal import process
from lib.utils import print_header, read_test_data

capacity = int(input("Podaj liczbę ramek: "))

frame, fault_counter, page_fault = [], 0, 'No'

test_data = read_test_data()

print_header(capacity)

process(test_data, frame, fault_counter, capacity)

print()
print(f"Total Requests: {len(test_data)}")
print(f"Total Page Faults: {fault_counter}")
print(f"Fault Rate: {(fault_counter / len(test_data)) * 100}%")
