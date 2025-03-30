import os
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    supported_formats = ('.jpg', '.jpeg', '.png')
    
    def __init__(self, quality: int):
        self.quality = quality
        register_heif_opener()
    
    @property
    def quality(self) -> int: # Получаем качество сжатия
        return self.__quality
    
    @quality.setter
    def quality(self, quality: int) -> None: # Устанавливаем качество сжатия в диапазоне от 0 до 100
        if not (0 <= quality <= 100):
            raise ValueError("Качество должно быть в диапазоне 0-100")
        self.__quality = quality

    def compress_image(self, input_path: str, output_path: str) -> None: # Функция для сжатия изображения и сохранения его в формате HEIF
        """
        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.__quality)
        print(f"Сжато: {input_path} -> {output_path}")    