function solution(my_str, n) {
  let result = [];
  for (let i = 0; i < Math.ceil(my_str.length / n); i++) {
    let idx = n * i;
    result.push(my_str.slice(idx, idx+n))
  }
  return result;
}