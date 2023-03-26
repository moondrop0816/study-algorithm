function solution(quiz) {
    return quiz.map((element)=> {
        let arr = element.split(' ');
        const x = arr[0];
        const operator = arr[1];
        const y = arr[2];
        const z = arr[4];

        if (operator === '+') {
          return Number(x) + Number(y) === Number(z) ? 'O' : 'X'
        } 

        if (operator === '-') {
          return Number(x) - Number(y) === Number(z) ? 'O' : 'X'
        }
      });
}