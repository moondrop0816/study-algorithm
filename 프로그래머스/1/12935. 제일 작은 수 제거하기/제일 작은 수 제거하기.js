function solution(arr) {
  const result = arr.filter((el)=> el !== Math.min(...arr))
  return result.length === 0 ? [-1] : result
}