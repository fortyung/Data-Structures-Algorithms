#----------------------------------------
# Big O
# Time Complexity
#----------------------------------------

import time
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo' for i in range(100000)]

def findNemo(array):
  t0 = time.time()
  for i in range(len(array)):
    if array[i] == 'nemo':
      print('Found Nemo!') 
      break
  t1 = time.time()
  print('time taken=', (t1-t0)*1000)
findNemo(nemo) 
# O(n) --- linear time
#-----------------------------------------

def printNemo(array):
  print(array[0])
  print(array[1])

printNemo(everyone)
# O(1) ---constant time
#------------------------------------------

def funNoFun(box1, box2):
  for i in range(len(box1)):
    print(i)
  for j in range(len(box2)):
    print(j)
# O(n + m)
#------------------------------------

lop = [1,2,3,4,5]

for i in lop:
  for j in lop:
    print(j, i)
# O(n^2) [nested loop]
#--------------------------------------------
# O(n!) [ adding a loop for every element]


#----------------------------------------
# Space Complexity
#----------------------------------------

def booo(n):
  for i in range(n):
    p = i
# O(1)
# the `p` variable is overwritten each time
#----------------------------------------

lop = []
def booo(n):
  for i in range(n):
    lop.append('hi')
# O(n)
# Dependent on the input and complies in memory
