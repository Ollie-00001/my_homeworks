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

def compress_image(image_path: str, output_format: str = DEFAULT_FORMAT, quality: int = DEFAULT_QUALITY) -> str:
    """
    Compresses an image and saves it to the specified format.
    """
    if output_format not in AVAILABLE_FORMATS:
        raise ValueError(f"Формат '{output_format}' не поддерживается. Доступные форматы: {AVAILABLE_FORMATS}.")

    image = Image.open(image_path)
    output_path = f"{os.path.splitext(image_path)[0]}_compressed.{output_format.lower()}"

    if output_format == 'WEBP':
        image.save(output_path, format='WEBP', quality=quality)
    elif output_format == 'HEIF':
        heif_file = heif_from_pillow(image)
        heif_file.save(output_path, quality=quality)
    elif output_format == 'AVIF':
        avif_file = avif_from_pillow(image)
        avif_file.save(output_path, quality=quality)

    original_size = os.path.getsize(image_path)
    compressed_size = os.path.getsize(output_path)
    compression_ratio = 100 - (compressed_size / original_size * 100)
    print(f"{os.path.basename(image_path)}: Сжатие на {compression_ratio:.2f}%")

    return output_path
