list1 = [1, 2, 3]
list2 = ['one', 'two', 'three']

# Zip the lists
zipped_result = zip(list1, list2)
result_list = list(zipped_result)

print("Zipped Result:", result_list)

# Unzip the zipped result
unzipped_lists = list(zip(*result_list))

print("Unzipped Lists:", unzipped_lists)
