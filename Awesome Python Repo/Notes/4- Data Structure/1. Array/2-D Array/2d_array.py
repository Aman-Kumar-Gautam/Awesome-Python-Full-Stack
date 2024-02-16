import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print("\n1st print TwoDArray\n", twoDArray)     # 1st print

newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
print("\n2nd print After insertion newTwoDArray\n", newTwoDArray)     # 2nd print

print("\n3rd print length of twoDArray:- ", len(twoDArray), "\n", twoDArray)     # 3rd print

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print("\n4th print Append method\n", newTwoDArray)     # 4th print
print("\n5th print length of New twoDArray:- ", len(newTwoDArray), "\n", newTwoDArray)      # 5th print
print("\n6th print length of New 2D Array at index 0:- ", len(newTwoDArray[0]), "\n", newTwoDArray)     # 6th print

# Accessing in 2 D Array

def access_elements(array, row_index, col_index):
    if row_index >= len(array) and col_index >= len(array[0]):
        print('Incorrect Index')     # 7th print
    else:
        print("Value at row", array[row_index], "Row and", [col_index], "index is:- ", array[row_index][col_index])
        # 8th print


access_elements(newTwoDArray, 2, 3)

# Traversing at 2 D Array


def traverse_2d_array(array):
    print("traverseTDArray")
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverse_2d_array(twoDArray)

# Searching at 2D Array


def search_2d_array(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at row '+str(i)+" column "+str(j)
    return 'The element no found'


print("searchTDArray", search_2d_array(twoDArray, 18))


# Deletions at 2D Array
print("2d array\n", twoDArray)
newTDArray = np.delete(twoDArray, 0, axis=0)
print("deletion in 2d array:-\n", newTDArray)
"""
 [[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
:::::::::::::::::At 0, axis=1::::::::::
[[15 10  6]
 [14 11  5] 
 [17 12  8]     
 [18 14  9]]

[[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
::::::::::::::::::::::::At 1 axis=0::::::
[[11 15 10  6]
 [12 17 12  8]
 [15 18 14  9]]
 
 
 [[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
At 1, 1::::::::::::::::::::::::
 [[11 10  6]
 [10 11  5]
 [12 12  8]
 [15 14  9]]
 
  [[11 15 10  6]
 [10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
 At 0, 0::::::::::::::::::::::
  [[10 14 11  5]
 [12 17 12  8]
 [15 18 14  9]]
"""