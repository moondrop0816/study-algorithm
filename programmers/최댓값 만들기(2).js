function solution(numbers) {
  let sorted = numbers.sort((a, b) => a - b) // 오름차순으로 정렬

  return Math.max(
    sorted[0] * sorted[1],
    sorted[sorted.length - 1] * sorted[sorted.length - 2]
  )
  // 큰 양수 - 작은 음수 순으로 정렬됨.
  // 첫번째로 큰 양수 * 두번째로 큰 양수, 가장 작은 음수 * 두번째로 작은 음수 (- * - = +) 중 큰 수를 리턴
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120862
