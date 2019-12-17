from sklearn.ensemble import RandomForestRegressor
from datetime import datetime
import pandas as pd

# tweets = pd.read_excel('./NLP/201910_Tweets.xlsx')
tweets = pd.read_csv('./NLP/5000tweets.csv')
stocks = pd.read_csv('./NLP/Oct_Price.csv')
stocks = stocks.sort_values('Date')

price_by_day = {}

for index, line in stocks.iterrows():
    # TODO: calculate difference to previous day
    if line['NAME'] == 'TESCO PLC':
        price_by_day[line['Date']] = line

tweets['TIMESTAMP'] = ''
tweets['PX_HIGH'] = 0
tweets['PX_LOW'] = ''
tweets['PX_OPEN'] = ''
tweets['PX_VOLUME'] = ''
for index, line in tweets.iterrows():
    day = line['Date']
    # 2019-10-24 14:06:58.0
    parsed = datetime.strptime(day, '%Y-%m-%d %H:%M:%S.%f')
    formatted = parsed.strftime('%d/%m/%Y')
    if formatted in price_by_day:
        line['TIMESTAMP'] = parsed.timestamp()
        line['PX_HIGH'] = price_by_day[formatted]['PX_HIGH']
        line['PX_LOW'] = price_by_day[formatted]['PX_LOW']
        line['PX_OPEN'] = price_by_day[formatted]['PX_OPEN']
        line['PX_VOLUME'] = price_by_day[formatted]['PX_VOLUME']


# X, y = make_regression(n_features=4, n_informative=2,
# regr = RandomForestRegressor(max_depth=2, random_state=0)
# X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
# regr.fit(X, y)
# RandomForestRegressor(max_depth=2, random_state=0)
# print(regr.predict([[0, 0, 0, 0]]))

X = tweets[['Twitter Following', 'Impact', 'Sentiment']]
y = tweets[['PX_HIGH']]
# y = tweets[['CHANGE_FROM_PREVIOUS_DAY']]

regr = RandomForestRegressor(max_depth=10, random_state=0)
regr.fit(X, y)



print(tweets[0])

# print(price_by_day)

# tweets.sort('date')

print('great')

