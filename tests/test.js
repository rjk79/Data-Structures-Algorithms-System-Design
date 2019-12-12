// function dijkstras(graph, source) {
//     let distance = {};
//     for (let node in graph) {
//         distance[node] = Infinity;
//     }
//     distance[source] = 0;

//     let unvisited = new Set(Object.keys(graph));
//     let previous = {};

//     while (unvisited.size > 0) {
//         let currNode = minDistanceNode(unvisited, distance);
//         unvisited.delete(currNode);

//         for (let neighbor in graph[currNode]) {
//             let distanceFromCurrToNeighbor = graph[currNode][neighbor];
//             let totalNeighborDistance = distance[currNode] + distanceFromCurrToNeighbor;

//             if (distance[neighbor] > totalNeighborDistance) {
//                 distance[neighbor] = totalNeighborDistance;
//                 previous[neighbor] = currNode;
//             }
//         }
//     }

//     return { distance, previous };
// }

// function minDistanceNode(nodes, distance) {
//     return Array.from(nodes).reduce((minNode, node) => (
//         distance[node] < distance[minNode] ? node : minNode
//     ));
// }

// let graph = {
//     'a': { 'c': 1, 'b': 7 },
//     'b': { 'a': 7, 'd': 12, 'e': 13 },
//     'c': { 'a': 1, 'd': 20, 'f': 4 },
//     'd': { 'b': 12, 'c': 20, 'e': 5 },
//     'e': { 'b': 13, 'd': 5, 'f': 9 },
//     'f': { 'c': 4, 'e': 9 }
// };

// let { distance, previous } = dijkstras(graph, 'a');

// console.log(distance);
// console.log(previous);

// let a = [1, 2, 3]

// console.log (a.reduce((acc, el)=> el + acc) )

async function f() {
    // let promise1 = new Promise((resolve, reject) => {
    //     setTimeout(() => resolve("value"),  3000)
    // })
    let promise1 = () => {setTimeout(() => res = "value", 3000)}
    let res = await promise1()
    console.log(res)
}

// f()

function summer(arg1){
    if (arguments.length === 2) return arguments[0] + arguments[1]
    return (arg2) => {
        return arg1 + arg2
    }
}

console.log(summer(1, 2))
console.log(summer(1)(2))