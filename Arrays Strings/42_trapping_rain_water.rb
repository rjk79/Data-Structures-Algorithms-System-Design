

# def trap(height)
#     # peaks = []
#     prevPeak = nil
#     valleys = []
#     water = 0
   
#     i = 0
#     while i < height.length 
# #       ternaries take care of edges
#         prev = (i != 0) ? height[i - 1] : 0
#         curr = height[i]
#         third = (i != height.length - 1) ? height[i + 1] : 0
# #       if its a peak:
#         if curr >= prev && curr >= third
# #           if we're past the 1st peak 
#             if prevPeak
#                 min = [prevPeak, height[i]].min
#                 valleys.each{|valley|
#                     water += min - valley if valley < min
#                 }
#                 valleys = []
#             end
#             prevPeak = height[i]
# #       if its a valley and we're past the 1st peak
#         elsif prevPeak
#             valleys << height[i]
#         end
#         i += 1
#     end
#     water
# end

# # peak means greater than the things around it
# # if 0th or last idx, then voids dont matter