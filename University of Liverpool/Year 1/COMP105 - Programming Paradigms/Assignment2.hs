-- Do not alter the following line
module Assignment2 (transaction_to_string, trade_report_list, stock_test, get_trades, trade_report, update_money, profit, profit_report, complex_profit_report) where


type Transaction = (Char, Int, Int, String, Int) 

test_log :: [Transaction]
test_log = [('B', 100, 1104,  "VTI",  1),
            ('B', 200,   36, "ONEQ",  3),
            ('B',  50, 1223,  "VTI",  5),
            ('S', 150, 1240,  "VTI",  9),
            ('B', 100,  229, "IWRD", 10),
            ('S', 200,   32, "ONEQ", 11), 
            ('S', 100,  210, "IWRD", 12)
            ]

-- Part A


transaction_to_string :: Transaction -> String
transaction_to_string (action, units, price, stocks, day) = 
    let transaction_type | action == 'B' = "Bought "
                | action == 'S' = "Sold "
                | otherwise     = "Incorrect, please input either B for bought or S for sold. " 
        transaction_units = show units ++ " units of "
        transaction_stocks = stocks ++ " for "
        transaction_price = show price ++ " pounds each on day "
        transaction_day = show day
    in
        transaction_type ++ transaction_units ++ transaction_stocks ++ transaction_price ++ transaction_day


trade_report_list :: [Transaction] -> [String]
trade_report_list x = map transaction_to_string x


stock_test :: String -> Transaction -> Bool
stock_test x (_, _, _, y, _) = x == y


get_trades :: String -> [Transaction] -> [Transaction]
get_trades x = filter (stock_test x)


trade_report :: String -> [Transaction] -> String
trade_report x y = unlines(trade_report_list((get_trades x y)))



-- Part B

update_money :: Transaction -> Int -> Int
update_money (action, units, price, stocks, day) current_money = 
    let money_type  | action == 'B' = current_money - units * price
                    | action == 'S' = current_money + units * price
                    | otherwise     = 0
    in
        money_type


profit :: [Transaction] -> String -> Int
profit x y  = foldr(update_money) 0 (get_trades y x)

profit_report :: [String] -> [Transaction] -> String
profit_report [] y=""
profit_report (x:xs) y =
    let display_profit = profit y x
    in
        (x)++": "++ (show display_profit) ++"\n"++profit_report xs y

-- Part C


test_str_log = "BUY 100 VTI 1\nBUY 200 ONEQ 3\nBUY 50 VTI 5\nSELL 150 VTI 9\nBUY 100 IWRD 10\nSELL 200 ONEQ 11\nSELL 100 IWRD 12\n"



type Prices = [(String, [Int])]

test_prices :: Prices
test_prices = [
                ("VTI", [1689, 1785, 1772, 1765, 1739, 1725, 1615, 1683, 1655, 1725, 1703, 1726, 1725, 1742, 1707, 1688, 1697, 1688, 1675]),
                ("ONEQ", [201, 203, 199, 199, 193, 189, 189, 183, 185, 190, 186, 182, 186, 182, 182, 186, 183, 179, 178]),
                ("IWRD", [207, 211, 213, 221, 221, 222, 221, 218, 226, 234, 229, 229, 228, 222, 218, 223, 222, 218, 214])
              ]



complex_profit_report :: String -> Prices -> String
complex_profit_report = error "not implemented"