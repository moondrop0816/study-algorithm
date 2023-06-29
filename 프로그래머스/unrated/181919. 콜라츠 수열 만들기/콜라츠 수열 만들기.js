function solution(n) {
    const result = [n];
    let num = n;
    while (num !== 1) {
        if (num % 2 === 0) {
            num /= 2
        } else {
            num = 3 * num + 1
        }
        result.push(num)
    }
    return result;
}