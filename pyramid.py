import sys
def weight_on(row, column):
    second_person = 200
    if column - 1 < 0 or column > row - 1 :
        second_person = 0
    if column < 0 or column > row:
        return 0.0
    if row <= 0:
        return 0.0
    return (second_person + 200 + (weight_on(row - 1, column - 1) + weight_on(row - 1, column))) / 2

def main():
    # print(weight_on(3, 1))
    argument = int(sys.argv[1])
    if (len(sys.argv) <= 1):
        raise IndexError("Please enter a valid argument")
        
    for i in range(argument):
        for j in range(i + 1):
            print(f"{weight_on(i, j):.2f}", end=' ')
        print('')
if __name__ == '__main__':
    main()
    