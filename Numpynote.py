import numpy as np

# Creating 5x4 array
array = np.arange(20).reshape(5,4)
print(array)
print()

# If no axis mentioned, then it works on the entire array
print (np.argmax(array))

# If axis=1, then it works on each row
print(np.argmax(array, axis=1))

# If axis=0, then it works on each column
print(np.argmax(array, axis=0))

print("*"*60)

array = np. array([
    [3, 7, 1],
    [10, 3, 2],
    [5, 6, 7]
    ])

print (array)
print()

# Sort the whole array

print(np.sort(array, axis=None))

# Sort along each row

print(np.sort(array, axis=1))

# Sort along each column

print(np.sort(array, axis=0))

print("*"*60)

list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
    ]

result = []

for i in range(len(list)):
    result.append(np.mean(list[i]))

print(result)

print("*"*60)

array = np.array([
    [3, 2, 8],
    [4, 12, 34],
    [23, 12, 67]
])

newRow = np.array([2, 1, 8])
newArray = np.vstack((array, newRow))
print (newArray)

array = np. array ([3, 6, 7, 2, 5, 1, 8])
reversedArray = np.flipud(array)
print(reversedArray)

print("*"*60)

matrix1 = [
    [3, 4, 2],
    [5, 1, 8],
    [3, 1, 9]
    ]

matrix2 = [
    [3, 7, 51],
    [2, 9, 8],
    [1, 5, 8]
    ]

result = np.dot(matrix1, matrix2)
print(result)

print("*"*60)

n = 8

# Create a nxn matrix filled with 0
matrix = np.zeros((n,n), dtype=int)

# f111 1 with alternate rows and column
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1

# Print the checkerboard pattern
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

print("*"*60)
 
import pandas as pd
import numpy as np

df = pd.read_csv("income.csv")
print (df)


income_dc = df.columns #all data columns from the income dataset
print (income_dc)#first 2 columns from the income dataset
print (income_dc [ :2])#find datatypes for all the columns
print (df.dtypes)

df.Y2008 = df.Y2008.astype (float) #converts integer type into float datatype
print (df.dtypes)
print ("total number of rows and columns:", df. shape)
print ("total number of rows:", df. shape [0])
print ("total number of columns:", df. shape [1])

print ("First Five Rows from income dataset")
print (df.head () )

print ("Last Five Rows from income dataset")
print (df.tail () )

print ("First three")
print (df. head (3) )

print ("Last three Rows from income dataset")
print (df.tail (3) )
print (df.iloc[0:5])
print (df[0:5])








































