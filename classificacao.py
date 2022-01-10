import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import GradientBoostingClassifier
import pickle


# load data from excel

dataset_file = pd.read_csv("alinhado_separados_superior_tratado_SUP25.csv")
dataset_file1 = pd.read_csv("desalinhado1_separados_superior_tratado_SUP25.csv")
dataset_file2 = pd.read_csv("desalinhado2_separados_superior_tratado_SUP25.csv")
dataset_file3 = pd.read_csv("transitorio_separados_superior_tratado_SUP25.csv")

X_1 = np.array(dataset_file.iloc[:,0:6].values).reshape(-1,6)#int(len(dataset_file.iloc[:,0].values)/25),-1)
X_2 = np.array(dataset_file1.iloc[0:25*4,0:6].values).reshape(-1,6)#int(len(dataset_file1.iloc[:,0].values)/25),-1)
X_3 = np.array(dataset_file2.iloc[0:25*5,0:6].values).reshape(-1,6)#int(len(dataset_file2.iloc[:,0].values)/25),-1)
X_4 = np.array(dataset_file3.iloc[0:25*1,0:6].values).reshape(-1,6)#int(len(dataset_file3.iloc[:,0].values)/25),-1)

X = np.concatenate((X_1,X_2,X_3,X_4))

y_1 = np.ones(X_1.shape[0])
# y_2 = np.ones(X_2.shape[0]) * 2
# y_3 = np.ones(X_3.shape[0]) * 3
y_2 = np.zeros(X_2.shape[0])
y_3 = np.zeros(X_3.shape[0])
y_4 = np.zeros(X_4.shape[0])
y = np.concatenate((y_1,y_2,y_3,y_4))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


rf_results = []
GB_results = []

num_rodadas = 10
num_tree = 25
profundidade_maxima = 30
for x in range(num_rodadas):
    # treino e teste  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)

    # GB Model
    gb_obj = GradientBoostingClassifier(n_estimators=10, learning_rate=0.1,max_depth=5).fit(X_train, y_train)
    gb_y_pred = gb_obj.predict(X_test)
    GB_results.append(accuracy_score(y_test, gb_y_pred))

    # Random Forest_model   
    rand_forest_model = RandomForestClassifier(n_estimators=num_tree,max_depth=profundidade_maxima)
    rand_forest_model.fit(X_train, y_train)
    # predicting     
    rf_y_pred = rand_forest_model.predict(X_test)
    rf_results.append(accuracy_score(y_test, rf_y_pred))


plt.plot(rf_results, label="Random Forest") 
plt.plot(GB_results,label = "Gradient Boosting")
plt.ylim([0,1])
plt.legend()
plt.show()

importance = rand_forest_model.feature_importances_
a = ['Media x', 'Media y', 'Media z', 'Desvio P x', 'Desvio P y', 'Desvio P z'] # 'MFC y'

plt.bar([x for x in a],importance)
plt.title("Gráfico de Importância das Entradas")
plt.xlabel("Entradas")
plt.ylabel("Importância")
plt.show()



filename = 'RF_trained_model.sav'
pickle.dump(rand_forest_model, open(filename, 'wb'))

filename = 'GB_trained_model.sav'
pickle.dump(gb_obj, open(filename, 'wb'))


#RF
print("Precisao RF {:.2f}%".format(np.mean(rf_results)*100))
print("Desvio Padrao RF {:.4f}".format(np.std(rf_results)))
print('Random Forest confusion matrix ultimo treino = \n'+ str(confusion_matrix(y_test, rf_y_pred)))

#GB
print("Precisao GB {:.2f}%".format(np.mean(GB_results)*100))
print("Desvio Padrao GB {:.4f}".format(np.std(GB_results)))
print('Random Forest confusion matrix ultimo treino = \n'+ str(confusion_matrix(y_test, gb_y_pred)))
