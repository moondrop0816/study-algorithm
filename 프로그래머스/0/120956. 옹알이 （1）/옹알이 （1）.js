function solution(babbling) {
  const word = ['aya', 'ye', 'woo', 'ma'];
  let answer = 0;
  
  for (let i = 0; i < babbling.length; i++){
    for (let j of word) {
      babbling[i] = babbling[i].replace(j, 'X')
    }

    babbling[i].split('X').join('') === '' ? answer += 1 : null
  } 

  return answer
}