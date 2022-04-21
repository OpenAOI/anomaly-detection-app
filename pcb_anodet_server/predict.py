import os
import torch
import numpy as np
import anodet
import cv2
from pcb_anodet_server.config import device_type, project_path
from typing import Any, Tuple


def get_model(model_path: str) -> Any:
    mean = torch.load(os.path.join(model_path, "mean.pt"))
    cov_inv = torch.load(os.path.join(model_path, "cov_inv.pt"))
    model = anodet.Padim(
        backbone="resnet18",
        mean=mean,
        cov_inv=cov_inv,
        device=torch.device(device_type),
    )
    return model


def image_classification(image_scores, thresh):
    """Use the scores to classify image as good/bad"""
    image_classification = anodet.classification(image_scores, thresh)
    return int(image_classification[0])


def predict_image(image: Any, thresh: int, model_path: str) -> Tuple[Any, float]:
    """Turn image into batch, make prediction and return heatmap, score and threshold"""
    model = get_model(model_path)
    batch = anodet.to_batch(
        [image], anodet.standard_image_transform, torch.device(device_type)
    )
    image_scores, score_maps = model.predict(batch)
    image_class = image_classification(image_scores, thresh)
    test_images = np.array([image]).copy()
    heatmap_images = anodet.visualization.heatmap_images(
        test_images, score_maps, alpha=0.5
    )
    heatmap = cv2.cvtColor(heatmap_images[0], cv2.COLOR_BGR2RGB)
    return heatmap, round(image_scores[0].item(), 2), image_class
