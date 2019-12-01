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
  let points' = filter (\x -> hasSingleClosest x coords) points
  let closests = map (\x -> head $ dists x coords) points'
  let closests' = filter (\x -> isInner (fst x) coords) closests
  let areaSizes = map (\x -> (x, length $ filter (\y -> fst y == x) closests')) coords
  let areaSizes' = sortOn snd areaSizes
  let largestAreaSize = snd $ last areaSizes'

  print largestAreaSize

-- "267, 196" -> (267,196)
parse str = (read (takeWhile isDigit str) :: Int, read (dropWhile (not . isDigit) $ dropWhile (isDigit) str) :: Int)

dist (x0, y0) (x1, y1) = abs (x0 - x1) + abs (y0 - y1)

dists coord points = sortOn snd [(point, dist coord point) | point <- points]

hasSingleClosest coord points = snd first < snd second
  where ds = dists coord points
        first = head ds
        second = head $ tail ds

-- An inner coord is one that has at least one other coord in each of its quadrants
-- (Which means it doesn't have an infinite area)
isInner coord otherCoords = hasU && hasL && hasR && hasD
  where qs = map (quad coord) otherCoords
        hasU = any (\(a, b, c, d) -> a == True) qs
        hasL = any (\(a, b, c, d) -> b == True) qs
        hasR = any (\(a, b, c, d) -> c == True) qs
        hasD = any (\(a, b, c, d) -> d == True) qs

quad (x0, y0) (x1, y1) = (u, l, r, d)
  where dx = abs $ x1 - x0
        dy = abs $ y1 - y0
        u = y1 < y0 && x0 - dy <= x1 && x1 <= x0 + dy
        l = x1 < x0 && y0 - dx <= y1 && y1 <= y0 + dx
        r = x1 > x0 && y0 - dx <= y1 && y1 <= y0 + dx
        d = y1 > y0 && x0 - dy <= x1 && x1 <= x0 + dy