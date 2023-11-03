function solution(myStr) {
  const arr = ['a', 'b', 'c'];
  let result = myStr;

  for (let el of arr) {
    result = result.replaceAll(el, ' ')
  }

  return result.split(' ').filter(el => el).length > 0 ? result.split(' ').filter(el => el) : ["EMPTY"]
}