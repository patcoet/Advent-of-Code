import Data.Char (intToDigit)
import qualified Data.Set (empty, filter, map, singleton, unions)
import Numeric (showIntAtBase)

input      = 1364
startCoord = (1, 1)
endCoord   = (31, 39)

isPassable (x, y)
  | x < 0 || y < 0 = False
  | otherwise = even $ length $ filter (== '1') $ showIntAtBase 2 intToDigit ((x*x + 3*x + 2*x*y + y + y*y) + input) ""

validMovesFrom (x, y) = Data.Set.unions [up, down, left, right]
  where up    = if isPassable (x, (y-1)) then Data.Set.singleton (x, y-1) else Data.Set.empty
        down  = if isPassable (x, (y+1)) then Data.Set.singleton (x, y+1) else Data.Set.empty
        left  = if isPassable ((x-1), y) then Data.Set.singleton (x-1, y) else Data.Set.empty
        right = if isPassable ((x+1), y) then Data.Set.singleton (x+1, y) else Data.Set.empty

reachableIn x startCoord
  | x == 0 = Data.Set.singleton startCoord
  | x > 0  = Data.Set.unions $ Data.Set.map validMovesFrom $ reachableIn (x-1) startCoord

howMany startCoord endCoord = howMany' startCoord endCoord 0
howMany' startCoord endCoord n = case (Data.Set.filter (== endCoord) $ reachableIn n startCoord) == Data.Set.empty of
  True -> howMany' startCoord endCoord (n+1)
  False -> n

main = print $ howMany startCoord endCoord