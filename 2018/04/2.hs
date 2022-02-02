import Data.Char (isDigit)
import Data.List (sort, sortOn)
import Data.List.Unique (count, sortUniq)

main = do
  input <- readFile "input.txt"
  let parsedInput = sortOn (\(x, y, z) -> y) $ assignIds 0 $ sort $ map parse $ lines input
  let sleepiest = last $ sortOn (snd . snd) $ map (\a -> (a, last $ sortOn snd $ count $ snd $ sleepingMinutes' $ filter (\(t, id, e) -> id == a) parsedInput)) $ idList parsedInput
  print sleepiest
  print $ (fst sleepiest) * (fst $ snd sleepiest)

getInts [] = []
getInts str@(c:cs)
  | isDigit c = (read (takeWhile isDigit str) :: Int) : getInts (dropWhile isDigit str)
  | otherwise = getInts cs

parse line = (timestamp, id, action)
  where ints = getInts line
        timestamp = take 5 ints
        id = if length ints == 6 then last ints else -1
        ws = words line
        action = if elem "begins" ws then "begin" else if elem "asleep" ws then "sleep" else "wake"

assignIds currId [] = []
assignIds currId l@(h:t) = case h of
  (timestamp, id, "begin") -> h : assignIds id t
  (timestamp, id, sleepOrWake) -> (timestamp, currId, sleepOrWake) : assignIds currId t

sleepingMinutes [] = []
sleepingMinutes (h:t) = case h of
  (ts, _, "sleep") -> init [ts !! 4 .. (\(x, y, z) -> x !! 4) $ head t] : sleepingMinutes (tail t)
  otherwise -> sleepingMinutes t

sleepingMinutes' e@((_, id, _):t) = case sleepingMinutes e of
  [] -> (id, [-1])
  otherwise -> (id, concat $ sleepingMinutes e)

idList events = sortUniq $ map (\(x, y, z) -> y) events
