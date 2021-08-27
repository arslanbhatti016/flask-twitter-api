# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:25:32 2021

@author: IT City
"""

# import joblib
from joblib import load

# sample tweet text
text = ["@user #cnn calls #michigan middle school 'build the wall' chant '' #tcot  "]

# load the saved pipleine model
pipeline = load("../main/text_classification.joblib")

# predict on the sample tweet text
print(pipeline.predict(text))
## >> array([0])
