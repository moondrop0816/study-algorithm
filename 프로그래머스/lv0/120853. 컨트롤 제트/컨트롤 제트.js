function solution(s) {
    let result = 0;
    let arr = s.split(' ');

    for(let i = 0; i < arr.length; i++) {
        if (arr[i] !== 'Z' &&arr[i+1] !== 'Z') {
          result += Number(arr[i])
        }
    }

    return result;
}