var canFinish = function (numCourses, prerequisites) {
    let graph = createGraph(prerequisites)
    let courses = Object.keys(graph)
    let finished = new Set()

    let eligibleCourses = true
    while (eligibleCourses) {
        eligibleCourses = false
        courses.forEach(course => {
            if (graph[course].every(prereq => finished.has(prereq)) && !finished.has(parseInt(course))) {
                finished.add(parseInt(course))
                eligibleCourses = true
            }
        })
    }
    return finished.size === courses.length
};

// iterate thru the courses, 
// if you havent finished one and you have all the prereqs done
// then add it to your list of finished and iter thru the courses again


var createGraph = function (list) {
    let graph = {}
    list.forEach(edge => {
        if (!(edge[0] in graph)) {
            graph[edge[0]] = [edge[1]]
        } else {
            graph[edge[0]].push(edge[1])
        }
        if (!(edge[1] in graph)) graph[edge[1]] = []
    })
    return graph
}