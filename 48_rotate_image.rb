def rotateImage(matrix)
    matrix.transpose.map!{|el| el.reverse}
end

# print rotateImage([
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ])