
function change(amount, coins, memo = {}) {
    let key = amount + "-" + coins
    if (key in memo) return memo[key]

    if (amount === 0) return 1

    let currentCoin = coins[coins.length - 1]
    let total = 0
    for (let qty = 0; currentCoin * qty <= amount; qty++) {
        total += change(amount - currentCoin * qty, coins.slice(0, -1), memo)
    }
    memo[key] = total
    return memo[key]

}