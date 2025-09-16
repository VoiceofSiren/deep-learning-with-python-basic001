import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
import numpy as np
import torchviz

class RegressionDataset(Dataset):
    def __init__(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
        self.n_samples = x_data.shape[0]

    def __len__(self):
        return self.n_samples

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

x_numpy = np.array(
    object = [-1.5, -0.8, 0.1, 0.9, 1.7],
    dtype = np.float32
)

y_numpy = np.array(
    object = [0.3, -0.3, 0.5, 1.8, 1.5],
    dtype = np.float32
)