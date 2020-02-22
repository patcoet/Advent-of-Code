use std::fs;

fn main() {
  let mut mem: Vec<_> = fs::read_to_string("input.txt")
    .expect("I AM ERROR.")
    .split(',')
    .filter_map(|x| x.parse::<i32>().ok())
    .collect();

  println!("Diagnostic code: {}", run(&mut mem, 1).last().unwrap());
}

fn digits(number: i32) -> (i32, i32, i32) {
  let n12 = number % 100;
  let n3 = number / 100 % 10;
  let n4 = number / 1000 % 10;
  return (n12, n3, n4);
}

fn run(mem: &mut Vec<i32>, input: i32) -> Vec<i32> {
  let mut ptr = 0;
  let mut output = Vec::new();

  loop {
    if ptr >= mem.len() || mem[ptr] == 99 {
      break;
    }
    let (opcode, mode1, mode2) = digits(mem[ptr]);
    let args = if opcode == 1 || opcode == 2 { 3 } else { 1 };
    let p1 = if mode1 == 0 {
      mem[ptr + 1] as usize
    } else {
      (ptr + 1)
    };
    let p2;
    let p3;
    if args > 1 {
      p2 = if mode2 == 0 {
        Some(mem[ptr + 2] as usize)
      } else {
        Some(ptr + 2)
      };
      p3 = Some(mem[ptr + 3]);
    } else {
      p2 = None;
      p3 = None;
    }

    match opcode {
      1 => mem[p3.unwrap() as usize] = mem[p1] + mem[p2.unwrap()],
      2 => mem[p3.unwrap() as usize] = mem[p1] * mem[p2.unwrap()],
      3 => mem[p1] = input,
      4 => output.push(mem[p1]),
      _ => break,
    }

    ptr += args + 1;
  }

  return output;
}
