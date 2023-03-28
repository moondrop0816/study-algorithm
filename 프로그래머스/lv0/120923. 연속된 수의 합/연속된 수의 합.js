function solution(num, total) {
    const mid = Math.floor(total/num);
  const midIdx = Math.floor(num/2);

  const result = [mid];

  for (let i = 0; i < num; i++) {
    if (i < midIdx) {
      result.unshift(result[0] - 1);
    } else if (i > midIdx) {
      result.push(result[result.length-1] + 1)
    }
  }

  let sum = result.reduce((acc, cur)=> acc += cur);

  if (sum !== total) {
    result.shift();
    result.push(result[result.length-1]+1)
  }

  return result;
}