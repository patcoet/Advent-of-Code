use std::fs;

fn main() {
  let input = fs::read_to_string("input.txt").expect("I AM ERROR.");

  let parsed = input
    .trim()
    .split('\n')
    .map(|x| {
      x.trim()
        .split(" => ")
        .map(|y| {
          y.split(", ")
            .map(|z| z.split(' ').collect::<Vec<_>>()) // All the collecting probably isn't needed.
            .map(|z| (z[0].parse::<i32>().unwrap(), z[1]))
            .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
    })
    .collect::<Vec<_>>();

  let mut requirements = vec![(1, "FUEL")];
  let mut leftovers: Vec<(i32, &str)> = Vec::new();

  while requirements.iter().any(|x| x.1 != "ORE") {
    requirements = combine_reqs(requirements);
    // println!("requirements: {:?}", requirements);
    // println!("leftovers: {:?}", leftovers);
    // println!("{:?}", "");

    let req = requirements.remove(requirements.iter().position(|x| x.1 != "ORE").unwrap());
    let element = req.1;
    let mut num_elem_needed = req.0;
    for leftover in &leftovers {
      if leftover.1 == element {
        num_elem_needed -= leftover.0;
        break;
      }
    }
    if leftovers.iter().position(|x| x.1 == element).is_some() {
      leftovers.remove(leftovers.iter().position(|x| x.1 == element).unwrap());
    }

    for line in &parsed {
      let output = line[1][0];
      if output.1 == element {
        let num_made_at_a_time = output.0;
        let mut num_reactions_needed = 0;
        loop {
          if num_made_at_a_time * num_reactions_needed >= num_elem_needed {
            let num_left_over = num_made_at_a_time * num_reactions_needed - num_elem_needed;
            leftovers.push((num_left_over, element));
            leftovers = combine_reqs(leftovers);
            break;
          }
          num_reactions_needed += 1;
        }

        for prereq in &line[0] {
          requirements.push((prereq.0 * num_reactions_needed, prereq.1));
        }
      }
    }
  }

  requirements = combine_reqs(requirements);

  println!("Ore required: {:?}", requirements[0].0);
}

// [(2, "A"), (3, "B"), (4, "A")] -> [(6, "A"), (3, "B")]
fn combine_reqs(reqs: Vec<(i32, &str)>) -> Vec<(i32, &str)> {
  let mut tmp = vec![];

  for req in &reqs {
    tmp.push((
      reqs.iter().filter(|x| x.1 == req.1).map(|x| x.0).sum(),
      req.1,
    ));
  }

  tmp.sort();
  tmp.dedup();

  return tmp;
}
