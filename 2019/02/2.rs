use std::fs;

fn main() {
  'outer: for noun in 0..100 {
    for verb in 0..100 {
      match run(noun, verb) {
        19690720 => println!("{:?}", 100 * noun + verb),
        _ => continue,
      }
      break 'outer;
    }
  }
}

fn run(input1: usize, input2: usize) -> usize {
  let mut ns: Vec<_> = fs::read_to_string("input.txt")
    .expect("I AM ERROR.")
    .split(',')
    .filter_map(|x| x.parse::<usize>().ok())
    .collect();
  let mut ptr = 0;

  ns[1] = input1;
  ns[2] = input2;

  loop {
    let opcode = ns[ptr];
    let p1 = ns[ptr + 1];
    let p2 = ns[ptr + 2];
    let p3 = ns[ptr + 3];

    match opcode {
      1 => ns[p3] = ns[p1] + ns[p2],
      2 => ns[p3] = ns[p1] * ns[p2],
      _ => break,
    }

    ptr += 4;
  }

  return ns[0];
}
