function solution(numbers) {
  const arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

  let result = numbers;

  for (let i = 0; i < arr.length; i++) {
    result = result.split(arr[i]).join(i);
  }

  return +result;
}