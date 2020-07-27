# Solution 1
def is_valid_subsequence(array, sequence):
	index = 0
	for num in array:
		if num == sequence[index]:
			index += 1
			if index == len(sequence):
				return True
	return False	

# Solution 2
def is_valid_subsequence_second(array, sequence):
	array_index = 0
	sequence_index = 0
	while array_index < len(array) and sequence_index < len(sequence):
		if array[array_index] == sequence[sequence_index]:
			array_index += 1
			sequence_index += 1
		else:
			array_index += 1
	return sequence_index == len(sequence)

