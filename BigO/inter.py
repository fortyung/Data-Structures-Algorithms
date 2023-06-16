array1_false = ['a', 'b', 'c', 'x', 2 ]
array2_false = ['z', 'y', 2]

array1_true = ['a', 'b', 'c', 'x']
array2_true = ['z', 'y', 'x']


def containsItem(arry1, arry2):
  # map = {}
  # map = {element: True for element in arry1 if element not in map}
  my_set = set(arry1)


  for element2 in arry2:
    if element2 in my_set:
      return True
  return False

print(containsItem(array1_false, array2_false))
