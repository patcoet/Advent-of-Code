import Data.List
import Data.Maybe
import System.Environment
import Debug.Trace

parseLine :: String -> ((Int, Int), (Int, Int))
parseLine l = tuples nums
  where words' = map (takeWhile (flip notElem ",:") . tail . dropWhile (/= '=')) $ filter (elem '=') $ words l
        nums = map (\x -> read x :: Int) words'
        tuples (x1:x2:x3:x4:[]) = ((x1, x2), (x3, x4))

dist :: (Int, Int) -> (Int, Int) -> Int
dist (x0, y0) (x1, y1) = abs (x0 - x1) + abs (y0 - y1)

coordsBlockedBy :: (Int, Int) -> Int -> Int -> Maybe (Int, Int)
coordsBlockedBy (x0, y0) d ty
  | d >= abs (ty - y0) = Just (x0 - d + abs (ty - y0), x0 + d - abs (ty - y0))
  | otherwise = Nothing

data SquashResult = NotDone (Int, Int) | Done Int
squash :: [(Int, Int)] -> Maybe Int
squash (c:[]) = Nothing
squash l@(c:cs) 
  | overlaps == [] = Just $ 1 + snd smallestFst
  | otherwise = squash l'
  where smallestFst = minimum l
        overlaps = filter (\(x, y) -> x - 1 <= snd smallestFst) (delete smallestFst l)
        smFst' = (fst smallestFst, maximum (map snd overlaps))
        l' = smFst' : (delete smallestFst $ l \\ overlaps)

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let parsed = map parseLine $ lines input
      sensorsAndDistances = map (\(c1, c2) -> (c1, dist c1 c2)) parsed
      blockedOnTy ty = map fromJust $ filter isJust $ map (\(x, y) -> coordsBlockedBy x y ty) sensorsAndDistances
      (Just x, y) = head $ filter (isJust . fst) $ map (\y -> (squash (blockedOnTy y), y)) [0 .. 4000000]
  print $ x * 4000000 + y
