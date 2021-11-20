"""module doc-string"""
import sys
import time
FUNCTION_COUNTER = 0
cache = {}
CACHE_COUNTER = 0
def weight_on(row, column):
    """weight on function"""
    global FUNCTION_COUNTER
    global cache
    global CACHE_COUNTER
    FUNCTION_COUNTER += 1
    second_person = 200
    key = (row, column)
    if key in cache:
        CACHE_COUNTER += 1
        return cache[key]
    if column == 0 and row == 0:
        cache[key] = 0
        return 0
    if column == 0:
        cache[key] = second_person / 2 + weight_on(row - 1, 0) / 2
        return second_person / 2 + weight_on(row - 1, 0) / 2
    if column == row:
        cache[key] = second_person / 2 + weight_on(row - 1, column - 1) / 2
        return second_person / 2 + weight_on(row - 1, column - 1) / 2
    cache[key] = (second_person + (weight_on(row - 1, column - 1) / 2 + weight_on(row - 1, column) / 2))
    return (second_person + (weight_on(row - 1, column - 1) / 2 + weight_on(row - 1, column) / 2))

def main():
    """main function"""
    argument = int(sys.argv[1])
    with open("part2.txt", 'w', encoding="utf-8") as file:
        if len(sys.argv) <= 1:
            raise IndexError("Please enter a valid argument")
        start_time = time.perf_counter()
        for i in range(argument):
            for j in range(i + 1):
                print(f"{weight_on(i, j):.2f}", end=' ')
                # file.write(f"{weight_on(i, j):.2f}")
            print('')
        end_time = time.perf_counter()
        print(f"Number of function calls: {FUNCTION_COUNTER}")
        file.write(f"Number of function calls: {FUNCTION_COUNTER}\n")
        print(f"Elapsed time: {end_time - start_time}")
        file.write(f"Elapsed time: {end_time - start_time}\n")
        print(f"Cache hits: {CACHE_COUNTER}")
        file.write(f"Cache hits: {CACHE_COUNTER}\n")
    file.close()
if __name__ == '__main__':
    main()
    