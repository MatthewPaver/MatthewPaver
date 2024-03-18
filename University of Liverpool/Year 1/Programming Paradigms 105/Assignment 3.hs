module Main (get_maze, print_maze, is_wall, place_player, move, can_move, game_loop, get_path, main) where 

import System.Environment

maze_path = "/Users/mattpaver/Downloads/a3unix/maze2.txt"

-- Useful code from Lecture 25
-- You may use this freely in your solutions

get :: [String] -> Int -> Int -> Char
get maze x y = (maze !! y) !! x 

modify_list :: [a] -> Int -> a -> [a]
modify_list list pos new =
    let
        before = take  pos    list
        after  = drop (pos+1) list
    in
        before ++ [new] ++ after

set :: [String] -> Int -> Int -> Char -> [String]
set maze x y char = 
    let
        line = maze !! y
        new_line = modify_list line x char
        new_maze = modify_list maze y new_line
    in
        new_maze

---- Part A

-- Question 1

get_maze :: String -> IO [String]
get_maze x = do
    mazeContent <- readFile x
    return (lines mazeContent)

-- Question 2

print_maze :: [String] -> IO ()
print_maze [] = return ()
print_maze (x:xs) = 
    do
        putStrLn x 
        print_maze xs

-- Question 3

is_wall :: [String] -> (Int, Int) -> Bool
is_wall m (x,y) =
    if get m x y == '#'
        then True
        else False

-- Question 4

place_player :: [String] -> (Int, Int) -> [String]
place_player maze (x, y) = 
  let 
    row = maze !! x
    prefix = take y row 
    symbol = '@' 
    suffix = drop (y + 1) row 
  in 
    take x maze ++ [prefix ++ [symbol] ++ suffix] ++ drop (x + 1) maze


---- Part B

-- Question 5

move :: (Int, Int) -> Char -> (Int, Int)
move (x,y) a
    |userinput =='w'=(x,y-1)
    |userinput =='s'=(x,y+1)
    |userinput =='a'=(x+1,y)
    |userinput =='d'=(x-1,y)
    |otherwise = (x,y)
    where userinput=a

-- Question 6

can_move :: [String] -> (Int, Int) -> Char -> Bool
can_move m (x,y) a = is_wall m (move (x,y) a)

-- Question 7

moveX :: (Int) -> Char -> (Int)
moveX (x) a
    |a =='w'=(x)
    |a =='s'=(x)
    |a =='a'=(x+1)
    |a =='d'=(x-1)
    |otherwise = (x)
    where userinput=a

moveY :: (Int) -> Char -> (Int)
moveY (y) a
    |a =='w'=(y-1)
    |a =='s'=(y+1)
    |a =='a'=(y)
    |a =='d'=(y)
    |otherwise = (y)
    where userinput=a

game_loop :: [String] -> (Int, Int) -> IO ()
game_loop m (x, y) =  do
    print_maze (place_player m (x, y))
    userinput <- getLine
    let firstchar = head userinput
    if ! can_move m (x,y) firstchar 
    then game_loop m (moveX x firstchar, moveY y firstchar)
    else game_loop m (x, y)

---- Part C

-- Question 8

get_path :: [String] -> (Int, Int) -> (Int, Int) -> [(Int, Int)]
get_path = error "Not implemented"

-- Question 9

main :: IO ()
main = error "Not implemented"
