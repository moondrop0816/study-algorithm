function solution(arr) {
  let x = 0
  let prev = arr
  
  while(true) {
      const check = prev.map(a => {
          if(a >= 50 && a%2 === 0) return a / 2
          if(a < 50 && a%2 === 1) return a * 2 + 1
          return a
      })
      
      const isAllSame = prev.every((a, i) => a === check[i])
      if(isAllSame) break
      x += 1
      
      prev = check
  }
  
  return x
}