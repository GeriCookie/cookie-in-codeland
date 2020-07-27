def move_element_to_end(array, to_move):
	left_index = 0
	right_index = len(array) - 1
	while left_index <= right_index:
		if array[left_index] != to_move:
			left_index += 1
		elif array[right_index] == to_move:
			right_index -= 1
		elif array[left_index] == to_move and array[right_index] != to_move:
			array[left_index], array[right_index] = array[right_index], array[left_index]
			left_index += 1
		
	return array