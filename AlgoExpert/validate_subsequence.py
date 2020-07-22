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
def is_valid_subsequence(array, sequence):
    arrayIndex = 0
	sequenceIndex = 0
	while arrayIndex < len(array) and sequenceIndex < len(sequence):
		if array[arrayIndex] == sequence[sequenceIndex]:
			arrayIndex += 1
			sequenceIndex += 1
		else:
			arrayIndex += 1
	return sequenceIndex == len(sequence)

