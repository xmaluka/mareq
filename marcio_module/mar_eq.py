import numpy as np
import pandas as pd

# Dictionary which  gives sample mean, standard deviation, variance and other staticstics:
def data_summary(list1):
    data_summary={'mean':round(np.mean(list1),2),
                  'median':round(np.percentile(list1,50),2),
                  'min':round(min(list1),2),
                  'max':round(max(list1),2),
                  'std':round(np.std(list1,ddof=1),2)}
