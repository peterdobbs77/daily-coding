import numpy as np
from sklearn import linear_model

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    # prep data
    X = np.array(marketing_expenditure)
    X = X.reshape(-1,1)
    Y = np.array(units_sold)
    Y = Y.reshape(-1,1)
    # fit model
    slr = linear_model.LinearRegression()
    slr.fit(X,Y)
    #print ('Slope =', slr.coef_[0])
    #print ('Intercept =', slr.intercept_)
    # use model parameters to predict
    ypred = (desired_units_sold - slr.intercept_)/(slr.coef_[0])
    return ypred

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))
