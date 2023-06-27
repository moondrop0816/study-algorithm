function solution(my_string) {
    const arr = []
    
    const strFn = (str, arr) => {
        if (str.length === 0) return;
        arr.push(str)
        return strFn(str.slice(1), arr)
    }
    
    strFn(my_string, arr)
    
    return arr.sort()
}