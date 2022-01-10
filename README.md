# ML_correia
## Autores
- Maurício Souza Sathler
- Matheus Neves Marques
- Andre Maciel Cid
- Gustavo Pessin

Este pacote foi desenvolvido em python3.6 com as seguintes bibliotecas:
- Numpy
- Matplotlib
- Sklearn
- Pickle

Arquivos necessários para o tratamento e treinamento dos dados de acelerometro para modelos de Machine Learning


### Separação dos Rotulos
Primeiramente é necessário separar os dados e seus respectivos rotulos, o codigo abaixo pode auxiliar na separação:

    python3 separacao_rotulos.py desalinhamento_xy_sem_filtro.csv save
    python3 separacao_superior.py desalinhado1_separados.csv 25 save
    python3 separacao_superior.py desalinhado2_separados.csv 25 save
    python3 separacao_superior.py transitorio_separados.csv 10 save


Os dados de entrada devem estar no formato da imagem abaixo:

![image](https://user-images.githubusercontent.com/51409770/148809583-4eace624-3472-47d9-927f-b8d81f6562fa.png)

O código gera diferentes arquivos para os labels, tendo o formado de saída:

![image2](https://user-images.githubusercontent.com/51409770/148809901-a429f0ad-fba4-4894-ab8a-c0e001c153b2.png)


### Retirada de dados que atrapalham o treinamento
Depois disso, para metodos de classificação baseados em Random Forest e Gradient Boosting é muito importante o tratamento da entrada, assim, para melhorar o resultado da classificação deve-se descartar os dados coletados da parte inferior da correia.

    python3 separacao_superior.py alinhado_separados.csv 10 save

O primeiro arquivo deve ser o com os dados de um rotulo com colunas x,y,z (Conforme a segunda imagem)


### Tratamento dos dados e Análise dos Labels
Após a separação da parte superior, vamos tirar a media e o desvio padrao de cada dado de aceleração, 

    python3 analise_labels.py alinhado_separados_superior.csv desalinhado1_separados_superior.csv desalinhado2_separados_superior.csv transitorio_separados_superior.csv
    
Esse codigo plotara os labels:

    
### Treinamento
Depois disso temos o arquivo de treinamento, nele é utilizados dois modelos o Random Forest e o Gradient Boosting

    python3 classificacao.py 
    
Este codigo retorna arquivos com modelos treinados, nomeados de:
  
    RF_trained_model.sav
    GB_trained_model.sav
    
### Utilizando o modelo treinado
Que podem ser carregados conforme o exemplo:

    python3 load_model.py

