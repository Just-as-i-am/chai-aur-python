import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print(arr)
#print(arr[0][0][1])
#print(arr.ndim)

arr2 = np.array([1,2,3],ndmin=5) #setting min no. of dimensions here i set to 5
print(arr2) 
print('number of dimensions :', arr2.ndim)