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

For a s