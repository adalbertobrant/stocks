# creation of asset object
import yahoo_fin.stock_info as si # next version use open BB sdk from didier rodrigues lopes
import datetime
import pandas as pd
import numpy as np
import os
from datetime import date, timedelta
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model


class Stock:
  def __init__(self, symbol):
    self.symbol = symbol
    self.last_day =  self.get_last_day()
    self.live_price = self.get_live_data()
    self.historical_data = self.get_history()
    self.tomorrow = self.get_prev()

  def get_last_day(self):
    # need to put the time acording to local gmt -> next version
    startdate = date.today()-timedelta(days=1)
    startdate  = startdate.strftime('%m-%d-%Y')
    self.last_day = si.get_data(self.symbol, start_date = startdate)
    self.last_day['Date'] = self.last_day.index
    self.last_day = self.last_day[['Date', 'open','high','low','close','adjclose','volume']]
    self.last_day.reset_index(drop=True, inplace=True)
    return self.last_day

  def get_live_data(self):
    self.live_price = si.get_live_price(self.symbol)
    return self.live_price

  def get_history(self):
    self.historical_data = si.get_data(self.symbol)
    self.historical_data['Date'] = self.historical_data.index
    self.historical_data = self.historical_data[['Date', 'open', 'high','low', 'close', 'adjclose', 'volume']]
    self.historical_data.reset_index(drop=True, inplace=True)
    return self.historical_data


  def get_prev(self):
    directory = "./models"
    file_name = f"{self.symbol}_.h5"
    if file_name in os.listdir(directory):
      stock_model = load_model(f"./models/{file_name}")
      features = self.last_day
      features = features.drop(columns=['Date'])
      features = features.drop(columns=['close'])
      print(features)
      prev = np.array(features)
      prediction = stock_model.predict(prev)
      return prediction[0][0]
    else:
      # ask and explain if the person wants to train a specific model
      # explain that the window for the trainning will be for the last five days
      # explain that the trainned model will be in the ./models directory
      # do the trainning 
      # after the model is trainned run get_prev() again and return the prediction
      return 0
