function solution(num_list) {
    const odd = num_list.filter((el, idx)=> idx % 2 === 1 ? el : 0).reduce((acc, cur)=> acc + cur)
    const even = num_list.filter((el, idx)=> idx % 2 === 0 ? el : 0).reduce((acc, cur)=> acc + cur)
    
    return odd >= even ? odd : even
}