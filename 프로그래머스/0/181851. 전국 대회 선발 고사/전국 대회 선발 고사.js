function solution(rank, attendance) {
  const chosen = []
  let num = 1
  while (chosen.length < 3) {
    const idx = rank.indexOf(num)
    if (attendance[idx]) chosen.push(idx) 
    num += 1
  }
  return 10000 * chosen[0] + 100 * chosen[1] + chosen[2]
}