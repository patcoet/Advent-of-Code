import Data.List
import Data.Set (Set, empty, fromList, member, singleton, toList, unions)
import qualified Data.Set (delete, filter, map, union)
import Debug.Trace

data Thing = G String | M String deriving (Eq, Ord)

instance Show Thing where
  show (G element) = "G-" ++ element
  show (M element) = "M-" ++ element

type State = ([Set Thing], (Set Thing, Int))

parseLine line = case filteredWords of
  [] -> []
  ("a" : element : genchip : ws) -> case genchip of
    "generator" -> G (take 2 element) : parseLine (unwords ws)
    "microchip" -> M (take 2 element) : parseLine (unwords ws)
  (w : ws) -> parseLine $ unwords ws
  where
    filteredWords = filter (/= "compatible") $ words $ map (\x -> if elem x ['.', ',', '-'] then ' ' else x) line

parse input = (map (fromList . parseLine) (lines input), (empty, 1))

endState startState = ([empty, empty, empty, unions (fst startState)], (empty, 4))

-- Given a state, return the set of states that can be reached from it in one move (taking any one or two items from the elevator's current floor either up or down one floor)
-- First, one item up or down:
oneItemMovedUpOrDown (floors, (_, elevLevel)) = [(map (Data.Set.delete item) floors, (fromList [item], newLevel)) | item <- toList currFloor, newLevel <- [elevLevel - 1, elevLevel + 1], elem newLevel [1 .. 4]]
  where
    currFloor = floors !! (elevLevel - 1)

-- Two items:
twoItemsMovedUpOrDown (floors, (_, elevLevel)) = [(map (Data.Set.delete item2 . Data.Set.delete item1) floors, (fromList [item1, item2], newLevel)) | item1 <- toList currFloor, item2 <- toList currFloor, item1 /= item2, newLevel <- [elevLevel - 1, elevLevel + 1], elem newLevel [1 .. 4]]
  where
    currFloor = floors !! (elevLevel - 1)

-- Make a pending elevator move happen:
doMove :: State -> State
doMove (floors, (items, elevLevel)) = (take (elevLevel - 1) floors ++ [Data.Set.union (floors !! (elevLevel - 1)) items] ++ drop elevLevel floors, (empty, elevLevel))

-- And combine the above to make the set of states you can get to in one elevator move:
listPossibleMoves state = fromList $ map doMove (oneItemMovedUpOrDown state) ++ map doMove (twoItemsMovedUpOrDown state)

-- A floor is legal if it has no generators or if every microchip on the floor is shielded by way of being with its corresponding generator
floorIsLegal floor = allMatched (generators floor) (microchips floor)
  where
    generators floor = fromList [x | x@(G _) <- toList floor]
    microchips floor = fromList [x | x@(M _) <- toList floor]
    allMatched gs ms = (gs == empty) || all (== True) (Data.Set.map (\(M x) -> member (G x) gs) ms)

-- A state is legal if the elevator is on floors 1-4 and each floor is legal
stateIsLegal (floors, (_, elevLevel))
  | elevLevel < 1 || elevLevel > 4 = False
  | otherwise = all ((== True) . floorIsLegal) floors

listLegalMoves state = Data.Set.filter stateIsLegal $ listPossibleMoves state

reachableIn x startState
  | x == 0 = Data.Set.singleton startState
  | x > 0 = unions $ Data.Set.map listLegalMoves $ reachableIn (x - 1) startState

howMany state = howMany' state 0

howMany' state n = case Data.Set.filter (== endState state) (reachableIn n state) == empty of
  True -> trace ("End state can't be reached in " ++ show n ++ " steps...") $ howMany' state (n + 1)
  False -> n

main = do
  input <- readFile "Z:\\projects\\Advent-of-Code\\2016\\11\\input.txt"
  let initialState = parse input
  putStrLn $ "Minimum number of steps to reach the end: " ++ show (howMany initialState)
