import qualified Data.ByteString.Char8 as BSC
import qualified Data.ByteString.Lazy as BSL
import Data.Digest.Pure.MD5

getHash :: String -> String
getHash id = show $ md5 $ BSL.fromStrict $ BSC.pack id

isInteresting :: String -> Bool
isInteresting hash = take 5 hash == "00000"

-- Generate numbers 1, 2, 3, ...
-- Prepend the input to each number so we get "abc1", "abc2", "abc3", ...
-- Take the MD5 hash of each of those
-- Apply the filter isInteresting to only get the hashes that are interesting
-- Take the first 8 of those
-- For each of those, print the first character after the first 5
main = do
  print $ map (!! 5) $ take 8 $ filter isInteresting $ map ((getHash . (input ++)) . show) [1 ..]
  where
    input = "reyedfim"
