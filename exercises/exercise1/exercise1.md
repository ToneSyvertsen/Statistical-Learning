```

dataset = pd.read_csv('ex1data1.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

plt.scatter(X, y, color = 'red')
```

This is the plots from the data:


￼![The plot](https://github.com/ToneSyvertsen/Statistical-Learning/blob/master/exercises/exercise1/plot_ex1.png)


Then I try making a prediction
```
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
Out[177]: LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

y_pred = regressor.predict(X)

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Population vs Profit')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

```

![The plot](https://github.com/ToneSyvertsen/Statistical-Learning/blob/master/exercises/exercise1/plot_pred_ex1.png)

If this is the correct way of doing it, seems strange ;)
It seems like the biggest towns is the most profitable once..
With a few exceptions..


I splitted it into two as we have learned.

```
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
```

Then I made the regressors and fit's and the prediction varible for the test set
```
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
Out[171]: LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

y_pred = regressor.predict(X_test)

```
Then I made the plot for the training set

```
y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

```
![Test](https://github.com/ToneSyvertsen/Statistical-Learning/blob/master/exercises/exercise1/ex1_test_set.png)

￼
And at last I made the plot for the test set with the prediction

```

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Test set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show() 

```

￼![Training](https://github.com/ToneSyvertsen/Statistical-Learning/blob/master/exercises/exercise1/ex1_trainingset.png)


