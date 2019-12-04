require "byebug"

# permutations
# nested loop
# prev.each
#   nextChars.each
def letter_combinations(digits)
    pad = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t','u','v'],
        "9": ['w','x','y','z'],
        }  
    return [""] if digits == ""
    res =[]
    possibilities = pad[digits[0].to_sym]
    letter_combinations(digits[1..-1]).each {|nextChar|
         possibilities.each{|poss|
            res <<  poss + nextChar
            }
        }
       
    
    
    return res
end

puts letter_combinations("23")