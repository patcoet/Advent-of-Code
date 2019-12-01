import Data.Char
import Data.List.Unique

main = do
  input <- readFile "input.txt"
  putStrLn $ show $ length $ repeated $ concat $ map parse $ lines input

getInts str
  | str == "" = []
  | isDigit $ head str = (read (takeWhile isDigit str) :: Int) : getInts (dropWhile isDigit str)
  | otherwise = getInts $ dropWhile (\x -> not $ isDigit x) str

claimedCoords (x0:y0:w:h:[]) = [(x0+x, y0+y) | x <- [0 .. w-1], y <- [0 .. h-1]]

parse line = claimedCoords $ tail $ getInts line
