import System.Environment

exec :: String -> Int -> Int -> Int -> (Int, Int)
exec "addx" v x c = (x + v, c + 2)
exec _ _ x c = (x, c + 1)

execLine :: String -> Int -> Int -> (Int, Int)
execLine str x c = case words str !! 0 of
  "addx" -> exec "addx" (read $ words str !! 1) x c
  "noop" -> exec "noop" 0 x c

recurse :: [String] -> Int -> Int -> [(Int, Int)]
recurse [] x cycles = [(x, cycles)]
recurse (instr:instrs) x cycles = (x, cycles) : recurse instrs x' cycles'
  where (x', cycles') = execLine instr x cycles

main = do
  args <- System.Environment.getArgs
  input <- readFile (head $ args ++ ["input"])
  let x = 1
      cycles = 0
      results = recurse (lines input) x cycles
      values = [(cyc, fst $ last $ filter (\(_, c) -> c < cyc) results) | cyc <- [1 ..]]
      beamPositions = [0 ..]
      pcvs = [take 40 $ zip beamPositions $ drop n values | n <- [0, 40 ..]]
      pixelses = [concat $ map (\(a, (_, c)) -> if elem a [c - 1 .. c + 1] then "█" else " ") pcv | pcv <- pcvs]
  putStrLn $ unlines $ take 6 pixelses
