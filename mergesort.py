def mergeSort(list_to_sort):
    
    length = len(list_to_sort)
    
    if (length > 1):
        
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]

        mergeSort(left)
        mergeSort(right)

        index_left = 0
        index_right = 0
        index_list = 0
        
        # We sort until the end of one sublist is reached
        while index_left < len(left) and \
              index_right < len(right):
            
            # Comparison of elements and place the smaller value in the original list
            if left[index_left] <= right[index_right]:
                list_to_sort[index_list] = left[index_left]
                index_left += 1
            else:
                list_to_sort[index_list] = right[index_right]
                index_right += 1
            index_list += 1
        
        # If one of our sublists is empty,
        # we sort in the remaining elements from the other list
        while index_left < len(left):
            list_to_sort[index_list] = left[index_left]
            index_left += 1
            index_list += 1

        while index_right < len(right):
            list_to_sort[index_list] = right[index_right]
            index_right += 1
            index_list += 1

import matplotlib.pyplot as plt


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.bar(x, my_list)
plt.show()
merge_sort(my_list)
plt.bar(x, my_list)
plt.show()

