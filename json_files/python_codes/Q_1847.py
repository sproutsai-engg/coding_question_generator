##Question ID: 1847


```javascript
function closestRoom(rooms, queries) {
    rooms.sort((a, b) => b[1] - a[1]);
    
    for (let i = 0; i < queries.length; ++i) {
        queries[i].push(i);
    }
    
    queries.sort((a, b) => b[1] - a[1]);
    
    let result = new Array(queries.length);
    let ids = new Set();
    
    let j = 0;
    for (const q of queries) {
        while (j < rooms.length && rooms[j][1] >= q[1]) {
            ids.add(rooms[j++][0]);
        }
        if (ids.size === 0) {
            result[q[2]] = -1;
        } else {
            let minAbsDiff = Infinity;
            let minId = undefined;
            for (let id = q[0]; id <= 10000000; ++id) {
                if (ids.has(id) && Math.abs(id-q[0]) < minAbsDiff) {
                    minAbsDiff = Math.abs(id - q[0]);
                    minId = id;
                }
                if (ids.has(id-1) && Math.abs(id-1-q[0]) < minAbsDiff) {
                    minAbsDiff = Math.abs(id - 1 - q[0]);
                    minId = id - 1;
                }
                if (minId !== undefined)
                    break;
            }
            result[q[2]] = minId;
        }
    }
    
    return result;
}
```


## Structure

    # Your code here

    pass