tableData = [['apples', 'oranges', 'cherries', 'banana'],              
    ['Alice', 'Bob', 'Carol', 'David'],              
    ['dogs', 'cats', 'moose', 'goose']]

for j in range(0,4):
    for i in tableData:
        string = i[j].rjust(9)
        print(string, end=' ')
    print("\n")
