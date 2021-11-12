def weight_on(row, column):
    if row <= 0:
        return 0
    if column <= 0 or column > row:
        return 0
    return 100 + (weight_on(row - 1, column - 1) + weight_on(row - 1, column)) / 2

def main():
    print(weight_on(3, 2))

if __name__ == '__main__':
    main()
    