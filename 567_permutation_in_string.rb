require 'byebug'
# def check_inclusion(s1, s2)
#     curr = s1[0]
#     currIdx = s2.index(curr)
#     if currIdx 
#         return recur(s1, s2, currIdx - 1, currIdx + 1)
#     else 
#         return false
#     end
# end

# def recur(s1, s2, prevIdx, nextIdx)
#     return true if s1.length == 0
#     debugger
#     curr = s1[0]
#     if s2[prevIdx] && s2[prevIdx] == curr
#         prevIdx = prevIdx > 0 ? prevIdx - 1 : -Float::INFINITY
#         recur(s1[1..-1], s2, prevIdx, nextIdx)
#     elsif s2[nextIdx] && s2[nextIdx] == curr
#         nextIdx = nextIdx < s2.length - 1 ? nextIdx + 1 : Float::INFINITY
#         recur(s1[1..-1], s2, prevIdx, nextIdx)
#     else 
#         return false
#     end
# end

check_inclusion("ab","eidbaooo")