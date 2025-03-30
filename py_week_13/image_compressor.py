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

    def process_directory(self, directory: str) -> None:
        """
        Args:
            directory (str): Путь к директории для обработки.
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)

def main(input_path: str) -> None: # Основная функция программы
    """
    Args:
        input_path (str): Путь к файлу или директории.
    """
    input_path = input_path.strip('"')
    compressor = ImageCompressor(quality=50)
    
    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            print(f"Обрабатываем директорию: {input_path}")
            compressor.process_directory(input_path)
    else:
        print("Указанный путь не существует")

if __name__ == "__main__":
    user_input = input("Введите путь к файлу или директории: ")
    main(user_input)