import numpy as np

array1 = np.array([[1, 2], [3, 4]])

# print(array1)
print(array1[array1 > 2])

numbers = np.random.choice(100, 10).reshape(2, 5)
print(numbers)

it = np.nditer(numbers, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    print(str(it.multi_index) + ":" + str(it.value))
    it.iternext()

numbers2 = np.arange(0, 100, 10).reshape(2, 5)
print(numbers2)
