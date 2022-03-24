import os
import torch
import numpy as np
import anodet
import cv2


def get_predict_model(path):
    model_data_path = path + "/distributions"
    mean = torch.load(os.path.join(model_data_path, 'mean.pt'))
    cov_inv = torch.load(os.path.join(model_data_path, 'cov_inv.pt'))
    model = anodet.Padim(backbone='resnet18', mean=mean, cov_inv=cov_inv, device=torch.device('cuda'))
    return model


def predict_image(image, path, thresh):
    """Turn image into batch, make prediction and return heatmap, score and threshold"""
    model = get_predict_model(path)
    batch = anodet.to_batch([image], anodet.standard_image_transform, torch.device('cuda'))
    image_scores, score_maps = model.predict(batch)
    test_images = np.array([image]).copy()
    heatmap_images = anodet.visualization.heatmap_images(test_images, score_maps, alpha=0.5)
    heatmap = cv2.cvtColor(heatmap_images[0], cv2.COLOR_BGR2RGB)
    return heatmap, round(image_scores[0].item(), 2)
