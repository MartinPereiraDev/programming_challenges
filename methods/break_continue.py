
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass
    else:
        print(i)