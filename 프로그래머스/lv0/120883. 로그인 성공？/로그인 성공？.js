function solution(id_pw, db) {
  const id = id_pw[0];
  const pw = id_pw[1];

  const filtered = db.filter(el => el[0] === id)[0];

  if (filtered) {
    return filtered[1] === pw ? 'login' : 'wrong pw'
  } else {
    return 'fail'
  }
}