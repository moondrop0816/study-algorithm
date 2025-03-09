function solution(s) {
  if (s.length % 2 === 0) {
    return s.slice(Math.round(s.length / 2)-1, Math.round(s.length / 2)+1)
  } else {
    return s[Math.round(s.length / 2)-1]
  }
}