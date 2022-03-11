f = open("document.txt", "r")
file = f.read()
f.close()

words = file.split(" ")
frequency_dict = {}

for i in words:
    if frequency_dict.get(i) is not None:
        frequency_dict.update({i: frequency_dict.get(i) + 1})
    else:
        frequency_dict.update({i: 1})

sorted_dict = dict(sorted(frequency_dict.items(), key=lambda _: _[1])[::-1])
print()

arr = list(sorted_dict.items())
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        # print(arr[j][0])
        if frequency_dict.get(arr[j][0]) == frequency_dict.get(arr[j + 1][0]):
            a = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = a

for i in range(0, 5):
    print(f"{arr[i][0]}: {arr[i][1]}")
