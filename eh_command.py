from tools import *

#* the meaning of these files
#todo learn more about it
''' 10 Output cube file of hole distribution to current folder
 11 Output cube file of electron distribution to current folder
 12 Output cube file of overlap of hole-electron to current folder
 13 Output cube file of transition density to current folder
 14 Output cube file of transition dipole moment density to current folder
 15 Output cube file of charge density difference to current folder
 16 Output cube file of Cele and Chole functions to current folder'''

fch_filename = 'Au8Pt5tddft.fch'
LOG_filename = 'AU8PT5TDDFT.LOG'
excited_states_list = [13, 14, 15]

input_list = [[fch_filename], [18], [1], [LOG_filename], [excited_states_list], [1], [3], \
    [10], [11], [12], [13], [14],[1], [14], [2], [14], [3], [14], [4], [15], [16]]
insert_list = [1, 1, 2]
insert_index = [7, 8, 9]


Multiwfn_input_list = iterate_list(1, len(input_list), input_list)
Multiwfn_output_list = insert_into_input_list(Multiwfn_input_list, insert_index, insert_list)
Multiwfn_exe("_excited_states", excited_states_list, Multiwfn_output_list)