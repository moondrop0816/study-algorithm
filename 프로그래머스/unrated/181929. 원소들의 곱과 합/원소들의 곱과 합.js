function solution(num_list) {
    const multiply = num_list.reduce((acc, cur) => acc * cur);
    const squre = Math.pow(num_list.reduce((acc, cur)=> acc + cur), 2);
    
    return multiply < squre ? 1 : 0
}