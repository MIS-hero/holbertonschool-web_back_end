export default function getSumOfHoods(initialNumber, expansion1989, expansion2019) {
    expansion1989 = expansion1989 === undefined && 89;
    expansion2019 = expansion2019 === undefined && 19;
  return initialNumber + expansion1989 + expansion2019;
}