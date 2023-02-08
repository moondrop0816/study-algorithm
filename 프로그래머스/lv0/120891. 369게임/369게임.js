function solution(order) {
    return String(order).split('').filter((el)=>Number(el) % 3 === 0 && Number(el) !== 0).length;
}