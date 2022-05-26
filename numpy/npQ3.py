#counting the frequency of each element in given array
import numpy as np
a=np.array([1,2,3,4,2,1])
arr_bins = np.bincount(a)
print(arr_bins)
len(arr_bins)