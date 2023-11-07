function solution(arr) {
    const answer = [...arr];
    let i = 0;

    while (true) {
        if (answer.length === 2 ** i) break;
        if (answer.length > 2 ** i) i++;
        else {
            const diff = (2 ** i) - answer.length;

            for (let j=0; j<diff; j++) {
                answer.push(0);
            }
        }
    }

    return answer;
}