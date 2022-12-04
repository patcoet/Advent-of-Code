import Data.Tuple
import System.Environment

-- Lines look like "7-24,8-8"
lineToRanges line = ((p1 elf1, p2 elf1), (p1 elf2, p2 elf2))
  where elf1 = takeWhile (/= ',') line
        elf2 = tail $ dropWhile (/= ',') line
        p1 part = read (takeWhile (/= '-') part) :: Int
        p2 part = read (tail $ dropWhile (/= '-') part) :: Int

main = do
  args <- System.Environment.getArgs
  input <- lines <$> readFile (head $ args ++ ["input"])
  let ranges = map lineToRanges input
  print $ length $ filter elem''' ranges
  where elem' a (y0, y1) = y0 <= a && a <= y1
        elem'' ((x0, x1), y) = elem' x0 y || elem' x1 y
        elem''' tup = elem'' tup || elem'' (swap tup)
