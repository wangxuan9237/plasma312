dict_book = {}
with open("bookdata","r") as f:
    for line in bookdata:
        dict_book[line.split()[0]] = line.split()[2]

