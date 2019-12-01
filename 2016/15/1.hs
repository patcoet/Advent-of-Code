import Data.Char

parseLine line = (startPosition, numPositions)
  where (_:startPosition:_:numPositions:[]) = map (\x -> read x :: Int) $ filter (/= "") $ map (\x -> filter isDigit x) $ words line

tick discs = [(fst x, mod (snd x + 1) $ fst x) | x <- discs]

presButan discs
  | discs == [] = True
  | snd (head (tick discs)) /= 0 = False
  | snd (head (tick discs)) == 0 = presButan (tick $ tail discs)

waitingRequired discs = waitingRequired' discs 0
waitingRequired' discs x
  | presButan discs == True = x
  | otherwise = waitingRequired' (tick discs) (x+1)

main = do
  input <- readFile "input.txt"
  print $ waitingRequired $ map parseLine $ lines input