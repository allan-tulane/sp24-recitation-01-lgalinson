"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if left > right:
		return -1

	mid = (left + right) // 2
	if mylist[mid] == key:
		return mid
	elif mylist[mid] > key:
		return _binary_search(mylist, key, left, mid - 1)
	else:
		return _binary_search(mylist, key, mid + 1, right)


def time_search(search_fn, mylist, key):
	start_time = time.time()  # Get the current time before running the search function
	search_fn(mylist, key)     # Run the search function
	end_time = time.time()    # Get the current time after running the search function

    # Calculate the elapsed time in milliseconds
	total_time = (end_time - start_time) * 1000

	return total_time

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	result_times = []
	
	for n in sizes:
		num_list = list(range(int(n)))

		linear_search_time = time_search(linear_search, num_list, -1)

		binary_search_time = time_search(binary_search, num_list, -1)

		result_times.append((n, linear_search_time, binary_search_time))

	return result_times

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
print(1)
print(2)

print_results(compare_search())