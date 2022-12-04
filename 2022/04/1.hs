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
  print $ length $ filter hasMatch' ranges
  where hasMatch (x, y) = fst x >= fst y && snd x <= snd y
        hasMatch' x = hasMatch x || hasMatch (swap x)
