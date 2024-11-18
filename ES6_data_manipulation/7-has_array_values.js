export default function hasValuesFromArray(set, array) {
  array.every((element) => set.has(element));
}
