function solution(num_list) {
    return Number(num_list.filter(el=> el % 2 === 1).join('')) + Number(num_list.filter(el=> el % 2 === 0).join(''))
}