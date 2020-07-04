SantanderCustomerQA
==============================

## Introducción
Novedades: la gente de Santander Tecnología nos compartío un baseline para que puedan seguir explorando o tengan un punto de partida para esta competencia.

En Santander tenemos por misión contribuir al progreso de las personas y las empresas. Debido a ello buscamos constantemente nuevas formas de entender al cliente, con el objetivo de consolidar vínculos a largo plazo.

Nuestro equipo de Advanced Analytics & Machine Learning se encuentra en continua mejora de sus algoritmos y modelos. Basándonos en esta premisa, decidimos abrir nuestros datos e invitar a la comunidad a identificar nuevas formas de entender las preguntas y reclamos de nuestros clientes, utilizando un motor de NLU (Natural Language Understanding).

Esta competencia tiene como objetivo desarrollar un algoritmo de clasificación que, utilizando técnicas de NLP (Natural Language Processing), sea capaz de entender la intención de un cliente (target) al momento de realizar una pregunta (predictor) en alguno de los canales del Banco.

## Descripción
Se disponen de tres datasets:

- training.csv: reúne la información del caso, el mismo tiene dos columnas
    - Pregunta: pregunta realizada por el cliente. (String)
    - Intención: intención de la pregunta realizada, contiene 350 intenciones aproximadamente. (String)

- test.csv: solo contiene la pregunta realizada por el cliente.

- primer_submit.csv: este archivo tiene el formato en el que se deben enviar las predicciones.

### Data
Uncompress data.zip.

### Notebooks: 

#### Baseline.ipynb
Baseline provisto para la competencia.

#### 00-logisticRegression.ipynb  
Simpler LogisticRegression model without cleaned data. 

Tags: Tfidf, Logistic, GridSearch. 

#### 01-create_dictionary_spellchecker.ipynb
we had downloaded Data from [RAE](http://corpus.rae.es/lfrecuencias.html) and we built a "frequence spellchecker". Dictionary saved at interim/dictionary. 
It has an execution stage, though it is obsolete because it is very expensive to execute on local machine.

Tags: pyspellchecker, [Norvig Spellchecker](https://norvig.com/spell-correct.html), [TutorialsPoint: Python text processing](https://www.tutorialspoint.com/python_text_processing/python_spelling_check.htm)

#### 01-execute_spellchecker_colab.ipynb
Before script were executed in colab, then it were saved at processed folder train and test datasets curated. 

#### 03_pytorch_text_classification.ipynb
Pytorch and Torchtext approach with cleaned data. 

Tags: pytorch, rnn, lstm, torchtext, spellchecker
Insights: 
1) usar fixed lenght sentences
2) LabelField te mapea en modo "categoria" tus labels, para encontrarlo hay que usar "itos" y no "stoi". Es decir Label.itois[ "lo que devolvió la red" ] => "categoría en mi dataset"
3) LSTM y toda esa bola de RNN no se obtuvo buen resultado
4) Activaciones tanh, relu tampoco
5) usé un número grande de dropout para regularizar (0.8)

#### 00-varios_modelos.ipynb
Obsolete. Multiple Model evaluation:
Tags: RandomForest, MLP, Lightgbm, Xgb, SVC, PCA (truncatedSVD), NMF, RobustScaler..

### Resources
[Torchtext](https://pytorch.org/text/index.html)

[TutorialsPoint: Python text processing](https://www.tutorialspoint.com/python_text_processing/python_spelling_check.htm)

[Pytorch Text examples](https://github.com/JonathanLoscalzo/pytorch-sentiment-analysis)
[Pytorch Architecture examples](https://github.com/JonathanLoscalzo/Text-Classification-Models-Pytorch)