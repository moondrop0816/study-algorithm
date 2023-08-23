function solution(arr, queries) {
    queries.map((query)=>{
      const [i, j] = query;
      const first = arr[i];

      arr[i] = arr[j];
      arr[j] = first;
  })
  
  return arr;
}