import Data.List
import System.Environment
import Debug.Trace

coordsBetween :: (Int, Int) -> (Int, Int) -> [(Int, Int)]
coordsBetween (x0, y0) (x1, y1) = [(xx, yy) | xx <- [lx .. hx], yy <- [ly .. hy]]
  where (lx, hx) = (min x0 x1, max x0 x1)
        (ly, hy) = (min y0 y1, max y0 y1)

coordsBetween' :: [(Int, Int)] -> [(Int, Int)]
coordsBetween' (_:[]) = []
coordsBetween' (c1:c2:cs) = nub $ coordsBetween c1 c2 ++ coordsBetween' (c2:cs)

parseLine :: String -> [(Int, Int)]
parseLine line = coordsBetween' $ map (\x -> read x :: (Int, Int)) $ map (\x -> "(" ++ x ++ ")") words'
  where words' = filter (/= "->") $ words $ line

parseLines :: [String] -> [(Int, Int)]
parseLines ls = concat $ map parseLine ls

doSand :: [(Int, Int)] -> Int -> (Int, Int)
doSand rocks maxY = doSand' rocks (500, 0)
  where doSand' rs (x, y)
          | elem (500, 0) rocks = (500, 0)
          | notElem (x, y + 1) rs = doSand' rs (x, y + 1)
          | notElem (x - 1, y + 1) rs = doSand' rs (x - 1, y + 1)
          | notElem (x + 1, y + 1) rs = doSand' rs (x + 1, y + 1)
          | otherwise = (x, y)

numRestedGrains :: [(Int, Int)] -> Int -> Int -> Int
numRestedGrains rocks n maxY
  | done = n
  | otherwise = trace ("sand resting at " ++ show doneSand) $ numRestedGrains (doneSand : rocks) (n + 1) maxY
  where doneSand = doSand rocks maxY
        done = doneSand == (500, 0)

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let rockCoords = parseLines $ lines input
      maxY = snd $ last $ sortOn snd rockCoords
      rc' = rockCoords ++ [(xx, maxY + 2) | xx <- [500 - maxY * 2 .. 500 + maxY * 2]]
  print maxY
  print $ 1 + numRestedGrains rc' 0 maxY
