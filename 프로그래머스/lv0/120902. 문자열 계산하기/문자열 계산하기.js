function solution(my_string) {
  let arr = my_string.split(' ');
  let result = Number(arr[0]);

  for (let i = 1; i < arr.length; i++) {

    if (arr[i-1] === '-') {
      result -= Number(arr[i])
    } else if (arr[i] === '-' || arr[i] === '+') {
      continue;
    } else {
      result += Number(arr[i])
    }
  }
  return result;
}