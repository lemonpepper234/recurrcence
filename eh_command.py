import os,sys

#* the meaning of these files
#todo learn more about it
''' 10 Output cube file of hole distribution to current folder
 11 Output cube file of electron distribution to current folder
 12 Output cube file of overlap of hole-electron to current folder
 13 Output cube file of transition density to current folder
 14 Output cube file of transition dipole moment density to current folder
 15 Output cube file of charge density difference to current folder
 16 Output cube file of Cele and Chole functions to current folder'''

command_list = [18, 1, 'X', 'X', 1, 3, 'X', 'X']

subsitute_index = [index for index, element in enumerate(command_list) if element == 'X']
subsitute_command = ['AU8PT5TDDFT.LOG', 
                     [25, 14, 23, 9, 13, 7, 16], 
                     [10, 11, 12, 13, 14, 15, 16],
                     [1, 1, 2, None, [1, 2, 3, 4], None, None]]

assert len(subsitute_index) == len(subsitute_command), \
    'The length of subsitute_index and subsitute_command are not equal you stupid idiot!'

current_directory = os.getcwd()
all_entries = os.listdir(current_directory)

print (os.getcwd())

print (len(subsitute_command))

