function solution(my_string, m, c) {
    let result = '';
    let idx = c - 1;
    
    while (idx <= my_string.length - 1) {
        result += my_string[idx];
        idx += m;
    }
    
    return result;
}