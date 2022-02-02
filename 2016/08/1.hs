import Data.Char
import Data.List
import Data.Maybe

set :: Int -> Int -> Int -> [[Int]] -> [[Int]]
set x y value screen = take index screen ++ [xx, yy, value] : drop (index + 1) screen
  where
    index = fromJust $ findIndex (\a -> a !! 0 == xx && a !! 1 == yy) screen
    xx = mod x $ (last screen !! 0) + 1
    yy = mod y $ (last screen !! 1) + 1

rect :: Int -> Int -> [[Int]] -> [[Int]]
rect w h screen = rect_ [(x, y) | x <- [0 .. w - 1], y <- [0 .. h - 1]] screen
  where
    rect_ [] screen = screen
    rect_ (x : xs) screen = rect_ xs (set (fst x) (snd x) 1 screen)

rotateRow :: Int -> Int -> [[Int]] -> [[Int]]
rotateRow y n screen = sort $ [[mod ((c !! 0) + n) ((last screen !! 0) + 1), c !! 1, c !! 2] | c <- screen, c !! 1 == y] ++ [c | c <- screen, c !! 1 /= y]

rotateCol :: Int -> Int -> [[Int]] -> [[Int]]
rotateCol x n screen = sort $ [[c !! 0, mod ((c !! 1) + n) ((last screen !! 1) + 1), c !! 2] | c <- screen, c !! 0 == x] ++ [c | c <- screen, c !! 0 /= x]

pprint :: [[Int]] -> IO ()
pprint screen = putStr $ unlines $ map (\n -> concatMap (show . (\[x, y, z] -> z)) $ filter (\x -> x !! 1 == n) screen) [0 .. (last screen !! 1)]

parse str = case head $ words str of
  "rect" -> rect (toDigit $ takeWhile isDigit $ words str !! 1) (toDigit $ dropWhile isDigit $ words str !! 1)
  "rotate" -> case words str !! 1 of
    "row" -> rotateRow (toDigit $ words str !! 2) (toDigit $ words str !! 4)
    "column" -> rotateCol (toDigit $ words str !! 2) (toDigit $ words str !! 4)
  where
    toDigit str = read (filter isDigit str) :: Int

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\08\\input.txt"
  let screen = [[x, y, 0] | x <- [0 .. 49], y <- [0 .. 5]]
  print $ sum $ map (!! 2) $ foldr parse screen $ reverse $ lines input