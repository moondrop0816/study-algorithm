function solution(arr) {
  const row = arr.length;
  const col = arr[0].length;
  const gap = Math.abs(row - col)
  
  if (gap === 0) return arr
  
  if (row > col) {
    const temp = new Array(gap).fill(0)
    return arr.map((el) => [...el, ...temp])
  }
  
  if (row < col) {
    const temp = new Array(arr[0].length).fill(0)
    for (let i = 0; i < gap; i++){
      arr.push(temp)
    }
    return arr
  }
}