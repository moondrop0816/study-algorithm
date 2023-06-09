function solution(num_list) {
    const result = num_list[num_list.length-1] > num_list[num_list.length-2] ? num_list[num_list.length-1] - num_list[num_list.length-2] : num_list[num_list.length-1] * 2;
    
    num_list.push(result)
    
    return num_list
}