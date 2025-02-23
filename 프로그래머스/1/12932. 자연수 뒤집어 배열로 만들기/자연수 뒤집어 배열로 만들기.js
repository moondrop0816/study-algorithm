function solution(n) {
  const arr = [];
  n.toString().split('').map((el)=>arr.unshift(Number(el)));
  return arr
}