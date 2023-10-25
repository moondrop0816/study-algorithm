function solution(num_list) {
  return num_list.reduce((acc, cur)=>{
    while(cur > 1) {
      if (cur % 2 === 0) {
        cur /= 2;
        acc++;
      } else {
        cur = (cur - 1) / 2
        acc++;
      }
    }
    return acc
  }, 0);
}