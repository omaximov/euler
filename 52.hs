import Data.List
import Data.Digits

listequals :: (Eq a) => [a] -> [a] -> Bool
listequals xs ys = null (xs \\ ys)


xList :: Int -> [Int]
xList x = [2*x, 3*x, 4*x, 5*x, 6*x]
