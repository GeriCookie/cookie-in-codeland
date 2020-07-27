def longest_peak(array):
    longest = 0
    current = 1
    index = 1
    while index < len(array)-1:
	    if array[index-1] < array[index] and array[index] > array[index+1]:
		    current+=2
	    else:
		    index+=1
		    continue
		
	    left_index = index - 2
	    while left_index >= 0:
		    if array[left_index] < array[left_index + 1]:
			    left_index -= 1
			    current +=1
		    else:
			    break
		
	    right_index = index + 2
	    while right_index < len(array):
		    if array[right_index] < array[right_index - 1]:
		 	    right_index += 1
		 	    current += 1
		    else:
			    break
			
	    if current > longest:
		    longest = current
		    current = 1
	    index = right_index
    return longest