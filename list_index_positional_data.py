n =  int(input('Enter No of inputs as length:'))
l1 = []
l2 = []
print('Now Enter numbers as pairs at each input line:')
for inp in range(0, n):
    # l1.append(int(input()))
    numbers1, numbers2 = map(int, input().split())
    l1.append(numbers1)
    l2.append(numbers2)
print("L1 = ",l1, "and ", "L2 = ", l2)

merged_L3 = l1[1::2] + l2[::2]
print("The merge lists of odd from l1 and even from l2:", merged_L3)