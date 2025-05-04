'''
you are given an array of integers. An inversion is defined as a pair (i,j) such that:
● i<j
● array[i]>array[j]
Write an algorithm to count the total number of inversions in the array using a divide and
conquer approach.
Sample:
Input: [2, 4, 1, 3, 5]
Output: 3
Explanation: The inversions are (2, 1), (4, 1), and (4, 3)
'''

def find_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0 # base case, returns array and 0 inversions
        mid = len(arr) // 2
        left, left_inversions = merge_sort(arr[:mid]) # sort left half
        right, right_inversions = merge_sort(arr[mid:]) # sort right half
        merged, merged_inversions = merge(left, right) # merge sorted halves
        return merged, right_inversions + left_inversions + merged_inversions # return merged array, total invs
    def merge(left, right):
        res = []
        i = j = inversion_count = 0 # set indecies for left and right arrays
        while i < len(left) and j < len(right): # while both arrays have elements
            if left[i] <= right[j]: # if left element is smaller or equal to , not inversion
                res.append(left[i]) # add to result array
                i += 1 # increment left index
            else:
                res.append(right[j]) # if left element is greater, it is an inversion. Here we add the right element to the result
                inversion_count += len(left) - i # add to inversion count:
                '''
                REASON: since both arrays are sorted, all elements in left[i:] are greater than right[j], which means every element in left[i:] forms an inversion with right[j]
                So, if left[i] > right[j], then all elements from left[i] to the end of left are greater than right[j].
                '''
                j += 1
        res+=left[i:] # add remaining elements from left
        res+=right[j:] # add remaining elements from right
        return res, inversion_count
    _, inversions = merge_sort(arr) # disregard merged array, we only need that for merge sort function
    return inversions # return final inversion count 

res1 = find_inversions([2, 4, 1, 3, 5])
print(res1) # Output: 3
