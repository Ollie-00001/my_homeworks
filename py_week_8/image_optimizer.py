import os
from typing import List
from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow
from pillow_avif import register_avif_opener, from_pillow as avif_from_pillow
from tqdm import tqdm

# Регистрируем форматы
register_heif_opener()
register_avif_opener()

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'JPG', 'JPEG'}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = 'AVIF'
AVAILABLE_FORMATS = {'WEBP', 'HEIF', 'AVIF'}
