function solution(n) {
  let num = 0;
  while (n % num !== 1) {
    num += 1
  }
  return num;
}