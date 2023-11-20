function solution(order) {
  return order.reduce((acc, _, idx)=>{
    if (order[idx].includes('americano') || order[idx].includes('anything')) {
      return acc += 4500
    }

    if (order[idx].includes('cafelatte')) {
      return acc += 5000
    }
  }, 0)
}