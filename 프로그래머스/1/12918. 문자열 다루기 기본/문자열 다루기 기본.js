function solution(s) {
  if (s.length === 4 || s.length === 6) {
    return /^[0-9]+$/g.test(s)
  } 

  return false
}