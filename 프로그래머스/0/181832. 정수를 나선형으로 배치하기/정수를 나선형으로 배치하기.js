function solution(n) {
  const arr = new Array(n).fill(0).map(() => new Array(n).fill(0));
  
  let num = 1; 
  let top = 0, bottom = n - 1, left = 0, right = n - 1; 
  
  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      arr[top][i] = num;
      num += 1;
    }
    top++; 
    
    for (let i = top; i <= bottom; i++) {
      arr[i][right] = num;
      num += 1;
    }
    right--; 
    
    if (top <= bottom) { 
      for (let i = right; i >= left; i--) {
        arr[bottom][i] = num;
        num += 1;
      }
      bottom--; 
    }
    
    if (left <= right) { 
      for (let i = bottom; i >= top; i--) {
        arr[i][left] = num;
        num += 1;
      }
      left++; 
    }
  }
  
  return arr
}
