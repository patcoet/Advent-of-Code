main = do
  input <- readFile "input.txt"
  putStrLn $ show $ map fst $ filter (\x -> fst x == snd x) $ head [zip id1 id2 | id1 <- lines input, id2 <- lines input, numDifferingLetters id1 id2 == 1]

numDifferingLetters id1 id2 = length $ filter (== False) $ map (\x -> fst x == snd x) $ zip id1 id2