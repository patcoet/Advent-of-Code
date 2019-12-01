import Data.Char (isDigit)
import Data.List (sort, sortOn)
import Data.List.Unique (sortUniq)

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

idList events = sortUniq $ map (\(x, y, z) -> y) events

-- "Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events."
timestampDiff (x, _, _) (y, _, _) = last $ zipWith (-) y x

minutesSlept [] total = total
minutesSlept events@(h:t) total = case h of
  (timestamp, id, "begin") -> minutesSlept t total
  (timestamp, id, "sleep") -> minutesSlept (tail t) (total + (timestampDiff h (head t)))

minutesSlept' eventList guardId = minutesSlept (filter (\(x, y, z) -> y == guardId) eventList) 0

idsAndMinutesSlept eventList = [(id, minutesSlept' eventList id) | id <- idList eventList]

sleepiestGuard eventList = fst $ last $ sortOn snd $ idsAndMinutesSlept eventList

listOfSleepingMinutes [] = []
listOfSleepingMinutes events@(h:t) = case h of
  (timestamp, id, "begin") -> listOfSleepingMinutes t
  ((y:d:m:h:mm:[]), id, "sleep") -> [mm .. ((\(x, y, z) -> x !! 4) $ head t) - 1] : listOfSleepingMinutes (tail t)

sleepiestMinute eventList = last $ sortOn (\x -> length $ filter (== x) eventList) eventList

sleepiestMinute' eventList = sleepiestMinute $ concat $ listOfSleepingMinutes eventList

main = do
  input <- readFile "input.txt"
  let parsedInput = sortOn (\(x, y, z) -> y) $ assignIds 0 $ sort $ map parse $ lines input
  let sg = sleepiestGuard parsedInput
  let sm = sleepiestMinute' $ filter (\(x, y, z) -> y == sg) parsedInput
  putStrLn $ show $ sg * sm
