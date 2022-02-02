import Data.Char
import Data.List
import GHC.Utils.Outputable (trace)

-- We're trying to find the way to visit numbers 1-7 with the fewest number of steps. Since 7! is only 5040, maybe we could just visit all of them in every order and see which path is shortest. Then we just need a function that gives us the number of steps from our current location to number n.
-- Read input and turn it into a quadruply linked list of nodes with four neighbors?
-- Start by calculating paths between the numbers?

-- data MapCell = Cell {coord :: (Int, Int), u :: MapCell, r :: MapCell, d :: MapCell, l :: MapCell} | Empty
-- newtype MapCell = Cell {coord :: (Int, Int)}
--   deriving (Eq, Ord, Show)

dijkstra :: [(Int, Int)] -> [(Int, (Int, Int))] -> (Int, Int) -> [(Int, (Int, Int))] -> [(Int, (Int, Int))]
dijkstra [] dists origin distances = distances
dijkstra mapCellList dists origin distances = dijkstra mapCellList dists origin dists
  where
    currentCell = minimum dists
    mapCellList' = filter (\x -> x /= snd currentCell) mapCellList
    neighbors = filter (\x -> ((fst (snd x) == fst (snd currentCell)) && ((snd (snd x) == snd (snd currentCell) - 1) || (snd (snd x) == snd (snd currentCell) + 1))) || ((snd (snd x) == snd (snd currentCell)) && ((fst (snd x) == fst (snd currentCell) - 1) || (fst (snd x) == fst (snd currentCell) + 1)))) $ filter (\x -> elem (snd x) mapCellList') dists
    dists' = [(min (fst currentCell + 1) (fst x), snd x) | x <- neighbors] ++ filter (\x -> notElem x neighbors) dists

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\24\\test1.txt"

  -- let zipped = filter (\x -> snd x /= '#') $ zip [(x, y) | x <- [1 .. 41], y <- [1 .. 179]] $ filter (/= '\n') input
  let zipped = filter (\x -> snd x /= '#') $ zip [(x, y) | x <- [1 .. 5], y <- [1 .. 11]] $ filter (/= '\n') input
  let mapCellList = map fst zipped
  let rows = length $ lines input
  let nums = filter (isDigit . snd) $ zip [(x, y) | x <- [1 .. rows], y <- [1 .. 11]] $ filter (/= '\n') input
  let coordOf0 = head [fst x | x <- nums, snd x == '0']

  let dists = [(if x == coordOf0 then 0 else 99999, x) | x <- mapCellList]
  -- print dists

  -- print mapCellList
  -- print dists

  print $ dijkstra mapCellList dists (0, 0)

-- print $ zip [1 ..] $ filter (/= '\n') input
-- print $ length $ lines input

-- let zipped = zip [1 ..] $ filter (/= '\n') input
-- print zipped