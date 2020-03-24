# A company stores login data and password hashes in two different containers:
#   * `DataFrame` with columns: `Id`, `Login`, `Verified`.
#   * Two-dimensional `NumPy` `array` where each element is an array that contains: `Id` and `Password`.
# Elements on the same row/index have the same `Id`.
#
# Implement the function login_table that accepts these two containers and modifies
# id_name_verified DataFrame in-place, so that:
#   * The `Verified` column should be removed.
#   * The password from NumPy array should be added as the last column with the name "Password" to DataFrame.

import pandas as pd
import numpy as np


def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.   
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place. 
              It should not return anything.
    """
    id_name_verified.drop(['Verified'], inplace=True, axis=1)
    id_name_verified['Password'] = id_password[:, 1]


id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [
                                2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)
login_table(id_name_verified, id_password)
print(id_name_verified)
