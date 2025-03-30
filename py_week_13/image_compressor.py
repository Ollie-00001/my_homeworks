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
        