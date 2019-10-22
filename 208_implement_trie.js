class Node {
    constructor() {
        this.children = {};
        this.isTerminal = false;
    }
}

class Trie {
    constructor() {
        this.root = new Node()
    }
    insert(word, root = this.root) {
        if (word === "") {
            root.isTerminal = true
            return
        }
        if (!Object.keys(root.children).includes(word[0])) {
            root.children[word[0]] = new Node()
        }
        this.insert(word.slice(1), root.children[word[0]])
    }

    search(word, root = this.root) {
        // if we've traversed all the way, hopefully its terminal
        if (word === "") return root.isTerminal
        if (Object.keys(root.children).includes(word[0])) {
            return this.search(word.slice(1), root.children[word[0]])
        } else {
            return false
        }
    }

    // just like 'search' except return true if found
    startsWith(word, root = this.root) {
        if (word === "") return true
        if (Object.keys(root.children).includes(word[0])) {
            return this.startsWith(word.slice(1), root.children[word[0]])
        } else {
            return false
        }
    }
}
// take the word and iter until you're sure you have the whole word
// then make recursive calls to find all the permutations