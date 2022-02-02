import Data.List (nub, sort)

main = do
  input <- readFile "input.txt"
  -- print $ parse input
  print "Second   Worker 1   Worker 2   Worker 3   Worker 4   Worker 5"
  thing (parse input) [] [] 0

-- "Step C must be finished before step A can begin.\nStep C must be finished before step F can begin." -> [Step "C" 'A',Step "C" 'F']
parse input = sort $ map (\a -> Step (sort $ map fst $ filter (\x -> snd x == a) $ pairs) a) letters
  where letters = sort $ nub $ concat $ filter (\x -> length x == 1) $ words $ filter (/= '\n') input
        pairs = [(\x -> (head $ x !! 1, head $ x !! 7)) $ words line | line <- lines input]

data Step = Step [Char] Char deriving (Eq, Ord, Show)

popFirstAvailable stepList = (firstAvailableLetter, filter (\(Step x y) -> y /= firstAvailableLetter) $ map (\(Step x y) -> Step (filter (/= firstAvailableLetter) x) y) stepList)
  where firstAvailableLetter = (\(Step x y) -> y) $ head (filter (\(Step x y) -> x == []) stepList)

popPop [] = []
popPop stepList = (fst first) : (popPop $ snd first)
  where first = popFirstAvailable stepList

thing stepList workerList result currentTick = do
  print $ (show currentTick) ++ "        " ++ [(fst $ pfa stepList)] ++ "          " ++ [(fst $ pfa $ snd $ pfa stepList)] ++ "          " ++ [(fst $ pfa $ snd $ pfa $ snd $ pfa stepList)]
  where pfa = popFirstAvailable