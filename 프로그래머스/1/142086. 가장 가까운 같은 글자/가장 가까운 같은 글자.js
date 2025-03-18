function solution(s) {
  const obj = {}
  const result = []
  for (let i = 0; i < s.length; i++) {
    if (s[i] in obj === false) {
      result.push(-1);
    } else {
      result.push(i - obj[s[i]])
    }
    obj[s[i]] = i;
  }
  return result
}