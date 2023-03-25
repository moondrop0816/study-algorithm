function solution(polynomial) {
let arr = polynomial.split(' + ');
  let xNum = arr.filter(el=>el.includes('x'));
  let num = arr.filter(el=> !el.includes('x'))
  let xResult = 0;
  let numResult = 0;

  xResult = xNum.reduce((acc, cur)=>{
    if (cur.length !== 1) {
      acc += Number(cur.slice(0, -1))
    } else {
      acc += Number(1);
    }
    return acc;
  }, 0);

  if (xResult === 0) {
    xResult = 0;
  } else if (xResult === 1) {
    xResult = 'x';
  } else {
    xResult += 'x'
  }


  if (numResult.length !== 0) {
    numResult = num.reduce((acc, cur)=> acc += Number(cur), 0);
  }


  if (numResult === 0) {
    return xResult;
  } else if (xResult === 0) {
    return numResult.toString();
  } {
    return [xResult, numResult].join(' + ')
  }
}