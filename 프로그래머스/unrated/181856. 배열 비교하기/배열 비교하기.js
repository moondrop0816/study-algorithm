function solution(arr1, arr2) {
    const len1 = arr1.length;
    const len2 = arr2.length;
    
    if (len1 > len2) {
        return 1
    } else if (len1 < len2) {
        return -1
    } else {
        const sum1 = arr1.reduce((acc, cur)=> acc + cur)
        const sum2 = arr2.reduce((acc, cur)=> acc + cur)

        if (sum1 === sum2) return 0
        if (sum1 > sum2) {
            return 1
        } else {
            return -1
        }    
    }
    
    
}