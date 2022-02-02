parse = map (\x -> read x :: Int) . lines . filter (/= '+')

freq (x:xs) sum list
  | elem newSum list = newSum
  | otherwise = freq (xs ++ [x]) newSum (newSum : list)
  where newSum = sum + x

main = do
  input <- readFile "input.txt"
  putStrLn $ show $ freq (parse input) 0 [0]