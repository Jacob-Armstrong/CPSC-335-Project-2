from itertools import combinations

def Dynamic_Programming(n, stocks_and_values, amount):
    dp = [(0, []) for _ in range(amount + 1)]

    for stock in stocks_and_values:
        for j in range(amount, stock[1] - 1, -1):
            if stock[0] + dp[j - stock[1]][0] > dp[j][0]:
                dp[j] = (stock[0] + dp[j - stock[1]][0], dp[j - stock[1]][1] + [stock])

    return dp[amount]

def Exhaustive_Search(n, stocks_and_values, budget):
    max_value = 0
    selected_stocks = []

    for r in range(1, n + 1):
        for stocks_n_values in combinations(stocks_and_values, r):
            total = sum(stock[1] for stock in stocks_n_values)
            if total <= budget:
                stocks = sum(stock[0] for stock in stocks_n_values)
                if stocks > max_value:
                    max_value = stocks
                    selected_stocks = list(stocks_n_values)

    return max_value, selected_stocks

def Parse_File():
    with open('input.txt', 'r') as file:
        content = file.read()

    sections = content.split('Sample input')[1:]

    for i, section in enumerate(sections, start=1):
        # File Parsing
        n_index = section.find('N = ')
        n_end = section.find('\n', n_index)
        n = int(section[n_index + len('N = '):n_end].strip())

        stocks_index = section.find('Stocks and values = ')
        stocks_end = section.find('].', stocks_index)
        stocks_str = section[stocks_index + len('Stocks and values = '):stocks_end + 1]
        stocks = eval(stocks_str)
        stocks = [list(map(int, pair)) for pair in stocks]

        amount_index = section.find('Amount = ')
        amount_end = section.find('\n', amount_index)
        if amount_end == -1:
          amount_end = len(section)
        else:
          amount_end = section.find('\n', amount_index)
        amount = int(section[amount_index + len('Amount = '):amount_end].strip())

        # File Output
        if i > 9:
          print("=============")
          print(f"= Sample {i} =")
          print("=============\n")
        else:
          print("============")
          print(f"= Sample {i} =")
          print("============\n")

        print("N:", n)
        print("Stocks and Values:", stocks)
        print("Amount:", amount, "\n")
        #print("--------------------")

        print("<< Part A: Exhaustive Search >>")
        es_result = Exhaustive_Search(n, stocks, amount)
        max_value, selected_stocks = es_result
        print("Maximum value:", max_value)
        print("Selected stocks:", selected_stocks, "\n")

        print("<< Part B: Dynamic Programming >>")
        result = Dynamic_Programming(n, stocks, amount)
        max_value, selected_stocks = result
        print("Maximum value:", max_value)
        print("Selected stocks:", selected_stocks, "\n")

Parse_File()
