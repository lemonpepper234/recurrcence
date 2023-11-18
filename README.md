# Recurrence

This is an example about how recursion works in search all possible combinations of a given set of list, beside with additional insert function to insertion another list into the input list during recursion.

## Basic Recursion

```python
def iterate(current_loop, max_loop, iterate_range, current_path = [], result = None):

if result == None:
    result = []

#* the interation count for the current interation
#* the interval between max_loop and current_loop narrows after each interation
index = len(iterate_range) - (max_loop - current_loop + 1)

#* otherwise in the first loop the index will be minus
assert index >= 0, \
    "the length of iterate_loop mismatches the number of loop."

if current_loop > max_loop:
    result.append(current_path)
    return

for i in range(iterate_range[index]):
    iterate(current_loop + 1, max_loop, iterate_range, current_path + [i], result)

return result
```

Here are something to notice:

- Only the parameters of a function could be passed in the nexr recursion, so the value should be stored in the function's parameters.

- When it reaches the base level of the recurrence, the result should be returned. 

For this example, in the first step of the loop, the function keeps nesting unitl it reaches the reutrn condition -- current_loop > max_loop. Then it returns to the level which current_loop = max_loop, continues the next step of loop, and so on.

After the loop in the level of current_loop = max_loop, the function returns to the level of current_loop = max_loop - 1, and so on.

For a simple example:

```python
current_loop = 1
max_loop = 3
iterate_range = [4, 3, 2] 

result = iterate(current_loop, max_loop, iterate_range)
```

The output result is:
```python
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[0, 2, 0]
[0, 2, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
[1, 2, 0]
[1, 2, 1]
[2, 0, 0]
[2, 0, 1]
[2, 1, 0]
[2, 1, 1]
[2, 2, 0]
[2, 2, 1]
[3, 0, 0]
[3, 0, 1]
[3, 1, 0]
[3, 1, 1]
[3, 2, 0]
[3, 2, 1]
```

## ~~Usage of iterate_list_with_insert:~~

## Usage of iterate_list and insert_into_input_list:

```python
Multiwfn_input_list = iterate_list(1, len(input_list), input_list)
Multiwfn_output_list = insert_into_input_list(Multiwfn_input_list, insert_index, insert_list)
```

- `input_list`: two layer list, the permutation and cobiination happens in the elements in the second layer between different lists in the first layer.

**each list elements in `input_list`** corresponds to one line of the input file for Multiwfn.

- `insert_list`: one layer list, the list to be inserted into the input list. **Only one layer could be added while using `insert_into_input_list` fuction.**

During the recurrsion proceed, the list elements in the second layer act the same as normal variables. However when using the `insert_into_input_list` fucntion, which the input list `insert_list` is a one layer list, beside with `insert_index`, the list elements in the modified list (`Multiwfn_input_list`) will exhaust all possible combinations with (if exist) the corresponding list element in the `insert_list`.



