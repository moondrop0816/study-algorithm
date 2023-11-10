function solution(arr, queries) {
  queries.map((query)=>{
    const [s, e, k] = query;

    for (let i = s; i <= e; i++) {
      if (i % k === 0) arr[i] += 1;
    }
  })

  return arr;
}