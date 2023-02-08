function solution(num, k) {
    const idx = num.toString().split('').findIndex((el)=> Number(el) === k);
    
    return idx !== -1 ? idx + 1 : idx
}