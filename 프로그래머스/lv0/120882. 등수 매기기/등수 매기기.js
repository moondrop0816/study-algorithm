function solution(score) {
    const avg = score.map(el=> (el[0] + el[1])/2);
    const rank = [...avg].sort((a,b) => b-a).map((el, idx)=> [el, idx+1]);

    return avg.map(el=> rank.findIndex(el2=> el2[0] === el) + 1);
}