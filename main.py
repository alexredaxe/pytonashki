from random import shuffle


def mat(n):
    shuffle(n)
    return n


def getArrIndex(fArray, fElem: str) -> (int, int):
    # print("fArray begin")
    # print(fArray)
    # print("len = ", len(fArray))
    # print("fElem =", fElem)
    # print("fArray end")
    for i in range(len(fArray)):
        for j in range(len(fArray[i])):
            if fArray[i][j] == fElem:
                # print(f"Index of [{fElem}] is [{i}, {j}]")
                return i, j
    else:
        return None


pArray = [
    ["01", "02", "03", "04"],
    ["05", "06", "07", "08"],
    ["09", "10", "11", "12"],
    ["13", "14", "15", "__"]
]

pArrayOriginal=pArray[:]

pArray = mat(pArray)

while True:

    for i in range(len(pArray)):
        for j in range(len(pArray[i])):
            print(pArray[i][j], end=" ")
        print()
    if pArray==pArrayOriginal:
        print("Вы выиграли. Игра закончена")
        break
    sym = input("Введите номер фишки или exit:")
    if sym.upper() == "EXIT":
        print("Выход из игры")
        break
    elif not sym.isdigit():
        print("Это не число. Попробуйте еще раз")
    elif (int(sym) < 1) or (int(sym) > 15):
        print("Вне диапазона. Попробуйте еще раз")
    else:
        if 0 < int(sym) < 10:
            sym = "0" + sym
        row, col = getArrIndex(fArray=pArray, fElem=sym)
        #print(row, col)
        if (3 >= row >= 0) and (3 >= col >= 0):
            if row == 0:
                row_prev = 0
                row_next = row + 1
            elif row == 3:
                row_prev = row - 1
                row_next = 3
            else:
                row_prev = row - 1
                row_next = row + 1

            if col == 0:
                col_prev = 0
                col_next = col + 1
            elif col == 3:
                col_prev = col - 1
                col_next = 3
            else:
                col_prev = col - 1
                col_next = col + 1

            if pArray[row_prev][col] == "__":
                pArray[row_prev][col] = pArray[row][col]
                pArray[row][col] = "__"
            elif pArray[row_next][col] == "__":
                pArray[row_next][col] = pArray[row][col]
                pArray[row][col] = "__"
            elif pArray[row][col_next] == "__":
                pArray[row][col_next] = pArray[row][col]
                pArray[row][col] = "__"
            elif pArray[row][col_prev] == "__":
                pArray[row][col_prev] = pArray[row][col]
                pArray[row][col] = "__"
            else:
                print("Некорректный номер фишки")
