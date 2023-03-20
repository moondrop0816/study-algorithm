function solution(a, b) {
    let temp = [];

  for (let i = 2; i < (a > b ? a : b); i++) {
    if (a % i === 0 && b % i === 0) {
      temp.push(i);
    }
  }

  if (temp.length !== 0) {
    let big = Math.max(...temp);
    a /= big;
    b /= big;
  } 

  for (let i = 2; i <= b; i++) {
    if (b % i === 0 && i % 2 !==0 && i % 5 !== 0) {
      return 2;
    }
  }

  return 1;
}