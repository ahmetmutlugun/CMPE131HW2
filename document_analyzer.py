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

sorted_dict = dict(sorted(frequency_dict.items(), key=lambda _:_[1])[::-1])

for i in list(sorted_dict.items())[:5]:
    print(f"{i[0]}: {sorted_dict.get(i[0])}")