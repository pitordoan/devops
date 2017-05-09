def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        mid_point = (first + last)//2
        if list[mid_point] == item:
            found = True
        else:
            if item < list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1

        return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
