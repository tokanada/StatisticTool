def partition(A, p, r):
	"""
	Given an array A, partition the subarray A[p..r], using A[r] as the pivot value.

	:param A: the array to be merged
	:param p: the left boundary
	:param r: the right boundary
	:type A: list
	:type p: int
	:type r: int
	"""
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i = i + 1
			temp = A[i]
			A[i] = A[j]
			A[j] = temp
	temp = A[i + 1]
	A[i + 1] = A[r]
	A[r] = temp
	return i + 1

def QuickSort(A, p, r):
	"""
	Sort the subarray A[p..r] in place, recursively.

	:param A: the input array
	:param p: left boundary of the subarray to be sorted
	:param r: right boundary of the subarray to be sorted
	:type A: list
	:type p: int
	:type r: int
	"""
	if p < r:
		q = partition(A, p, r)
		QuickSort(A, p, q - 1)
		QuickSort(A, q + 1, r)
	return list
