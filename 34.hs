import Data.Numbers.Primes as P
import Data.Digits as D
import Data.List

fact :: Int -> Int
fact 0 = 1
fact x = x * fact (x-1)

digitfact :: Int -> Int
digitfact x = sum $ map fact (D.digits 10 x)

isDigitFact :: Int -> Bool
isDigitFact x = (x == digitfact x)
