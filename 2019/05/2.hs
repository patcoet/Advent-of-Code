-- Day 5: Sunny with a Chance of Asteroids
-- Task: Expand the Intcode computer from day 2 with more opcodes and stuff.
import Data.List.Split (splitOn)

-- Turn an integer into a list of digits:
digits x
  | x == 0 = []
  | x /= 0 = digits (div x 10) ++ [mod x 10]

-- Given a computer's memory and an input value, return an output value:
run' mem input = run mem input [] 0

run mem input output ptr = case opcode of
  99 -> output
  1 -> run (mem' mem p3 (v1 + v2)) input output (ptr + 4)
  2 -> run (mem' mem p3 (v1 * v2)) input output (ptr + 4)
  3 -> run (mem' mem p1 input) input output (ptr + 2)
  4 -> run mem input (output ++ [v1]) (ptr + 2)
  5 -> case v1 /= 0 of True  -> run mem input output v2
                       False -> run mem input output (ptr + 3)
  6 -> case v1 == 0 of True  -> run mem input output v2
                       False -> run mem input output (ptr + 3)
  7 -> case v1 < v2 of True  -> run (mem' mem p3 1) input output (ptr + 4)
                       False -> run (mem' mem p3 0) input output (ptr + 4)
  8 -> case v1 == v2 of True  -> run (mem' mem p3 1) input output (ptr + 4)
                        False -> run (mem' mem p3 0) input output (ptr + 4)
  where instruction = mem !! ptr
        opcode = mod instruction 100 -- Last two digits of the instruction.
        modes' = replicate 3 0 ++ digits (div instruction 100) -- Takes all digits of the instruction but the last two,
        modes = reverse $ drop (length modes' - 3) modes'      -- reverses, and pads with 0s, so `12` becomes `[2,1,0]`.
        p1 = case modes !! 0 of 0 -> mem !! (ptr + 1) -- 1st parameter if in position mode.
                                1 -> ptr + 1          -- 1st parameter if in immediate mode.
        p2 = case modes !! 1 of 0 -> mem !! (ptr + 2)
                                1 -> ptr + 2
        p3 = case modes !! 2 of 0 -> mem !! (ptr + 3)
                                1 -> ptr + 3
        v1 = mem !! p1 -- These are just to save having to write `mem !! p1` and so on above.
        v2 = mem !! p2
        v3 = mem !! p3
        mem' memory index newValue = take index memory ++ [newValue] ++ drop (index + 1) mem -- Changes a value in memory.

main = do
  input <- readFile "input.txt"
  let mem = map (\x -> read x :: Int) $ splitOn "," input
  putStrLn $ "Program output: " ++ (show $ run' mem 5)

