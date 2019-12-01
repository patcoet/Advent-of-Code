possibleTriangle :: [Int] -> Bool
possibleTriangle (a:b:c:[])
  | a + b > c && a + c > b && b + c > a = True
  | otherwise                           = False

main = do
  input <- readFile "input.txt"
  let ints = map (map (read::String->Int)) (map words (lines input))
  let ps = filter possibleTriangle ints
  putStrLn $ show (length ps)
