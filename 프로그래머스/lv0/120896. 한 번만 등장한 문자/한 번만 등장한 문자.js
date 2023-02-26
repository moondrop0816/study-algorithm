function solution(s) {
  let sorted = s.split('').sort((a,b) => a > b ? 1 : -1);
  let result = '';

  for (let i = 0; i < sorted.length; i++) {
    if (!result.includes(sorted[i]) && sorted[i] !== sorted[i+1] && sorted[i-1] !== sorted[i]) {
      result += sorted[i]
    }    
  }

  return result;  
}