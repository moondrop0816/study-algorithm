function solution(a, b) {
    if (`${a}${b}` === `${b}${a}`) return Number(`${a}${b}`)
    return `${a}${b}` > `${b}${a}` ? Number(`${a}${b}`) : Number(`${b}${a}`)
}