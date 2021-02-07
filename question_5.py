# timeit is used to measure the execution time taken by the given code snippet
import timeit

# setup a list and a tuple
list1 = [1,2,3]
tuple1 = (1,2,3)

# measure how much time it takes to run list1 as code 1000 times
list1_time = timeit.timeit(stmt=str(list1), number=1000) 
# measure how much time it takes to run tuple1 as code 1000 times
tuple1_time = timeit.timeit(stmt=str(tuple1), number=1000)

# print out the results
print(list1_time)
print(tuple1_time)