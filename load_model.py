import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import GradientBoostingClassifier
import pickle

ex_new_data = np.array([1,1,2,1,2,3]).reshape(1,-1)

loaded_model = pickle.load(open("RF_trained_model.sav", 'rb'))
result = loaded_model.predict(ex_new_data)
if result[0] == 0:
    print(f"O resultado da precição é {result[0]} ---> Desalinhado <---")
else:
    print(f"O resultado da precição é {result[1]} ---> Alinhado <---")