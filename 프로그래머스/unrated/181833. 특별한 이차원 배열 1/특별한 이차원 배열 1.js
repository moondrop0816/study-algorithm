function solution(n) {
    const arr = [];
    for (let i = 0; i < n; i++) {
        arr.push([])
        for (let j = 0; j < n; j++) {
            arr[i].push(i === j ? 1 : 0)
        }
    }
    return arr
}