# Your task is to write a function to find the average closing price of a specified stock.

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

def average_price(list):
    sum = 0
    counter = 0
    stock = input("What stock? ")

    for item in stock_data:
        if item[0] == stock:
            sum = sum + item[2]
            counter = counter + 1
    print(sum / counter)
average_price(stock_data)
