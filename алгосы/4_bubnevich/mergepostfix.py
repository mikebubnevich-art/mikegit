import sys

def common_suffix(s1, s2):
    i = 1
    while i <= len(s1) and i <= len(s2) and s1[-i] == s2[-i]:
        i += 1
    return s1[-(i-1):] if i > 1 else ""

def longest_common_suffix(words, left, right):
    if left == right:
        return words[left]
    mid = (left + right) // 2
    left_suffix = longest_common_suffix(words, left, mid)
    right_suffix = longest_common_suffix(words, mid + 1, right)
    return common_suffix(left_suffix, right_suffix)

def main():
    if len(sys.argv) < 2:
        return
    
    words = sys.argv[1].split()
    
    if not words:
        print(0)
        return
    
    if len(words) == 1:
        print(len(words[0]))
        return
    
    result = longest_common_suffix(words, 0, len(words) - 1)
    print(len(result))

if __name__ == "__main__":
    main()