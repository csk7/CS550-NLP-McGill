# Language Modelling

This repository contains the codes for COMP 550 Course - Natural Language Processing Final project done by Sivakumar Chidambaram and Ian Porada.
A copy of the report is also added to this repository.

## Links to download the data 
The data can be downloaded from the link below:
[Data](https://drive.google.com/open?id=1r81bVka_ZZj7RXP3AmBCY9p8Fiz-zpKa)

The corpus token file and the data folder should be added in the main directory.

## General requirements

CUDA enabled GPU
CuDNN, Pytorch 0.4 

## Commands to Run

For Q-LSTM 4 - bits

```
python main.py --epochs 20 --data data/wikitext-2 --dropouth 0 --wdrop 0 --seed 1882

```



