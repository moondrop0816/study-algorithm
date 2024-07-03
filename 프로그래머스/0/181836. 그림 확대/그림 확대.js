function solution(picture, k) {
  const result = []
  for (let str of picture) {
    let newStr = ''
    for (let el of str) {
      newStr += el.repeat(k)
    }
    result.push(...new Array(k).fill(newStr))
  }

  return result
}