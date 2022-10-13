def lists(list1, list2):
	return {keyItem:valueItem for keyItem,valueItem in zip(list1, list2) if len(list1)==len(list2)}

print(lists([1,2,3], [4,3,2]))
print(lists([16, 100, 50], []))
print(lists([10, 22], [1, 2]))
