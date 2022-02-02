import qualified Data.Digest.Pure.MD5 as MD5
import Data.ByteString.Lazy (fromStrict)
import Data.ByteString.Char8 (pack)
import Data.List

md5 str = show $ MD5.md5 $ fromStrict $ pack str

paths passcode path = [(u, pu, reachedVault pu), (d, pd, reachedVault pd), (l, pl, reachedVault pl), (r, pr, reachedVault pr)]
  where hash = md5 $ passcode ++ path
        -- Going up is allowed if we've gone down more than up and the hash is right
        u = length (filter (== 'D') path) > length (filter (== 'U') path) && elem (hash !! 0) ['b' .. 'f']
        pu = path ++ "U"
        d = length (filter (== 'D') path) - length (filter (== 'U') path) < 3 && elem (hash !! 1) ['b' .. 'f']
        pd = path ++ "D"
        l = length (filter (== 'R') path) > length (filter (== 'L') path) && elem (hash !! 2) ['b' .. 'f']
        pl = path ++ "L"
        r = length (filter (== 'R') path) - length (filter (== 'L') path) < 3 && elem (hash !! 3) ['b' .. 'f']
        pr = path ++ "R"

reachedVault path = num 'D' - num 'U' == 3 && num 'R' - num 'L' == 3
  where num char = length $ filter (== char) path

thing passcode ps = case any (\(x, y, z) -> x == True && z == True) ps of
  True -> (\(x, y, z) -> y) $ head $ sortOn (\(x, y, z) -> length y) $ filter (\(x, y, z) -> x == True && z == True) ps
  False -> thing passcode $ concat $ map (\(x, y, z) -> paths passcode y) $ filter (\(x, y, z) -> x == True) ps

thing' passcode = thing passcode $ paths passcode ""

main = print $ thing' "qtetzkpl"