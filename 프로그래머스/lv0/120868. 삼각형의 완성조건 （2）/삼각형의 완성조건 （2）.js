function solution(sides) {
    sides.sort((a,b) => b - a);

  return (sides[0] + sides[1] - 1) - (sides[0] - sides[1] + 1) + 1
}