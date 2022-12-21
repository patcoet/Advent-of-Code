import Data.Maybe
import System.Environment

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

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let ty = 2000000
      parsed = map parseLine $ lines input
      sensorsAndDistances = map (\(c1, c2) -> (c1, dist c1 c2)) parsed
      blockedOnTy = map fromJust $ filter isJust $ map (\(x, y) -> coordsBlockedBy x y ty) sensorsAndDistances
      lowest = minimum $ map fst blockedOnTy
      highest = maximum $ map snd blockedOnTy
  print $ highest - lowest
