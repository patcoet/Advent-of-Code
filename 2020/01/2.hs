main = do
  input <- readFile "input.txt"
  let expenses = map (\x -> read x :: Int) $ words input
  print $ head [ x * y * z | x <- expenses, y <- expenses, z <- expenses, x /= y, x /= z, y /= z, x + y + z == 2020 ]