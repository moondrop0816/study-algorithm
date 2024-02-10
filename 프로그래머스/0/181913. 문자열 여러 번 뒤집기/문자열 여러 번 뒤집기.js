function solution(my_string, queries) {
  let str = my_string.split('')
  queries.map(el=>{
    const reverseStr = str.slice(el[0], el[1]+1).reverse();
    str.splice(el[0], reverseStr.length, ...reverseStr)
  })

  return str.join('')
}