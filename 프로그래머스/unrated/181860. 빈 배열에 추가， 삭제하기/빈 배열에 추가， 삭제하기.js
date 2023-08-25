function solution(arr, flag) {
    let x = [];

    for (let i = 0; i < flag.length; i++) {
      if (flag[i]) {
        x.push(...Array(arr[i]*2).fill(arr[i]))
      } else {
        for (let j = 0; j < arr[i]; j++) {
          x.pop()
        }
      }
    }

    return x
}