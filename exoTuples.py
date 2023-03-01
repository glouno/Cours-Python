data = [("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]
sortedData = []

for element in data:
    print(element)
    print(element[0])
    for nElement in sortedData:
        print("test")
        sortedData.append(element)


print("sortedData: ", sortedData)