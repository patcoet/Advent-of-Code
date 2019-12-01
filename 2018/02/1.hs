main = do
  input <- readFile "input.txt"
  let pts = map points $ lines input
  let pairs    = sum $ map fst pts
  let triplets = sum $ map snd pts
  putStrLn $ show $ pairs * triplets

points line = (a, b)
  where ls = map (\x -> length $ filter (== x) line) line
        a = if any (== 2) ls then 1 else 0
        b = if any (== 3) ls then 1 else 0
