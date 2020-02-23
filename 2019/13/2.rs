use std::fs;

fn main() {
  let mut mem: Vec<_> = fs::read_to_string("input.txt")
    .expect("I AM ERROR.")
    .trim()
    .split(',')
    .filter_map(|x| x.parse::<i64>().ok())
    .collect();

  mem[0] = 2;

  // I think what you're supposed to do is pause execution every time you get to an input instruction, but I guess apparently this also works, so...
  let mut tiles = Vec::new();
  for _ in 0..300 {
    tiles = run(&mut mem, 0);
  }

  draw_game(tiles);
}

fn draw_game(tiles: Vec<i64>) {
  let mut line = String::from("");
  let mut score = 0;
  for i in 0..tiles.len() {
    if i % 3 == 0 {
      let x = tiles[i];
      let y = tiles[i + 1];
      let v = tiles[i + 2];

      if x == -1 && y == 0 {
        println!("Score: {:?}", v);
        score = v;
      }

      if x == 0 && line.len() > 0 {
        println!("{}", line);
        line = String::from("");
      }

      let chr = match v {
        1 => '█',
        2 => '█',
        3 => '―',
        4 => '●',
        _ => ' ',
      };

      line = format!("{}{}", line, chr);
    }
  }

  println!("{:?}", score);
}

fn run(mem: &mut Vec<i64>, input: i64) -> Vec<i64> {
  let mut output = Vec::new();
  let mut ptr = 0;
  let mut rel = 0;

  loop {
    let opcode = mem[ptr] % 100;
    let modes = vec![
      mem[ptr] / 100 % 10,
      mem[ptr] / 1000 % 10,
      mem[ptr] / 10000 % 10, // This is always going to be 0, but for completeness...
    ];

    let num_args = match opcode {
      1 | 2 | 7 | 8 => 3,
      3 | 4 | 9 => 1,
      5 | 6 => 2,
      _ => 0,
    };

    let mut args: Vec<usize> = Vec::new();
    for i in 0..num_args {
      match modes[i] {
        1 => args.push(ptr + i + 1 as usize),
        2 => args.push((mem[ptr + i + 1] + rel) as usize),
        _ => args.push(mem[ptr + i + 1] as usize),
      }
    }

    // If we might be writing to mem[x], pad mem with 0s until x if necessary:
    for &arg in &args {
      if arg >= mem.len() {
        for _ in 0..(arg - mem.len()) + 1 {
          mem.push(0);
        }
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
      9 => rel += mem[args[0]],
      _ => return output,
    }
  }
}
