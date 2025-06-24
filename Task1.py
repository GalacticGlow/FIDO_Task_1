def returnElementAtIndex(lst, n):
    return lst[2*n//3 - 1] if n > 1 else None

test_cases = [
    [0, 1, 2],
    [0, 1, 2, 3],
    [0, 1, 2, 3, 4]
]

print('Test case 1: ' + str(test_cases[0]) + ' - ' + str(returnElementAtIndex(test_cases[0], 3)))
print('Test case 2: ' + str(test_cases[1]) + ' - ' + str(returnElementAtIndex(test_cases[1], 4)))
print('Test case 3: ' + str(test_cases[2]) + ' - ' + str(returnElementAtIndex(test_cases[2], 5)))