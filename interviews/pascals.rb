def pascal_row(row_index)
    return [1] if row_index == 0
    prev = pascal_row(row_index - 1)
    new = [1]
    i = 0
    while i < prev.length - 1
        new.push(prev[i] + prev[i + 1])
        i += 1
    end
    new.push(1)
    return new
end

# puts pascal_row(0)
# print pascal_row(1)
# print pascal_row(2)


