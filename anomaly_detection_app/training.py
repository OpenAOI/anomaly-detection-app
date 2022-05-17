import os
import anodet
import torch
from torch.utils.data import DataLoader
from anomaly_detection_app.config import device_type


def train(path: str) -> None:

    dataset = anodet.AnodetDataset(os.path.join(path, "images"))
    dataloader = DataLoader(dataset, batch_size=32)

    padim = anodet.Padim(backbone="resnet18", device = torch.device(device_type))

    padim.fit(dataloader)

    torch.save(padim.mean, os.path.join(path + "/distributions/", "mean.pt"))
    torch.save(padim.cov_inv, os.path.join(path + "/distributions/", "cov_inv.pt"))
