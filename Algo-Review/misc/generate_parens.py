# Time: O(4^n) -- see Grokking on how this is derived
# Space: O(2n), plus space of call stack
def generate_combinations(n):
    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return

        if left < n:
            dfs(left + 1, right, s + '(')

        if right < left:
            dfs(left, right + 1, s + ')')

    res = []
    dfs(0, 0, '')
    return res

def main():
    n = 3
    res = generate_combinations(n)
    print(res)

main()
