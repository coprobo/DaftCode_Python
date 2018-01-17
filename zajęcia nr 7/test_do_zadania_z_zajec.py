from zadania_z_zajec import flatten

def test_flat_list():
	result = flatten([1,2,3,4])

	assert result == [1,2,3,4]

def test_empty_list():
	result = flatten([])

	assert result == []

def test_one_element():
	result = flatten([1])

	assert result == [1]

def list_in_list():
	result = flatten([1,2,3,[4,5]])

	assert result == [1,2,3,4,5]