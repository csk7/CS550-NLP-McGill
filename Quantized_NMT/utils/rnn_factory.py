"""
 RNN tools
"""
import torch.nn as nn
import onmt.models
from onmt.utils.my_lstm_file import LSTM,LSTMCell

def rnn_factory(rnn_type, **kwargs):
    """ rnn factory, Use pytorch version when available. """
    no_pack_padded_seq = False
    if rnn_type == "SRU":
        # SRU doesn't support PackedSequence.
        no_pack_padded_seq = True
        rnn = onmt.models.sru.SRU(**kwargs)
    elif rnn_type == "LSTM":
    	rnn = LSTM(**kwargs)
    elif rnn_type == "LSTMCell":
    	print(**kwargs)
    	rnn = LSTMCell(**kwargs)
    else:
        rnn = getattr(nn, rnn_type)(**kwargs)
    return rnn, no_pack_padded_seq
