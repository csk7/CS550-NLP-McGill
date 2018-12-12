# Language Translation (English - German)

This repository contains the codes for COMP 550 Course - Natural Language Processing Final project done by Sivakumar Chidambaram and Ian Porada.
A copy of the report is also added to this repository.

## Links to download the data 
The data can be downloaded from the link below:
[Data](https://drive.google.com/open?id=1r81bVka_ZZj7RXP3AmBCY9p8Fiz-zpKa)

The data2 folder should be added in the main directory.

## General requirements

CUDA enabled GPU,
CuDNN, Pytorch 0.4, 
six,
tqdm,
configargparse,

## Commands to Run

To train the Q-LSTM model with 8 bits parameters for Encoder, Decoder, Attention and Generator:
```
python train.py -data data2/multi30k.atok.low -save_model multi30k_model -gpu_ranks 0 -train_steps 5000 -save_checkpoint_steps 5000 -dropout 0
```

Translate the test set:
```
python translate.py -gpu 0 -model multi30k_model_step_5000.pt -src data2/multi30k/test2016.en.atok -tgt data2/multi30k/test2016.de.atok -replace_unk -verbose -output multi30k.test.pred.atok -batch_size 128
```
BLEU Score

```
perl tools/multi-bleu.perl data2/multi30k/test2016.de.atok < multi30k.test.pred.atok
```

