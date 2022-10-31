
test_array = ['alpha','alpha1','alpha2','bmw','b1','beta','cnot','charlie','d1','d2']
entire_array = []
init = 0
i = -1
for x in test_array:
  i += 1
  if test_array[i-1][0] != test_array[i][0]:
    entire_array.append(test_array[init:i])
    init = i
print(init)
print(test_array[init])
entire_array.pop(0)
entire_array.append(test_array[init:])
print(entire_array)
