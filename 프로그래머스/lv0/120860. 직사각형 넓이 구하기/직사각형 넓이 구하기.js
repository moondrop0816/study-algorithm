function solution(dots) {
  let x = dots.map(el => el[0]);
  let y = dots.map(el => el[1]);

  return (Math.max(...x) - Math.min(...x)) * (Math.max(...y) - Math.min(...y))
}