// 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120812

// 문제 설명
// 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

// 제한사항
// 0 < array의 길이 < 100
// 0 ≤ array의 원소 < 1000

// 입출력 예
// array	result
// [1, 2, 3, 3, 3, 4]	3
// [1, 1, 2, 2]	-1
// [1]	1

// 입출력 예 설명
// 입출력 예 #1

// [1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.
// 입출력 예 #2

// [1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.
// 입출력 예 #3

// [1]에는 1만 있으므로 최빈값은 1입니다.
// ※ 공지 - 2022년 10월 17일 제한 사항 및 테스트케이스가 수정되었습니다.

function solution(array) {
  // array의 요소 중 같은 값이 가장 많은 요소
  // 배열에 요소-빈도수 추가하게 해서 빈도수가 가장 많은 키값을 리턴
  const obj = {}

  // 배열의 길이만큼 반복
  // 객체에 배열의 요소가 없으면 요소를 추가하고 값을 1로 함
  // 요소가 있으면 값에 1씩 추가

  for (i = 0; i < array.length; i++) {
    if (!(array[i] in obj)) {
      obj[array[i]] = 1
    }
    obj[array[i]]++
  }

  // 키값을 담을 결과값
  // 최대값.
  // 객체의 값 중에서 가장 큰 값을 가진 키를 결과값에 담는다.
  // 만약 가장 큰 값이 여러개라면 -1.

  let result = 0
  let max = 0
  for (key in obj) {
    if (obj[key] > max) {
      // 객체의 값이 max보다 클때만 실행
      max = obj[key]
      result = Number(key)
    } else if (obj[key] === max) {
      // 객체의 값이 max와 같을때만 실행
      result = -1
    }
  }

  return result
}
