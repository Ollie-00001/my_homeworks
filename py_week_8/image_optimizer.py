import os
from typing import List
from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
from pillow_avif import register_avif_opener, from_pillow as avif_from_pillow
from tqdm import tqdm

# Registered image openers
register_heif_opener()
register_avif_opener()

# Added constants
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'JPG', 'JPEG'}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = 'AVIF'
AVAILABLE_FORMATS = {'WEBP', 'HEIF', 'AVIF'}

def get_images_paths(source_path: str) -> List[str]:
    """
    Returnns a list of image paths in the specified directory.
    """
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Путь '{source_path}' не существует.")

    image_paths = []
    for root, _, files in os.walk(source_path):
        for file in files:
            if file.split('.')[-1] in ALLOWED_EXTENSIONS:
                image_paths.append(os.path.join(root, file))

    if not image_paths:
        raise ValueError("Не найдено подходящих изображений в указанной директории.")

    return image_paths