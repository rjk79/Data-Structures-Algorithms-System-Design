# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    return true if s == ""
    
   word_dict.each {|word| 
       if s.include?(word)
        puts word
         idx = s.index(word)
         if word_break(s[0...idx], word_dict) && word_break(s[idx+word.length..-1], word_dict) 
             return true
         end
        
       end
    } 
#   never triggered "if" so no word is included
    return false
end


# for each word it contains, return wordBreak(s[0...idx start of word]) &&
# wordBreak(s[idx end of word...-1]) || next iter

# return true if empty string
# return false if no matches

puts( word_break("cars", ["car", "ca", "rs"]) )

