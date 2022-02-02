import qualified Data.Digest.Pure.MD5 as MD5
import Data.ByteString.Lazy (fromStrict)
import Data.ByteString.Char8 (pack)

md5 str = show $ MD5.md5 $ fromStrict $ pack str

input = "zpqevtbw"

hasTriple str@(c:cs)
  | length str < 3 = Nothing
  | otherwise = if all (== c) (take 3 str) then Just c else hasTriple cs

hasQuintupleOf char str
  | length str < 5 = False
  | otherwise = if all (== char) (take 5 str) then True else hasQuintupleOf char $ tail str

indexesWithTriples = [x | x <- [0..], hasTriple (md5 $ input ++ show x) /= Nothing]

indexProducesKey index = case hasTriple $ md5 $ input ++ show index of
  Nothing -> False
  Just x -> any (hasQuintupleOf x) [md5 $ input ++ show x | x <- [index+1 .. index+1000]]

main = print $ [x | x <- indexesWithTriples, indexProducesKey x] !! 63