main = do
  input <- readFile "input.txt"
  putStrLn $ show $ foldr (+) 0 $ map (\x -> read x :: Int) $ lines $ filter (/= '+') input