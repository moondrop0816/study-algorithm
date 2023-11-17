function solution(strArr) {
    const lengthArr = strArr.map(el => el.length);
    const result = lengthArr.reduce((acc, cur) => { 
      acc[cur] = (acc[cur] || 0)+1; 
      return acc;
    }, {});

    return Math.max(...Object.values(result))
}