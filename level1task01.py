import pandas as pd
import numpy as np

# --- 1. Create dataset with intentional issues ---
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           1, 2, 3, 4, 5, 11, 12, 13, 14, 15],  # duplicate IDs
    "Name": ["Person_" + str(i) for i in range(1, 21)],
    "Age": [25, 30, np.nan, 22, 28, 35, 40, np.nan, 29, 31, 
            25, 30, np.nan, 22, 28, 33, 24, 36, np.nan, 32],
    "Department": ["hr", "IT", "Finance", "it", np.nan, "HR", 
                   "finance", "IT", "Finance", "hr",
                   "HR", "IT", "finance", "it", "finance",
                   "Finance", "hr", "IT", "Finance", np.nan],
    "Salary": [50000, 60000, 55000, 45000, 52000, np.nan, 
               62000, 58000, 49000, 61000, 
               50000, 60000, 55000, 45000, 52000,
               56000, 60000, 48000, 51000, np.nan],
    "Experience": [2, 5, 3, np.nan, 4, 7, 10, 6, np.nan, 5,
                   2, 5, 3, np.nan, 4, 6, np.nan, 8, 7, 3],
    "JoiningDate": ["2020-01-15", "2019/03/20", np.nan, "10-06-2021", "2020-07-25",
                    "30-11-2018", "2017/05/18", "2021-09-12", np.nan, "22-08-2019",
                    "2020/10/05", "14-01-2019", np.nan, "2018/07/19", "01-03-2017",
                    "2020-02-28", "11-06-2019", "2021-04-09", "2020-12-01", np.nan]
}

df = pd.DataFrame(data)

print("🔹 Original Dataset:\n", df.head(), "\n")