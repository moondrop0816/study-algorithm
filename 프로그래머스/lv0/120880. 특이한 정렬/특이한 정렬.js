function solution(numlist, n) {
    let gap = numlist.map((el, idx)=> {
    return {idx : idx, value: Math.abs(n - el), el}
  });


  gap.sort((a, b) => {
    return a.value - b.value || b.el - a.el
  })

  return gap.map(el=> el.el)
}