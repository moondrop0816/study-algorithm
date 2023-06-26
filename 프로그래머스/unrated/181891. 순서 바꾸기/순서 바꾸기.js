function solution(num_list, n) {
    const arr = num_list.slice(0, n)
    return num_list.slice(n).concat(arr)
}