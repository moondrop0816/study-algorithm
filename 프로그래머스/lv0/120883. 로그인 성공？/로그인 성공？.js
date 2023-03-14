function solution(id_pw, db) {
  const [id, pw] = id_pw;

  const filtered = db.filter(el => el[0] === id)[0];

  if (filtered) {
    return filtered[1] === pw ? 'login' : 'wrong pw'
  } else {
    return 'fail'
  }
}