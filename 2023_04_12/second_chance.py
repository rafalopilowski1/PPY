"""
Test data
 - (2)(5)(4)(3)(6)(5)(4)(3)(6)(8)(4)(3)(2)(1)(2)(6)(5)(2)(1)(8)
 - (5)(1)(6)(2)(7)(5)(4)(8)(5)(3)(6)(3)(8)(1)(8)(5)(2)(1)(8)(6)
"""

from lib.algorithms.second_chance import Process
from lib.utils import read_test_data

frames_num = int(input("Enter the number of frames: "))
page_array = read_test_data()

frame = Process(max_cells=frames_num)

for i, value in enumerate(page_array):
    frame.mutate(value)
    print(i + 1, f'->{value}', frame, sep='\t')

print('Page faults:', frame.page_faults_count)
