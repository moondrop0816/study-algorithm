function solution(ineq, eq, n, m) {
  let result = true
  switch (ineq+eq) {
    case '<=' : 
      result = n <= m;
      break;
    case '<!' : 
      result = n < m;
      break;
    case '>=' : 
      result = n >= m;
      break;
    case '>!' : 
      result =n > m;
  }
  return result ? 1 : 0
}