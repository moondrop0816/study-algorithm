function solution(arr, queries) {
    const result = []
    for (query of queries) {
        const [s, e, k] = query
        const value = arr.filter((el, idx)=> idx >= s && idx <= e && el > k)
        value.sort((a, b)=> a - b)
        result.push(value[0] ? value[0] : -1)
    }
    return result
}