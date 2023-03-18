function solution(chicken) {
    let coupon = chicken;
  let count = 0;

  while (coupon >= 10) {
    if (coupon >= 10) {
      count += 1;
      coupon -= 9
    } 
  }
  return count;
}