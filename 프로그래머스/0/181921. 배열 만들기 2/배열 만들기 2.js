function solution(l, r) {
  const result = []
  for (i = l; i <= r; i++) {
    const temp = i.toString().split('')
    if (temp.every((el)=> el === '5' || el === '0')) {
      result.push(i)
    }
  }
  return result.length === 0 ? [-1] : result.sort((a,b)=> a - b)
}