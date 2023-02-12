1. distribuir na internet

# Stock Data Analysis (assets_mon.py)

This program is a class for stock data that uses the yahoo_fin library to pull stock data for a given symbol. The class has several methods, including:

- `get_last_day`: returns data for the last trading day.
- `get_live_data`: returns the live price of the stock.
- `get_history`: returns historical data for the stock.
- `get_prev`: returns a prediction of the next day's closing price for the stock using pre-trained models.

The script loads pre-trained models specific to different stock symbols. The `get_prev` method checks the symbol of the stock and loads the corresponding pre-trained model to make a prediction for the next day's closing price. It also drops specific columns from the last day's data to prepare it for the prediction.

The script also uses the keras library for creating and loading models. It also uses the pandas library for data manipulation.

## Installation

stock = Stock('PETR4.SA')To install the dependencies from the `requirements.txt` file, navigate to the root directory of the project and run the following command:

```python
Copy code
pip install -r requirements.txt
```

This will install all the packages listed in the `requirements.txt` file in your environment.

and It is recommended to use a virtual environment for this project, you can use `virtualenv` or `conda` to create a virtual environment and then activate it, then install the dependencies.

## Usage

To use the class, you should import the class Stock and create an instance of the class passing the stock symbol as an argument.

You could try in a virtual env, importing everthing to python3 prompt.

```python
import assets_mon as ats
# stock object 
stock = ats.Stock('PETR4.SA')
# get_last_day() returns open, high, close, adj close and volume
print(stock.get_last_day())
# get_live_data() returns the price with some delay 
print(stock.get_live_data())
# get_history() returns all times historical data
print(stock.get_history())
# get_prev() return a prevision for the next day closing price
print(stock.get_prev())
```

For Brazilians stocks market you should use the stock symbol plus ' .sa ' -> ' petr4.sa ', this is needed to differentiate from others markets.

For American market you just need the stock symbol. Example -. ' aappl '

Please note that the pre-trained models are specific to the stocks symbols in the "stocks.txt" file located in the models directory. You can also use the class to get data from other stocks, but the prediction will not be available.

Please also note that the data returned by the methods are in the form of a pandas DataFrame, so you can use the pandas library to manipulate the data as you see fit.


# Stocks Monitor (monitor.py)

​	This is a Python example  program that allows the user  to input some stocks and retrieve their future closing price for the next trading day. The results are displayed in a rich table and also stored in a JSON file.

## Requirements

- Python 3.x

- rich library
- pandas library
- assets_mon library

## Usage

​	A list of stocks symbols is stored in a text file (./models/stocks.txt). The program reads the stocks symbols from the file and inputs each one to retrieve its future closing price.

​	The resulting rich table displays the stock symbol and the future closing price for each stock.

​	The resulting JSON file stores the stock symbol and the future closing price for each stock in JSON format. The file name is saved in ./json/stocks_json_dd-mm-yyyy.json.

## How to Run

1. Make sure you have installed the required libraries.
```python
Copy code
pip install -r install.txt
```
3. Run the monitor.py file.

```python
Copy code
python monitor.py
```

1. The results will be displayed in a rich table and also stored in a JSON file.

![Result from monitor.py](https://github.com/adalbertobrant/stocks/blob/main/screens/monitor_py.png)





