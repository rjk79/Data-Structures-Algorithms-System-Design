var evalRPN = function (tokens) {
    if (tokens.length === 1) return parseInt(tokens[0])

    let otherNum;
    let nonStr;

    res = null
    stack = []

    tokens.forEach(token => {
        debugger
        nonStr = parseInt(token)
        if (!isNaN(nonStr)) {
            stack.push(nonStr)
        } else {
            otherNum = stack.pop()
            switch (token) {
                case "+":
                    if (!res) res = stack.pop()

                    res += otherNum
                    break
                case "-":
                    if (!res) {
                        res = stack.pop()
                        res -= otherNum
                    } else {
                        res = otherNum - res
                    }

                    break
                case "*":
                    if (!res) res = stack.pop()

                    res *= otherNum
                    break
                case "/":
                    if (!res) {
                        res = stack.pop()
                        res = (res / otherNum)
                    } else {
                        res = (otherNum / res)
                    }
                    // console.log(res)
                    break
            }
        }
    })

    return res
}

//  use a stack, iter thru tokens
//  push into stack if its an "int" else, 
//    run it into a switch statem
//        change your current result
//    if it is the first time you are changing your result AKA
//    if changing from nil then take first TWO elems from Stack
//    else take 1st el and do: firstEl ${symbol} currRes

console.log(evalRPN(["2", "1", "+", "3", "*"]))
// 9
console.log(evalRPN(["4", "13", "5", "/", "+"]))
// 6
console.log(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
// 22