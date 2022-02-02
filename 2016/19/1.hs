import Debug.Trace

elfList n = [(x, 1) | x <- [1..n]]

splitList list = (evens, odds)
  where zippedList = zip list [1..]
        evens = map fst $ filter (\x -> even $ snd x) zippedList
        odds = map fst $ filter (\x -> odd $ snd x) zippedList

act elves
  | odd $ length elves = init (tail thing) ++ [((\x y -> (fst y, snd y + snd x)) firstElf lastElf)]
  | otherwise = thing
  where (a, b) = splitList elves
        thing = zipWith (\x y -> (fst y, snd y + snd x)) (a ++ [(0,0)]) b
        firstElf = head thing
        lastElf = last thing

thing elves
  | length elves == 1 = elves
  | otherwise = thing $ act elves

main = print $ fst $ head $ thing $ elfList 3004953