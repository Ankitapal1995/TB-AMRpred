from sys import argv
s,ml_model,test_ml_file,k=argv

import numpy as np, matplotlib.pyplot as plt,  pandas as pd
from sklearn.model_selection import cross_val_score,cross_val_predict,  KFold,  LeaveOneOut, StratifiedKFold
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
#from sklearn import 
############################ xgb libraries ##############################
import xgboost as xgb
from xgboost import XGBClassifier
#import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from numpy import asarray
from numpy import savetxt
import pickle
#from keras.callbacks import Callback
print(test_ml_file.split("_")[0]+"_"+k+"_xgb_prediction.csv")
'''############################ ann dl libraries ###########################3
import shap
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#export TF_CPP_MIN_LOG_LEVEL="2"
print(xgb.__version__)'''

'''########################################### DL-ANN LOAD MODEL ##################################################

load_model_ann=tf.keras.models.load_model(dl_model)

########################################## DL-ANN TEST DATASET LOAD AND EVALUATION ##################################


# load the test dataset for model prediction
dl_dataset = pd.read_csv(test_dl_file,delimiter=',',header=None)
# split into input (X) and output (y) variables
X_dl = dl_dataset.iloc[:, :-1].values
Y_dl = dl_dataset.iloc[:, -1].values

##print(X_dl.shape)
##print(X_dl)
##print(dim)
# make probability predictions with the model
predictions_dl = load_model_ann.predict(X_dl).astype(int)
# round predictions 
rounded = [round(x[0]) for x in predictions_dl]'''

'''# summarize the first 5 cases
for i in range(len(predictions_dl)):
        ##print('%s => %d (expected %d)' % (x_test[i].tolist(), predictions[i], y_test[i]))
    print('%d (expected %d)' % (predictions_dl[i], Y_dl[i]))'''


'''from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
from sklearn.metrics import accuracy_score,roc_auc_score
######################################### CALCULATING THRESHOLDS ANN MODEL #####################################
thres_ann=1
pred_dl_ml=[]
for i in predictions_dl:
    if i >=thres_ann:
       pred_dl_ml.append("resistant")
    else:
       pred_dl_ml.append("susceptible")

#print(f"ann prediction: {''.join(pred_cut_off_dl)}")'''

       

################################### XGBOOST SAVED MODEL LOADING ##################################
#booster= xgboost.Booster()
loaded_model_xgb = pickle.load(open(ml_model, 'rb'))
#loaded_model = pickle.load(open('saved_model_3800_3800_iso_res_sus_4838_mut_prof_for_ml.sav', 'rb'))

################################## XGBOOST TEST DATASET LOADING AND EVALUATION ########################

#loading test dataset for xgboost algorithm
dataset_ml = pd.read_csv(test_ml_file, sep=',')
# split into input (X) and output (y) variables
X_ml = dataset_ml.iloc[:, :-1].values
Y_ml = dataset_ml.iloc[:, -1].values

##print(X_ml.shape)


# make probability predictions with the model
y_pred = loaded_model_xgb.predict(X_ml)
predictions_ml=[round(x) for x in y_pred]


# In[18]:

cm_ml = confusion_matrix(Y_ml, predictions_ml)
#print(f"xgb cm: {cm_ml}")
######################################### CALCULATING THRESHOLDS XGB #####################################
#print(predictions_ml)
pred_dl_ml=[]
thres_xgb=1
#pred_cut_off_ml=[]
for i in predictions_ml:
    if i >=thres_xgb:
       pred_dl_ml.append("R")
       #print("resistant")
    else:
        pred_dl_ml.append("S")
       #print("susceptible")


#print(pred_dl_ml)
'''prepf=[]
if test_ml_file.count('.')==3:
    prepf.append(test_ml_file.split('.')[:2])
else:
    prepf.append(test_ml_file.split('.')[:1])
output_file=''.join(prepf)'''
output_file=test_ml_file.split("_")[0]
fo=open(output_file+".csv"+"_"+k+"_xgb_prediction.csv","w")
fo.write(','.join(pred_dl_ml))
fo.write("\t")
fo.write(k)
fo.write("\n")
fo.close()
