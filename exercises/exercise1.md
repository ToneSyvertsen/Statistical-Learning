dataset = pd.read_csv('ex1data1.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


I splitted it into two as we have learned.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
/Applications/anaconda/lib/python3.5/site-packages/sklearn/cross_validation.py:44: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
  "This module will be removed in 0.20.", DeprecationWarning)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
Out[171]: LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Training set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

![Test](Statistical-Learning/exercises/ex1 test set.png)
￼

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Population vs Profit (Test set)')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

￼![Training](Statistical-Learning/exercises/ex1 trainingset.png)
