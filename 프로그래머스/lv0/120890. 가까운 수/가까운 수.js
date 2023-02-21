function solution(array, n) {
    let sorted = array.sort((a,b) => a - b);
    sorted = sorted.map(el => el - n > 0 ? el - n : -(el - n));
    const idx = sorted.indexOf(Math.min(...sorted));
    
    return array[idx];
}