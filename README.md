# CMPS 2200  Recitation 01

**Name (Team Member 1): Lakeland Galinson**  
**Name (Team Member 2): Chris Yarbro**

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [x] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [x] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [x] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [x] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
For linear search, the worst-case occurs when the key is not present in the list at all. In such cases, the function needs to iterate through the entire list, resulting in O(n) time complexity.

For binary_search, the worst-case occurs when the key is not present in the list or is present at the ends of the list (front or back). In these cases, the function devides the list in half until the list is empty. The worst-case time complexity for binary search is O(log n).

- [x] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**TODO: your answer goes here**
The best case for linear search occurs when the target key is found at the beginning of the list. In this scenario, the linear search algorithm will find the key in the first comparison.

The best case for binary search occurs when the target key is exactly at the middle of the list. In this scenario, the binary search algorithm finds the key with one comparison. 

- [x] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [x] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [x] 8. Call `print_results(compare_search())` and paste the results here:
|            n |   linear |   binary |
|--------------|----------|----------|
|       10.000 |    0.002 |    0.002 |
|      100.000 |    0.002 |    0.003 |
|     1000.000 |    0.022 |    0.002 |
|    10000.000 |    0.227 |    0.002 |
|   100000.000 |    2.289 |    0.002 |
|  1000000.000 |   21.185 |    0.007 |
| 10000000.000 |  216.087 |    0.013 |

**TODO: add your timing results here**

- [x] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: your answer goes here**
In my empirical results, the time taken by linear search increases linearly with the size of the input list. This aligns with the theoretical running times.

In my empirical results, the time taken by binary search remains relatively constant even as the size of the input list increases exponentially. This matches the theoretical running time.

- [x] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? **TODO: $O(kn)$** 
  + For binary search? **TODO: $O(n^2+klog{_2}(n))$**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: It depends on the size of the values of $k$ and $n$ and the overhead of sorting. If $k$ is large and $n$ is not too big, it's more efficient to sort and then use binary search and vice versa.**
