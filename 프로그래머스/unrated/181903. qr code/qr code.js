function solution(q, r, code) {
    return code.split('').filter((el, idx)=> idx % q === r ? el : null).join('')
}