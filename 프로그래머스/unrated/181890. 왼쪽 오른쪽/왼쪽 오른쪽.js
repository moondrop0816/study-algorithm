function solution(str_list) {
  let left = str_list.indexOf('l');
  let right = str_list.indexOf('r');

  if (left !== -1 && left < right || right === -1) {
    console.log(true);
    return str_list.slice(0, left)
  }

  if (right !== -1 && right < left || left === -1) {
    console.log('lala');
    return str_list.slice(right + 1)
  }

  return []
}