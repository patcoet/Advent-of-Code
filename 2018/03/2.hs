import Data.Char

main = do
  input <- readFile "input.txt"
  let rects = map getInts $ lines input
  putStrLn $ show $ head $ head [x | x <- rects, (all (== False) $ map (overlap x) (filter (/= x) rects)) == True]

getInts str
  | str == "" = []
  | isDigit $ head str = (read (takeWhile isDigit str) :: Int) : getInts (dropWhile isDigit str)
  | otherwise = getInts $ dropWhile (\x -> not $ isDigit x) str

overlap (id1:x1:y1:w1:h1:[]) (id2:x2:y2:w2:h2:[]) = x1 <= x2+w2-1 && x1+w1-1 >= x2 && y1 <= y2+h2-1 && y1+h1-1 >= y2
