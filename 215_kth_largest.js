// heap reduces time complex for large arrays

var findKthLargest = function (nums, k) {
    let heap = new MaxHeap()
    for (let i = 0; i < nums.length; i++) {
        heap.insert(nums[i])
    }
    for (let j = 0; j < k - 1; j++) {
        heap.deleteMax()
    }
    return heap.array[1]
};
// or add them in one at a time and then siftUp/Down for Each
// then return the length - 1 - (k - 1)

class MaxHeap {
    constructor() {
        this.array = [null]
    }

    getParent(idx) {
        return Math.floor(idx / 2)
    }
    getLeftChild(idx) {
        return idx * 2
    }
    getRightChild(idx) {
        return idx * 2 + 1
    }
    insert(val) {
        this.array.push(val)
        let currIdx = this.array.length - 1

        this.siftUp(currIdx)
        // console.log(this.array)

    }
    siftUp(idx) {
        let currIdx = idx
        while (this.getParent(currIdx) && this.array[currIdx] > this.array[this.getParent(currIdx)]) {

            [this.array[currIdx], this.array[this.getParent(currIdx)]] = [this.array[this.getParent(currIdx)], this.array[currIdx]]
            // becomes parent idx
            currIdx = this.getParent(currIdx)
        }
        return
    }
    siftDown(idx) {
        let arr = this.array
        let currVal = arr[idx]
        let leftIdx = this.getLeftChild(idx)
        let rightIdx = this.getRightChild(idx)

        let leftVal = arr[leftIdx]
        let rightVal = arr[rightIdx]
        let swapIdx = idx

        if (!leftVal) leftVal = -Infinity
        if (!rightVal) rightVal = -Infinity

        if (currVal >= rightVal && currVal >= leftVal) return

        if (leftVal < rightVal) { swapIdx = rightIdx }
        else { swapIdx = leftIdx }

        [arr[idx], arr[swapIdx]] = [arr[swapIdx], arr[idx]]
        this.siftDown(swapIdx)
    }

    deleteMax() {
        // dont check for length 0 since we start with null
        if (this.array.length === 1) return null
        if (this.array.length === 2) return this.array.pop()
        // set the last thing to be the first thing
        let max = this.array[1]
        this.array[1] = this.array.pop()
        this.siftDown(1)
        return max
    }
}