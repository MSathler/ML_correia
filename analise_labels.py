import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import librosa

def salvar_csv(x_mean,y_mean,z_mean,x_desv,y_desv,z_desv,nome,tam_frequencia):
    dfdict = {}
    dfdict["Mean x"] = x_mean
    dfdict["Mean y"] = y_mean
    dfdict["Mean z"] = z_mean
    dfdict["Desv x"] = x_desv
    dfdict["Desv y"] = y_desv
    dfdict["Desv z"] = z_desv
    # dfdict["MFC y"] = mfcc
    # dfdict["Classificação 0 desalinhado 1 alinhado"] = classificacao
    df = pd.DataFrame(dfdict)
    nome = nome.split('.')
    nome = nome[0]
    print(nome)
    df.to_csv((str(nome) + '_tratado_SUP'+str(tam_frequencia)+'.csv'),index = False, header = True)#, columns=["Media x","Media y","Media z","Desv x","Desv y","Desv z","MFC y", "Classificação 0 desalinhado 1 alinhado"])
## 


if __name__ == '__main__':
    frequencia_de_coleta = 125
    velocidade_correia = 0.5 # m/s
    tamanho_correia = 1 # metros
    tamanho_coletas = 0.1 # metros
    # tam_frequencia = int(frequencia_de_coleta*tamanho_correia/velocidade_correia)
    tam_frequencia = 25

    dataset_file = pd.read_csv(sys.argv[1])
    x = dataset_file.iloc[:,0].values
    y = dataset_file.iloc[:,1].values
    z = dataset_file.iloc[:,2].values

    mean_x,mean_y,mean_z,desv_x,desv_y,desv_z,classificacao, fourier_y = [],[],[],[],[],[],[], []
    for i in range(0,len(x),tam_frequencia):
        mean_x.append(np.mean(x[i:i+tam_frequencia]))
        mean_y.append(np.mean(y[i:i+tam_frequencia]))
        mean_z.append(np.mean(z[i:i+tam_frequencia]))
        desv_x.append(np.std(x[i:i+tam_frequencia]))
        desv_y.append(np.std(y[i:i+tam_frequencia]))
        desv_z.append(np.std(z[i:i+tam_frequencia]))

    salvar_csv(mean_x,mean_y,mean_z,desv_x,desv_y,desv_z,sys.argv[1],tam_frequencia)

    dataset_file2 = pd.read_csv(sys.argv[2])
    x2 = dataset_file2.iloc[:,0].values
    y2 = dataset_file2.iloc[:,1].values
    z2 = dataset_file2.iloc[:,2].values

    mean_x2,mean_y2,mean_z2,desv_x2,desv_y2,desv_z2,classificacao2, fourier_y2 = [],[],[],[],[],[],[], []
    for i in range(0,len(x2),tam_frequencia):
        mean_x2.append(np.mean(x2[i:i+tam_frequencia]))
        mean_y2.append(np.mean(y2[i:i+tam_frequencia]))
        mean_z2.append(np.mean(z2[i:i+tam_frequencia]))
        desv_x2.append(np.std(x2[i:i+tam_frequencia]))
        desv_y2.append(np.std(y2[i:i+tam_frequencia]))
        desv_z2.append(np.std(z2[i:i+tam_frequencia]))

    salvar_csv(mean_x2,mean_y2,mean_z2,desv_x2,desv_y2,desv_z2,sys.argv[2],tam_frequencia)

    dataset_file3 = pd.read_csv(sys.argv[3])
    x3 = dataset_file3.iloc[:,0].values
    y3 = dataset_file3.iloc[:,1].values
    z3 = dataset_file3.iloc[:,2].values

    mean_x3,mean_y3,mean_z3,desv_x3,desv_y3,desv_z3 =  [],[],[],[],[],[]
    for i in range(0,len(x3),tam_frequencia):
        mean_x3.append(np.mean(x3[i:i+tam_frequencia]))
        mean_y3.append(np.mean(y3[i:i+tam_frequencia]))
        mean_z3.append(np.mean(z3[i:i+tam_frequencia]))
        desv_x3.append(np.std(x3[i:i+tam_frequencia]))
        desv_y3.append(np.std(y3[i:i+tam_frequencia]))
        desv_z3.append(np.std(z3[i:i+tam_frequencia]))

    salvar_csv(mean_x3,mean_y3,mean_z3,desv_x3,desv_y3,desv_z3,sys.argv[3],tam_frequencia)

    dataset_file4 = pd.read_csv(sys.argv[4])
    x4 = dataset_file4.iloc[:,0].values
    y4 = dataset_file4.iloc[:,1].values
    z4 = dataset_file4.iloc[:,2].values

    mean_x4,mean_y4,mean_z4,desv_x4,desv_y4,desv_z4 =  [],[],[],[],[],[]
    for i in range(0,len(x4),tam_frequencia):
        mean_x4.append(np.mean(x4[i:i+tam_frequencia]))
        mean_y4.append(np.mean(y4[i:i+tam_frequencia]))
        mean_z4.append(np.mean(z4[i:i+tam_frequencia]))
        desv_x4.append(np.std(x4[i:i+tam_frequencia]))
        desv_y4.append(np.std(y4[i:i+tam_frequencia]))
        desv_z4.append(np.std(z4[i:i+tam_frequencia]))

    salvar_csv(mean_x4,mean_y4,mean_z4,desv_x4,desv_y4,desv_z4,sys.argv[4],tam_frequencia)

    
    
        # classificacao.append(0)   
    # salvar_csv(media_x,media_y,media_z,desv_x,desv_y,desv_z,sys.argv[1],tam_frequencia)
    
    # plt.plot(media_y,'-*',label = "Alinhado")
    # plt.plot(media_y2,label = "Deslinhado")
    plt.plot(np.arange(len(mean_y)),mean_y,label = "Alinhado")
    plt.plot(np.arange(start = len(mean_y),stop = len(mean_y2)+len(mean_y)),mean_y2,label = "Desalinhado 1")
    plt.plot(np.arange(start = len(mean_y2)+len(mean_y), stop =len(mean_y3)+len(mean_y2)+len(mean_y)),mean_y3,label = "Desalinhado 2")
    plt.plot(np.arange(start = len(mean_y3)+len(mean_y2)+len(mean_y), stop =len(mean_y3)+len(mean_y2)+len(mean_y)+len(mean_y4)),mean_y4,label = "Transitorio")
    plt.legend()
    plt.xlabel("Coletas")
    plt.ylabel("Aceleração Média (m/s²)")
    plt.show()
    