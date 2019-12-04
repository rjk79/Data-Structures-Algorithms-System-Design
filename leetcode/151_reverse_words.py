def reverseWords(s):
        words = []
        l = 0
        while l < len(s):
            r = l + 1
            while r < len(s) and s[r] != " ":
                r += 1
            words.append(s[l:r])
            
            l = r
            while l < len(s) and s[l] == " ":
                l += 1
        return " ".join(words[::-1]).rstrip(" ").lstrip(" ")
print(reverseWords("  hello world!  "))