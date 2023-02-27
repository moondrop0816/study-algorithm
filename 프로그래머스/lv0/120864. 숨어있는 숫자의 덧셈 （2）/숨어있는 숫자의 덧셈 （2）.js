function solution(my_string) {
  let str = my_string;
  const rex = /[a-z|A-Z]/g;
  return str.replaceAll(rex,',').split(',').filter(el=> el !== '').reduce((acc, cur)=> acc += Number(cur), 0);
    

}