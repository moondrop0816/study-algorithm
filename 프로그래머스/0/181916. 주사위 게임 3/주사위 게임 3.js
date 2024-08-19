function solution(a, b, c, d) {
  const temp = [a,b,c,d];
  const dict = {}
  for (let el of temp) {
    if (el in dict) {
      dict[el] += 1
    } else {
      dict[el] = 1
    }
  }

  const keys = Object.keys(dict)
  const values = Object.values(dict)

  if (values.length === 1) return 1111 * a

  if (values.length === 2) {
    if (values.indexOf(3) !== -1){
      const p = Number(keys[values.indexOf(3)])
      keys.splice(values.indexOf(3),1)
      return (10 * p + Number(keys[0])) ** 2
    } else {
      return (Number(keys[0]) + Number(keys[1])) * Math.abs(Number(keys[0]) - Number(keys[1]))
    }
  }
    
  if (values.length === 3) {
    keys.splice(values.indexOf(2),1)
    return keys[0] * keys[1]
  }
  
  if (values.length === 4) return Math.min(...keys)  
}