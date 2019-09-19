var preorder = function (root) {
    let others;
    //     edge case
    if (!root) {
        return []
    }
    // no children  
    else if (!root.children.length) { return [root.val] }
    //children
    else {
        others = [root.val]
        root.children.forEach(child => {
            others = others.concat(preorder(child))
        })
        return others

    }
};