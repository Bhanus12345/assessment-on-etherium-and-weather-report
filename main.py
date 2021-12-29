import yfinance as yf
from datetime import datetime
import requests, json
from wwo_hist import retrieve_hist_data
import matplotlib.pyplot as plt
plt.style.use('default')

def EthereumDataPull(today,start_date):
    # diownlaoding ETH-USD data and saving it in a dataframe

    eth_df = yf.download('ETH-USD',start_date, today)
    return eth_df



def weatherDataPull(today,start_date):
    frequency = 3
    # api key to retrive historical data
    api_key = 'f5dde6f78c73407facc203054212912'
    location_list = ['california']
    hist_weather_data = retrieve_hist_data(api_key,
                                    location_list,
                                    start_date,
                                    today,
                                    frequency,
                                    location_label = False,
                                    export_csv = True,
                                    store_df = True)
    return hist_weather_data[0]


def graph(today,start_date):
    # calling EthereumDataPull function
    eth_df=EthereumDataPull(today,start_date)
    # calling weatherDataPull function
    weather_df=weatherDataPull(today,start_date)
    weather_df=weather_df.set_index('date_time')
    plt.figure(figsize=(16, 8), dpi=150)
    weather_df["maxtempC"] = weather_df["maxtempC"].astype(str).astype(int)
    weather_df["mintempC"] = weather_df["mintempC"].astype(str).astype(int)
    weather_df["humidity"] = weather_df["humidity"].astype(str).astype(int)
    # using plot method to plot open prices.
    eth_df['Close'].plot(label='ETH-USD', color='orange')
    weather_df['maxtempC'].plot(label='MaxtempC')
    weather_df['mintempC'].plot(label='MintempC')
    weather_df['humidity'].plot(label='Humidity')
    # adding title to the plot
    plt.title('Change of price and weather with time')
    # adding Label to the x-axis
    plt.xlabel('Date')
    # adding legend to the curve
    plt.legend()
    
    plt.show()
    
    
    

if __name__ == '__main__':
    today = datetime.today().strftime('%Y-%m-%d')
    start_date = '2021-11-01'
    graph(today,start_date)
