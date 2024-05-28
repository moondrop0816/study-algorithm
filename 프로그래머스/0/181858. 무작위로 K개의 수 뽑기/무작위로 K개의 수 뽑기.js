function solution(arr, k) {
  const result = []

  for (let num of arr) {
    if (result.includes(num)) continue
    if (result.length === k) break
    result.push(num)
  }

  if (result.length < k) {
    const temp = new Array(k - result.length).fill(-1) 
    result.push(...temp)
  }

  return result
}