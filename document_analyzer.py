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

sorted_dict = dict(sorted(frequency_dict.items(), key=lambda _: _[1])[::-1])  # Sort by keys and then reverse

sorted_list = list(frequency_dict.items())
for i in range(len(sorted_list)):
    for j in range(len(sorted_list) - i - 1):
        if sorted_list[j][1] < sorted_list[j+1][1]:
            a = sorted_list[j]
            sorted_list[j] = sorted_list[j + 1]
            sorted_list[j + 1] = a
        if sorted_list[j][1] == sorted_list[j + 1][1]:
            if sorted_list[j][0] > sorted_list[j + 1][0]:
                a = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = a

print()
for i in range(0, 5):
    print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")
