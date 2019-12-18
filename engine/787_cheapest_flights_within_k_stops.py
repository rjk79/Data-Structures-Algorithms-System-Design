# n = # of cities
# m flights [ [start, end, price],  ]
# src
# dst = destination
# k # of stops

# {
#     src: [ [dest, price], [dest, price] ]
# }

# [[0, src, k + 1 ], ]

# price, city, stops

# var findCheapestPrice = function(n, flights, src, dst, K) {
#     let map = new Map();
    
#     for (let i = 0; i < flights.length; i++) {
#         const [start, end, price] = flights[i];
#         let edges = map.get(start) || [];
#         edges.push([end, price]);
#         map.set(start, edges);
#     }
    
#     let queue = [[0, src, K + 1]];
    
#     while (queue.length) {
#         const [price, city, stops] = queue.shift();
#         if (city === dst) return price;
    # if you've stopped too many times => stops < 0 and we'll do nothing after we shift it off
#         if (stops > 0) {
#             const nextFlights = map.get(city) || [];
#             for (let i = 0; i < nextFlights.length; i++) {
#                 const [next, cost] = nextFlights[i];
#                 queue.push([cost + price, next, stops - 1]);
#             }
    # sort the q after every shift, thus favoring shorter routes (lower price)
#             queue.sort((a, b) => a[0] - b[0]);
#         }
#     }
    
#     return -1;
# };