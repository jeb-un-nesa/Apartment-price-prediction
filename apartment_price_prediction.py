import csv
import numpy
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression


def find_price_range_map(price_sqft):
    if price_sqft >= 500 and price_sqft < 1000:
        return 1
    elif price_sqft >= 1000 and price_sqft < 1500:
        return 2
    elif price_sqft >= 1500 and price_sqft < 2000:
        return 3
    elif price_sqft >= 2000 and price_sqft <2500:
        return 4
    elif price_sqft >=2500 and price_sqft <3000:
        return 5
    elif price_sqft >= 3000 and price_sqft <4000:
        return 6
    else:
        return 7



read_file_name = 'kc_house_data.csv'
train_data=[]
train_target=[]
with open(read_file_name, 'rt') as csv_file:
    count = 0
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in csv_reader:
        if count > 0 and count<=14000:
              temp=[]
              price=float(row[2])

              bedroom=float(row[3])
              temp.append(bedroom)
              bathroom=float(row[4])
              temp.append(bathroom)
              sqft_living=float(row[5])
              area=find_price_range_map(sqft_living)
              temp.append( area)
              sqft_lot=float(row[6])
              temp.append(sqft_lot)
              floor_chng=row[7].replace('"','')
              floors=float(floor_chng)
              temp.append(floors)
              condition=float(row[10])
              temp.append(condition)
              grade=float(row[11])
              temp.append(grade)
              sqft_above = float(row[12])
              temp.append(sqft_above)
              sqft_base = float(row[13])
              temp.append(sqft_base)
              yr_built=float(row[14])
              temp.append(yr_built)
              zip_code_chng=row[16].replace('"','')
              zip_code=float(zip_code_chng)
              temp.append(zip_code)
              lat=float(row[17])
              temp.append(lat)
              long=float(row[18])
              temp.append(long)
              train_data.append(temp)
              train_target.append(price)

        count+=1


        # for testing data
test_data=[]
test_target=[]
with open(read_file_name, 'rt') as csv_file:
    count = 0
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in csv_reader:
        if count > 14000:
              predict=[]
              price=float(row[2])
              bedroom=float(row[3])
              predict.append(bedroom)
              bathroom=float(row[4])
              predict.append(bathroom)
              sqft_living=float(row[5])
              area=find_price_range_map(sqft_living)
              predict.append(sqft_living)
              sqft_lot=float(row[6])
              predict.append(sqft_lot)
              floor_chng=row[7].replace('"','')
              floors=float(floor_chng)
              predict.append(floors)
              condition=float(row[10])
              predict.append(condition)
              grade=float(row[11])
              predict.append(grade)
              sqft_above = float(row[12])
              predict.append(sqft_above)
              sqft_base = float(row[13])
              predict.append(sqft_base)
              yr_built=float(row[14])
              predict.append(yr_built)
              zip_code_chng=row[16].replace('"','')
              zip_code=float(zip_code_chng)
              predict.append(zip_code)
              lat=float(row[17])
              predict.append(lat)
              long=float(row[18])
              predict.append(long)
              test_data.append(predict)
              test_target.append(price)


        count+=1


####### nearest neighbor algorithm
neigh = KNeighborsRegressor(n_neighbors=50)
neigh.fit(train_data, train_target)
predicted_price = neigh.predict(test_data)
# print(predicted_price)
error = 0.0
for i in range(0, len(predicted_price)):
    error += (abs(test_target[i] - predicted_price[i]) / test_target[i])
error = error / len(predicted_price)
accuracy = 100.0 - (error * 100.0)
print("Predicted Apartment price :"+str(accuracy))



