function solution(s){
  const str = s.toLowerCase();
  return str.split('p').length - 1 === str.split('y').length - 1 ? true : false
}