import numpy as np
import os

def sorted_exc_file(file_name):

    strength_lineNum_list = []
    counter = 0
    with open(file_name, 'r') as exc_file:
        for line in exc_file:
            temp_list = []
            if "#" in line:
                temp_list.append(float(line.split()[7]))
                temp_list.append(counter)
                strength_lineNum_list.append(temp_list)
            counter += 1

    sorted_list = sorted(strength_lineNum_list, key=lambda x: x[0], reverse=True)

    #* the structure of sorted_list: [[strength, lineNum], [strength, lineNum], ...]
    return sorted_list


def sorted_file(file_name):
    sorted_list = sorted_exc_file(file_name)
    with open(file_name, 'r') as exc_file:
        lines = exc_file.readlines()

    with open(f"{file_name.split('.')[0]}_sorted.{file_name.split('.')[1]}", 'w') as new_exc_file:
        for i in range(len(sorted_list)):
            new_exc_file.write(lines[sorted_list[i][1]])
            new_exc_file.write(lines[sorted_list[i][1] + 1])

    return None

file_name = input("Please input the file name: ")
sorted_file(file_name)