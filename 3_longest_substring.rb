def length_of_longest_substring(s)
    return 0 if s.length == 0 
    longest = ""
    i = 0
    while i < s.length 
        current = s[i]
        j = i + 1

        while j < s.length 
            if current.include?(s[j]) 
                break
            else 
                current += s[j]
            end
            j += 1
        end
        longest = current if current.length > longest.length
        i += 1
    end
    longest.length
end