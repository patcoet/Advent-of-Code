import Data.List

move :: ((Int, Int), (Int, Int)) -> Char -> ((Int, Int), (Int, Int))
move ((hx, hy), (tx, ty)) dir = case dir of
  'U' -> case separated (hx, hy - 1) (tx, ty) of
    True -> ((hx, hy - 1), (hx, hy))
    False -> ((hx, hy - 1), (tx, ty))
  'L' -> case separated (hx - 1, hy) (tx, ty) of
    True -> ((hx - 1, hy), (hx, hy))
    False -> ((hx - 1, hy), (tx, ty))
  'R' -> case separated (hx + 1, hy) (tx, ty) of
    True -> ((hx + 1, hy), (hx, hy))
    False -> ((hx + 1, hy), (tx, ty))
  'D' -> case separated (hx, hy + 1) (tx, ty) of
    True -> ((hx, hy + 1), (hx, hy))
    False -> ((hx, hy + 1), (tx, ty))
  where separated (x0, y0) (x1, y1) = abs (x0 - x1) > 1 || abs (y0 - y1) > 1 || abs (x0 - x1) + abs (y0 - y1) > 2

main = do
  input <- readFile "input"
  let lines_ = lines input
      wordsed = map words lines_
      parsed = map (\x -> replicate (read $ x !! 1) $ head $ x !! 0) wordsed
  print $ length $ nub $ map snd $ move' ((0,0),(0,0)) $ concat parsed
  where move' coords [] = []
        move' coords (x:xs) = [move coords x] ++ move' (move coords x) xs
