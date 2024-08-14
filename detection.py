import pathlib
import torch
from pathlib import Path
from collections import defaultdict
from PIL import Image
import numpy as np
import cv2

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model = torch.hub.load('yolov5', 'custom', path=r"training_result\exp\weights\best.pt", source='local', force_reload=True)

def points(img):
    def extract_class_counts(results):
        class_counts = defaultdict(int)
        for *xyxy, conf, cls in results.xyxy[0]:
            class_id = int(cls)
            if class_id not in excluded_classes:
                class_name = model.names[class_id]
                class_counts[class_name] += 1
        return dict(class_counts)

    excluded_classes = [1, 2]  

    results = model(img, size=640)
    results.print()

    class_counts = extract_class_counts(results)

    points = {
        'Car': 2.5,
        'Two Wheeler': 1,
        'Auto': 1.5,
        'Bus': 4,
        'Truck': 4
    }

    total_points = sum(class_counts.get(cls, 0) * points.get(cls, 0) for cls in class_counts)

    return total_points
