bob = {
    'age': 12,
    'name': 'young',
    'magic': True,
    'scream': lambda: print('ahhh!')
}

print(bob['age']) # O(1)
print(bob['name'])
bob['new'] = 'hello' # O(1)
bob['scream']() # O(1)

print(bob)