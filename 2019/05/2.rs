use std::fs;

fn main() {
  let mut mem: Vec<_> = fs::read_to_string("input.txt")
    .expect("I AM ERROR.")
    .trim()
    .split(',')
    .filter_map(|x| x.parse::<i32>().ok())
    .collect();

  println!("Output: {:?}", run(&mut mem, 5));
}

fn run(mem: &mut Vec<i32>, input: i32) -> Vec<i32> {
  let mut ptr = 0;
  let mut output = Vec::new();

  loop {
    let opcode = mem[ptr] % 100;
    let modes = vec![
      mem[ptr] / 100 % 10,
      mem[ptr] / 1000 % 10,
      mem[ptr] / 10000 % 10,
    ];

    let num_args = match opcode {
      1 | 2 | 7 | 8 => 3,
      3 | 4 => 1,
      5 | 6 => 2,
      _ => 0,
    };

    let mut args: Vec<usize> = Vec::new();
    for i in 0..num_args {
      if modes[i] == 0 {
        args.push(mem[ptr + i + 1] as usize);
      } else {
        args.push(ptr + i + 1 as usize);
      }
    }

    ptr += num_args + 1;

    match opcode {
      1 => mem[args[2]] = mem[args[0]] + mem[args[1]],
      2 => mem[args[2]] = mem[args[0]] * mem[args[1]],
      3 => mem[args[0]] = input,
      4 => output.push(mem[args[0]]),
      5 => {
        if mem[args[0]] != 0 {
          ptr = mem[args[1]] as usize
        }
      }
      6 => {
        if mem[args[0]] == 0 {
          ptr = mem[args[1]] as usize
        }
      }
      7 => mem[args[2]] = if mem[args[0]] < mem[args[1]] { 1 } else { 0 },
      8 => mem[args[2]] = if mem[args[0]] == mem[args[1]] { 1 } else { 0 },
      _ => return output,
    }
  }
}
