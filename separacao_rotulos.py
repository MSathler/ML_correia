from numpy.core.defchararray import array
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import librosa

def salvar_csv(x_media,y_media,z_media,nome):
    dfdict = {}
    dfdict["x"] = x_media
    dfdict["y"] = y_media
    dfdict["z"] = z_media

    df = pd.DataFrame(dfdict)
    nome = nome.split('.')
    nome = nome[0]
    print(nome)
    df.to_csv((str(nome) + '_separados.csv'),index = False, header = True)#, columns=["Media x","Media y","Media z","Desv x","Desv y","Desv z","MFC y", "Classificação 0 desalinhado 1 alinhado"])




if __name__ == '__main__':
    frequencia_de_coleta = 125
    velocidade_correia = 0.5 # m/s
    tamanho_correia = 1 # metros
    tamanho_coletas = 0.1 # metros
    # tam_frequencia = int(frequencia_de_coleta*tamanho_correia/velocidade_correia)
    tam_frequencia = 1

    dataset_file = pd.read_csv(sys.argv[1])
    mediax = dataset_file.iloc[:,2].values
    mediay = dataset_file.iloc[:,3].values
    mediaz = dataset_file.iloc[:,4].values
    

    transitorio, alinhado, desalinhado1,desalinhado2 = [], [], [], []

    _transitorio1_x = np.array(mediax[0:1350])
    _transitorio1_y = np.array(-mediay[0:1350])
    _transitorio1_z = np.array(mediaz[0:1350])
    _transitorio2_x = np.array(mediax[10276:10875])
    _transitorio2_y = np.array(-mediay[10276:10875])
    _transitorio2_z = np.array(mediaz[10276:10875])
    _transitorio3_x = np.array(mediax[20176:21600])
    _transitorio3_y = np.array(-mediay[20176:21600])
    _transitorio3_z = np.array(mediaz[20176:21600])
    x_transitorio = np.concatenate((_transitorio1_x,_transitorio2_x,_transitorio3_x))
    y_transitorio = np.concatenate((_transitorio1_y,_transitorio2_y,_transitorio3_y))
    z_transitorio = np.concatenate((_transitorio1_z,_transitorio2_z,_transitorio3_z))


    _alinhado1_x = np.array(mediax[1351:10275])
    _alinhado1_y = np.array(-mediay[1351:10275])
    _alinhado1_z = np.array(mediaz[1351:10275])
    _alinhado2_x = np.array(mediax[21601:29475])
    _alinhado2_y = np.array(-mediay[21601:29475])
    _alinhado2_z = np.array(mediaz[21601:29475])
    _alinhado3_x  = np.array(mediax[39451:48825])
    _alinhado3_y  = np.array(-mediay[39451:48825])
    _alinhado3_z  = np.array(mediaz[39451:48825])
    
    x_alinhado = np.concatenate((_alinhado1_x,_alinhado2_x,_alinhado3_x))
    y_alinhado = np.concatenate((_alinhado1_y,_alinhado2_y,_alinhado3_y))
    z_alinhado = np.concatenate((_alinhado1_z,_alinhado2_z,_alinhado3_z))

    x_desalinhado1 = np.array(mediax[10876:20175])
    y_desalinhado1 = np.array(-mediay[10876:20175])
    z_desalinhado1 = np.array(mediaz[10876:20175])

    x_desalinhado2 = np.array(mediax[29476:39450])
    y_desalinhado2 = np.array(-mediay[29476:39450])
    z_desalinhado2 = np.array(mediaz[29476:39450])
    # _desalinhado2 = np.array(desalinhado2)

    if len(sys.argv) > 2 and sys.argv[2] == "save": 
        salvar_csv(x_alinhado,y_alinhado,z_alinhado,'alinhado')
        salvar_csv(x_desalinhado1,y_desalinhado1,z_desalinhado1,'desalinhado1')
        salvar_csv(x_desalinhado2,y_desalinhado2,z_desalinhado2,'desalinhado2')
        salvar_csv(x_transitorio,y_transitorio,z_transitorio,'transitorio')

    # plt.plot(mediay, linewidth = 2, label = "Original")
    # plt.plot(desalinhado1, linewidth = 0.5, label = "Valores superiores")
    # plt.title("Gráfico para analise")
    # plt.legend()
    # plt.show()
    