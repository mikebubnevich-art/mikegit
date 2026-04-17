import sys

def find_partitions(n, max_part, current, result):
    if n == 0:
        result.append(current[:])
        return
    for part in range(min(max_part, n), 0, -1):
        current.append(part)
        find_partitions(n - part, part, current, result)
        current.pop()

def main():
    n = int(sys.argv[1])
    result = []
    find_partitions(n, n, [], result)
    result.reverse()
    print(len(result))
    print(result)

if __name__ == "__main__":
    main()