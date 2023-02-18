function solution(balls, share) {
    let all = 1;
    for(i = 1; i <= balls; i++) {
        all *= i
    }
    
    let pick = 1;
    for (i = 1; i <= share; i++) {
        pick *= i;
    }
    
    let gap = 1;
    for (i = 1; i <= (balls - share); i++) {
        gap *= i;
    }
    
    return Math.round(all / (gap * pick))  ;
        
        
}