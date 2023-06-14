function solution(num_list, n) {
    return num_list.findIndex(el => el === n) !== -1 ? 1 : 0
}