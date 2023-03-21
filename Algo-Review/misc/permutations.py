def swap(word, i, j):
    word = list(word)
    word[i], word[j] = word[j], word[i]
    return ''.join(word)

def find_perms(word, cur_index, result):
    # base case
    if cur_index == len(word) - 1:
        result.append(word)
        return

    # recursive case
    for i in range(cur_index, len(word)):
        swapped_str = swap(word, cur_index, i)
        find_perms(swapped_str, cur_index + 1, result)

def permute(word):
    result = []
    find_perms(word, 0, result)
    return result

def main():
    word = "abc"
    permutations = permute(word)
    print(permutations)

main()
