import numpy as np

## create array using numpy
##create a 1D array
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape) ## Shape of the array

## reshape the array
arr2 = arr1.reshape((1, 5)) ## reshaped to 1 row and 5 columns 
print(arr2)
print(arr2.shape) ## Shape of the array

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.shape) ## Shape of the array

print(np.arange(0, 10, 2).reshape((5,1))) ## Reshaped to 5 rows and 1 column

print(np.ones((3,4))) ## creates a 2D array with ones

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)

arr = np.array([1,2,3,4,5])
print(np.sqrt(arr)) ## square root of each element

arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr[2:3, 1:4]) ## Prints row 2, columns 1 to 3
print(arr[1:,2:]) ## Prints rows 1 to end, columns 2 to end

## calculate mean, std dev and normalized array
arr = np.array([1,2,3,4,5])
mean = np.mean(arr)
print(mean)
std_dev = np.std(arr)
print(std_dev)
## Normalization means rescaling the array to have a mean of 0 and a standard deviation of 1
normalized = (arr - mean) / std_dev
print(normalized)
## Variance means the average of the squared differences from the mean
var = np.var(arr)
print(var)

## Logical operations using numpy
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr > 2) ## Prints a boolean array
print(np.any(arr > 2)) ## Checks if any element is greater than 2
print(np.all(arr > 2)) ## Checks if all elements are greater than 2
print(arr[(arr > 2) & (arr < 5)]) ## Prints elements greater than 2 and less than 5