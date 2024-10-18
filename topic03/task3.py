def testfunct():
    tdict = {'name': 'Katya', 'age': 18}
    print(f"Початковий словник: {tdict}")

    tdict.update({'age': 28, 'surname': 'Kondratenko'})
    print(f"Після update: {tdict}")

    del tdict['age']
    print(f"Після del tlist['age']: {tdict}")

    tdict.clear()
    print(f"Після clear(): {tdict}")

    tdict = {'name': 'Katya', 'surname': 'Kondratenko'}
    print(f"Відновлений словник: {tdict}")

    print(f"Ключі словника: {list(tdict.keys())}")

    print(f"Значення словника: {list(tdict.values())}")

    print(f"Пари ключ-значення словника: {list(tdict.items())}")

testfunct()
