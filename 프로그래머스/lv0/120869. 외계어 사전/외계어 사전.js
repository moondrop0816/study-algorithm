function solution(spell, dic) {
  for (let i = 0; i < dic.length; i++) {
      let result = true;
    for (let j = 0; j < spell.length; j++) {
      const include = dic[i].includes(spell[j]);
      const leng = dic[i].split(spell[j]).length - 1 === 1;

      result = result && include && leng;
    }
    if (result) return 1;
  }

  return 2;
}