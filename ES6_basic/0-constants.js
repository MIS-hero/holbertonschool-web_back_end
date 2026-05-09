export function taskFirst() {
  const var task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let var combination = 'But sometimes let';
  combination += getLast();

  return combination;
}