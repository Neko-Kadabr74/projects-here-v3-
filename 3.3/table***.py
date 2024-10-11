n = int(input("enter de number...  ") )

for i in range(11):
    row = [i * j for j in range(11)]
    print(f"Table {i}: {' '.join(map(str, row))}")