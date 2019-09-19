
// @param {number[][]} matrix
// @return {number[]}

var spiralOrder = function (matrix) {
    if (!matrix.length) return []
    result = []
    while (true) {
        try {
            //      right: take off first arr
            result = result.concat(matrix.shift())

            //      down
            matrix.forEach(sub => {
                result.push(sub.pop())
            })
            matrix = cleanUp(matrix)

            //      left: take off last arr    
            while (matrix[matrix.length - 1].length > 0) {
                result.push(matrix[matrix.length - 1].pop())
            }

            //      up    
            let i = matrix.length - 1
            while (i >= 0) {
                result.push(matrix[i].shift())
                i--
            }

        }

        catch (e) {
            result = result.filter(el => typeof el !== 'undefined')
            return result
        }
    }
    result = result.filter(el => el)
    return result

};

function cleanUp(matrix) {
    return matrix.filter(el => el.length)
}


