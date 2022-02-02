use std::fs;

fn main() {
  let mut ns: Vec<_> = fs::read_to_string("input.txt")
    .expect("I AM ERROR.")
    .split(',')
    .filter_map(|x| x.parse::<usize>().ok())
    .collect();
  let mut ptr = 0;

  ns[1] = 12;
  ns[2] = 2;

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

  println!("Value at position 0: {}", ns[0]);
}
