possibleTriangle :: [Int] -> Bool
possibleTriangle [a, b, c] = a + b > c && a + c > b && b + c > a

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\03\\input.txt" -- input looks like "  368  692  564\n   48  263  586\n  356  902  922\n"
  let ints = map (map (read :: String -> Int) . words) (lines input)
  let ps = filter possibleTriangle ints
  print (length ps)
