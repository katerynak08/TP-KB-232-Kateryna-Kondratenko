def findposition(sortedlist, nelement):
    left, right = 0, len(sortedlist)
    
    while left < right:
        mid = (left + right) // 2
        if sortedlist[mid] < nelement:
            left = mid + 1
        else:
            right = mid
    
    return left 

sortedlist = [1, 2, 4, 6, 8]
nelement = 5
position = findposition(sortedlist, nelement)
print(f"Елемент {nelement} слід вставити на позицію {position}")