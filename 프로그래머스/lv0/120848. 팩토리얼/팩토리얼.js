function solution(n) {
  const fac = (number) => {
      if (number <= 1) return 1;
      
      return number * fac(number - 1);
  }

  let num = 1;
  let result = 1;
  
  while (result <= n) {
      result = fac(num);

      if (result > n) {
        num--;
        break;
      }

      num += 1;
  }
  
  return num;
}