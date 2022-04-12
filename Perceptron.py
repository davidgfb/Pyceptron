#######################
# Perceptron 1 capa:  #
#                     #
# Diferencia Os de Xs #
# X opacidad          #
# Imagen cuadrada     #
# N Ps neuronas       #
#######################

from numpy import array

############### Inic vars #############
es_X = False
figuras = ('O', 'X')
n_Filas_Pixeles  = 3
n_Cols_Pixeles = n_Filas_Pixeles

######### Fotos  #############
###### [0.0, 1.0] ############

######### Opacos ############
########### O ################
F_O = ((0.0, 1.0, 0.0),
     

       (1.0, 0.0, 1.0),


       (0.0, 1.0, 0.0))   
################################

########### X #################
F_X = ((1.0, 0.0, 1.0),

       
       (0.0, 1.0, 0.0),


       (1.0, 0.0, 1.0))
###############################
###############################
###############################

Nivs_Act_Neuronas = []
nivs_Act_Neuronas_1 = []

def inicia_Neuronas(img):
    global Nivs_Act_Neuronas, nivs_Act_Neuronas_1

    Nivs_Act_Neuronas = img
    nivs_Act_Neuronas_1 = []

inicia_Neuronas(F_O)
    # neurona.niv_Activacion

pesos_Neuronas = n_Filas_Pixeles * [n_Cols_Pixeles * [0]]
    # [-2, 2]

pesos_Neuronas_1 = [] # nivs_Act_Neuronas_1 NO vale

umbral = 0.0

#nivs_Act_Neuronas_1 = n_Filas_Pixeles * n_Cols_Pixeles * [0.0]
##########################################

####### tramite conversion ms fila (prod escalar) ########
for fila_Nivs_Act_Neuronas in Nivs_Act_Neuronas:
    for niv_Act_Neurona in fila_Nivs_Act_Neuronas: # for col
        nivs_Act_Neuronas_1.append(niv_Act_Neurona)

for fila_Pesos_Neuronas in pesos_Neuronas:
    for peso_Neurona in fila_Pesos_Neuronas: 
        pesos_Neuronas_1.append(peso_Neurona)
##################################################

############### vars #############
nivs_Act_Neuronas_2 = array(nivs_Act_Neuronas_1) 
pesos_Neuronas_2    = array(pesos_Neuronas_1)

niv_Act_Neurona = nivs_Act_Neuronas_2 @ pesos_Neuronas_2
    # matriz fila ≡ m columna para prod escalar

esta_Act_Neurona = niv_Act_Neurona > umbral
es_Correcto = es_X == esta_Act_Neurona
##################################

####### parte grafica ######
print('niv_Act_Neurona:', niv_Act_Neurona,
      '\n\nesta_Act_Neurona:', esta_Act_Neurona,
      '\n\nPrediccion:', figuras[int(esta_Act_Neurona)],
      '\n\nes_Correcto:', es_Correcto)
############################

########### Sig Paso ############
####### Se deberia equivocar ####
inicia_Neuronas(F_X) # No tocamos pesos aun. Siguen siendo origs
    
##################################



































'''####### parte grafica ######
print('niv_Act_Neurona:', niv_Act_Neurona,
      'esta_Act_Neurona:', esta_Act_Neurona,
      'nivs_Act_Neuronas:\n\n', nivs_Act_Neuronas_2,
      '\n\npesos_Neuronas_2:\n\n', pesos_Neuronas_2,
      'nivs_Act_Neuronas:\n\n', nivs_Act_Neuronas_1,
      '\n\npesos_Neuronas:\n\n', pesos_Neuronas_1,
      'nivs_Act_Neuronas:\n')

for fila_Nivs_Act_Neuronas in nivs_Act_Neuronas:
    print(fila_Nivs_Act_Neuronas)

print('\npesos_Neuronas:\n')

for fila_Pesos_Neuronas in pesos_Neuronas:
    print(fila_Pesos_Neuronas)
############################'''























































    
