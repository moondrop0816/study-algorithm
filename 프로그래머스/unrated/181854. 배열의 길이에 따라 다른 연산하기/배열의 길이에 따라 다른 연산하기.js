function solution(arr, n) {
    return arr.map((el, idx) => {
        if (arr.length % 2 === 1) {
            if (idx % 2 === 0)  return el + n
        } else {
            if (idx % 2 === 1) return el + n
        }
        
        return el
    })
}