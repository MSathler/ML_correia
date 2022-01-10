import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


def salvar_csv(x_mean,y_mean,z_mean,nome):
    dfdict = {}
    dfdict["Mean x"] = x_mean
    dfdict["Mean y"] = y_mean
    dfdict["Mean z"] = z_mean

    df = pd.DataFrame(dfdict)
    nome = nome.split('.')
    nome = nome[0]
    print("Arquivo criado com o nome: \033[32m" + str(nome) + '_superior.csv')
    df.to_csv((str(nome) + '_superior.csv'),index = False, header = True)#, columns=["Mean x","Mean y","Mean z","Desv x","Desv y","Desv z","MFC y", "Classificação 0 desalinhado 1 alinhado"])



if __name__ == '__main__':
    # frequencia_de_coleta = 125
    velocidade_correia = 0.5 # m/s
    tamanho_correia = 1 # metros
    tamanho_coletas = 0.1 # metros
    # tam_frequencia = int(frequencia_de_coleta*tamanho_correia/velocidade_correia)

    if len(sys.argv) > 2: 
        tam_frequencia = int(sys.argv[2])
    else:
        tam_frequencia = 10


    dataset_file = pd.read_csv(sys.argv[1])
    x = dataset_file.iloc[:,0].values
    y = dataset_file.iloc[:,1].values
    z = dataset_file.iloc[:,2].values
    
    plt.plot(y)
    plt.title("Raw data on the y-axis")
    plt.show()

    n = []
    mean_x,mean_y,mean_z,desv_x,desv_y,desv_z,classificacao = [],[],[],[],[],[],[]
    new_x,new_y,new_z = [], [], []

    # Make a moving average to separete the intervals // Faz uma média movel para ver separar os intervals
    for i in range(0,len(y),tam_frequencia):
        
        mean_x.append(np.mean(x[i:i+tam_frequencia]))
        mean_y.append(np.mean(y[i:i+tam_frequencia]))
        mean_z.append(np.mean(z[i:i+tam_frequencia]))
        
    cont_i, cont_s = 0,0
    begin_interval, end_interval = [], []
    
    if mean_y[0]> 0:
        begin_interval.append(0) ## Case the read starts on the top // caso a leitura começe no topo da correia


    # With well defined intervals its possible to split the top values  // Com o interval bem definido separa-se os pontos superiores
    for w in range(0,len(mean_y)):
        if mean_y[w]>=0.0:# and (y[i] - y[i-1])>=0.1:
            if cont_i > 2:
                begin_interval.append(w*tam_frequencia)
            n.append(w)
            new_x.append(mean_x[w])
            new_y.append(mean_y[w])
            new_z.append(mean_z[w])
            cont_s += 1
            cont_i = 0
        else:
            if cont_s > 2:
                end_interval.append(w*tam_frequencia)
            cont_i +=1
            cont_s = 0
            
    plt.plot(mean_y)
    plt.title("Average of the data in y note: If the data in the upper part does not keep above 0, change the average value, which is " + str(tam_frequencia))
    plt.show()
    
    if mean_y[0]<= 0:
        end_interval.append(len(y))

    # Makes both lists with same lenght # Deixar as duas listas do mesmo tamanho
    while len(begin_interval) > len(end_interval):
        begin_interval.pop(-1)
    while len(begin_interval) < len(end_interval):
        end_interval.pop(-1)

    x_sup, y_sup, z_sup, interval_s, interval_i = [], [], [], [], []

    ## Create a new top vector # Cria um novo vetor superior
    for i in range(len(begin_interval)):
        x_sup.append(x[begin_interval[i]:end_interval[i]])
        y_sup.append(y[begin_interval[i]:end_interval[i]])
        z_sup.append(z[begin_interval[i]:end_interval[i]])
        interval_s.append(np.arange(begin_interval[i],end_interval[i]))


    x = np.concatenate(np.array(interval_s, dtype="object"))
    x_dados_s = np.concatenate(np.array(x_sup, dtype="object"))
    y_dados_s = np.concatenate(np.array(y_sup, dtype="object"))
    z_dados_s = np.concatenate(np.array(z_sup, dtype="object"))


    ## Save data
    if len(sys.argv) > 3 and sys.argv[3] == "save": 
        salvar_csv(x_dados_s,y_dados_s,z_dados_s,sys.argv[1])
    
    # salvar_csv(x_dados_s,y_dados_s,z_dados_s,sys.argv[1])

    plt.plot(y, linewidth = 2, label = "Original")
    plt.plot(x,y_dados_s, linewidth = 0.5, label = "Top Values")
    plt.title("Graph for analysis")
    plt.legend()
    plt.show()

    plt.title("Data without bottom part")
    plt.plot(y_dados_s)
    plt.show()

    