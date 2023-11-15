with open('Input.txt', 'r') as file:
    content = file.read()

sections = content.split('Sample input')[1:]

def Parse_File():
    for i, section in enumerate(sections, start=1):
    
        # Number of stocks
        n_index = section.find('N = ')
        n_end = section.find('\n', n_index)
        N = int(section[n_index + len('N = '):n_end].strip())

        # Stocks and values
        stocks_index = section.find('Stocks and values = ')
        stocks_end = section.find('].', stocks_index)
        stocks_str = section[stocks_index + len('Stocks and values = '):stocks_end + 1]
        stocks_and_values = eval(stocks_str)

        # Convert the stocks_and_values into arrays of numbers
        stocks_and_values = [list(map(int, pair)) for pair in stocks_and_values]

        # Amount of resources
        amount_index = section.find('Amount = ')
        amount_end = section.find('\n', amount_index)
        Amount = int(section[amount_index + len('Amount = '):amount_end].strip())

        # Print the extracted values for each section
        print(f"Sample {i}:")
        print("N:", N)
        print("Stocks and Values:", stocks_and_values)
        print("Amount:", Amount)
        print("------")

        print("Beginning Exhaustive Search implementation for sample input " + str(i))
        Exhaustive_Search(N, stocks_and_values, Amount)
    
        print("Beginning Dynaming Programming implementation for sample input " + str(i))
        Dynamic_Programming(N, stocks_and_values, Amount)

        print("=================")

def Exhaustive_Search(N, stocks, Amount):
    pass

def Dynamic_Programming(N, stocks, Amount):
    pass

Parse_File()