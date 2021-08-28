import statistics
from collections import Counter

values = [47,95,88,73,88,84]


def sum_values(v):
	sum = 0
	for i in v:
		sum = sum + i
	return sum
  
def count_values(v,v1):
	count = 0
	for i in v:
		if (i == v1):
	  		count = count + 1
	return count


print("Count of 88 in values is " + str(count_values(values,88)))
print("Sum of Values is " + str(sum_values(values)))
  
# Calculate mean
n = len(values)
get_sum = sum_values(values)
mean = get_sum / n
  
print("Mean of Values is: " + str(mean))

# Calculate median
n = len(values)
values.sort()
  
if n % 2 == 0:
    median1 = values[n//2]
    median2 = values[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[n//2]
print("Median of Values is: " + str(median))


# Calculate mode

n = len(values)
  
data = Counter(values)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode of Values is / are: " + ', '.join(map(str, mode))
      
print(get_mode)
