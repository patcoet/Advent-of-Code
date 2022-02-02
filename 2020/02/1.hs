main = do
  input <- readFile "input.txt"
  print $ map words $ lines input
  -- let expenses = map (\x -> read x :: Int) $ words input
  -- print $ head [ x * y | x <- expenses, y <- expenses, x /= y, x + y == 2020 ]