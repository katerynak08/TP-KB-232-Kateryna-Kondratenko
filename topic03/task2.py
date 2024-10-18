def testfunct():
    tlist = [6, 3, 9, 4, 2]
    print(f"Початковий список: {tlist}")

    tlist.append(7)
    print(f"Після append(7): {tlist}")

    tlist.extend([5, 10])
    print(f"Після extend([5, 10]): {tlist}")

    tlist.insert(3, 8) 
    print(f"Після insert(3, 8): {tlist}")

    tlist.remove(9) 
    print(f"Після remove(9): {tlist}")

    tlist.sort()
    print(f"Після sort: {tlist}")

    tlist.reverse()
    print(f"Після reverse: {tlist}")

    coplist = tlist.copy()
    print(f"Копія списку: {coplist}")

    tlist.clear()
    print(f"Після clear: {tlist}")

testfunct()
