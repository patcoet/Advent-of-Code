import Data.Char (isDigit)
import Data.List (sort, sortOn)

main = do
  input <- readFile "input.txt"
  let coords = map parse $ lines input
  let x0 = head $ sort $ map fst coords
  let x1 = last $ sort $ map fst coords
  let y0 = head $ sort $ map snd coords
  let y1 = last $ sort $ map snd coords
  let points = [(x, y) | x <- [x0 .. x1], y <- [y0 .. y1]]
  let distSums = map (\x -> sumOfDists x coords) points

  print $ length $ filter (< 10000) distSums

-- "267, 196" -> (267,196)
parse str = (read (takeWhile isDigit str) :: Int, read (dropWhile (not . isDigit) $ dropWhile (isDigit) str) :: Int)

dist (x0, y0) (x1, y1) = abs (x0 - x1) + abs (y0 - y1)

dists coord points = sortOn snd [(point, dist coord point) | point <- points]

sumOfDists coord points = sum $ map (dist coord) points
