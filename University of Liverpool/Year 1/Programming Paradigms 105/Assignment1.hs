-- Do not alter the following line
module Assignment1 (char_to_int, repeat_char, decode, int_to_char, length_char, 
drop_char, encode, complex_encode, complex_decode) where
-- Part A
char_to_int :: Char -> Integer
char_to_int c = digitToInt c

main = do
    let number = '0'
    putStrLn "The number : "
    print (number)
    putStrLn "Integer equivalent to character entered"
    print ( char_to_int number)