import os
import anodet
import torch
from torch.utils.data import DataLoader


def train(path):

    dataset = anodet.AnodetDataset(os.path.join(path, "images"))
    dataloader = DataLoader(dataset, batch_size=32)

    padim = anodet.Padim(backbone="resnet18")

    padim.fit(dataloader)

    torch.save(padim.mean, os.path.join(path + "/distributions/", "mean.pt"))
    torch.save(padim.cov_inv, os.path.join(path + "/distributions/", "cov_inv.pt"))
