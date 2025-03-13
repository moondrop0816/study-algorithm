function solution(d, budget) {
  let result = 0;
  d.sort((a, b)=>a-b)
  while (budget >= d[0]) {
    budget -= d[0];
    result += 1;
    d.shift();
  }
  return result;
}