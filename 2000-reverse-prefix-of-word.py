class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def reverse(s):
            left, right = 0, len(s) - 1
            s = list(s)

            while left <= right:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                left += 1
                right -= 1

            return ''.join(s)

        index = word.find(ch)
        return reverse(word[0:index + 1]) + word[index+1:]


if __name__ == "__main__":
    sol = Solution()
    word = "abcdefd"
    ch = "d"
    ans = sol.reversePrefix(word, ch)
    print(ans)
