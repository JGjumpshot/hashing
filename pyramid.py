import sys
def weight_on(row, column):
    second_person = 200 #finds out if there is a second person on top or not
    if column - 1 < 0 or column > row - 1 :
        second_person = 0
    if column < 0 or column > row:
        return 0.0
    if row <= 0:
        return 0.0
    return (second_person + 200 + (weight_on(row - 1, column - 1) + weight_on(row - 1, column))) / 2

def main():
    argument = sys.argv[1]
    if (len(sys.argv) <= 1):
        raise IndexError("Please enter a valid argument")
        
    for i in range(int(argument)):
        for j in range(i):
            print(f"{weight_on(i, i):.2f}", end=' ')
            # print(i, end=' ')
        print(f'{i}')
if __name__ == '__main__':
    main()
    