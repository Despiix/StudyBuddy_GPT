import torch
import torch.nn as nn
from torch.nn import functional as F

# setting hyperparameters
batch_size = 16  # how many independent sequences will we process in parallel?
block_size = 32  # what is the maximum context length for predictions?
max_iters = 5000
eval_interval = 100
learning_rate = 1e-3
device = 'cuda' if torch.cuda.is_available() else 'cpu'  # sets the device (CPU or GPU) it will be trained on
eval_iters = 200
n_embd = 64
n_head = 4
n_layer = 4
dropout = 0.0

