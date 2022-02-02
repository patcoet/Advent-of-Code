processLine :: [Char] -> Int -> Int
processLine [] curr = curr
processLine (s : ss) curr = case s of
  'U' -> if elem curr [1, 2, 3] then processLine ss curr else processLine ss (curr - 3)
  'R' -> if elem curr [3, 6, 9] then processLine ss curr else processLine ss (curr + 1)
  'D' -> if elem curr [7, 8, 9] then processLine ss curr else processLine ss (curr + 3)
  'L' -> if elem curr [1, 4, 7] then processLine ss curr else processLine ss (curr - 1)

processLines :: [[Char]] -> [Int] -> [Int]
processLines [] nums = tail (reverse nums)
processLines (line : lines) nums = processLines lines (processLine line (head nums) : nums)

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\02\\input.txt" -- input looks like "RUDDDU\nLLLR\n"
  let code = processLines (lines input) [5]
  print code