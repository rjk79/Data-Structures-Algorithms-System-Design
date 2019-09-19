// implement yourself



// 1..n 
// so n is number of nodes u need to place

// n = 1
// recurse  leftNums = 0, rightNums = 0, output = ( 1 * 1 )+= 1

// n = 2
// recurse leftNums = 0, rightNums = 1, output += 1
// recurse leftNums = 1, rightNums = 0, output += 1

// n = 3
// recurse leftNums = 0, rightNums = 2, output += 2
// recurse leftNums = 1, rightNums = 1, output += 1
// recurse leftNums = 2, rightNums = 0, output += 2

// growing n doesnt just change # of iterations, it also changes what those iterations are

var numTrees = (n) => {
    if (n <= 1) { return 1; }
    let output = 0;

	// recursive fn that calcs the # of unique binary tree arrangements with n numbers and index i as the head
    const recurse = (i, n) => {
// the thing at i is the root so basically the partition
        const leftNums = i - 1;
        // num of nodes on left side (1 is being used for the root of the subtree)
        const rightNums = n - i; 
        // num of nodes on right side

		// treat the numbers to the left and right of i each as their own binary tree
		// get the # of unique arrangements of the left tree and right tree
        const leftTrees = numTrees(leftNums);
        const rightTrees = numTrees(rightNums);
        
		// Total arrangements = unique arrangements of left tree x unique arrangements of right tree
		// add product to the output
        output += leftTrees * rightTrees;
    };

    // repeat function treating every index as a potential head of the tree
// so when n = 6, i = 3 => (1, 2) = left subtree, (3) = root, (4, 5, 6) = right subtree
    for (let i = 1; i <= n; i += 1) { recurse(i, n); }

    return output;
};


// INVALID SOLN
// does not work because: if you have 5 things
// it will only find rearrangements of the bottom tree but not try to place it on either side
//   / \
//     / \


// var numTrees = (n) => {
//     if (n === 1) return 1
//     if (n === 1) return 0 

//     let count = 0
//     // left only, right only, both
//     count += 1 + numTrees(n - 1)
//     count += 1 + numTrees(n - 1)
//     count += 1 + numTrees(n - 2)

//     return count
// }
