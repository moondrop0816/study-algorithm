function solution(x, n) {
  const arr = [x];
  for (i = 0; i < n-1; i++) {
    arr.push(arr[i] + x);
  }
  return arr
}