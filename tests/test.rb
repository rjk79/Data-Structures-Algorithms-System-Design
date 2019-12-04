def myflatten(arr) 
    return arr.map{|el| el.kind_of?(Array) ? myflatten(el): el}
end

print flatten([[1, 2], [3, 4, 5, [6, 7]]])

# [ [] ]