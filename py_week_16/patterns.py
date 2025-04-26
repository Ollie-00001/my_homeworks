from abc import ABC, abstractmethod

class PalindromeStrategy(ABC):
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        pass

class SingleWordPalindrome(PalindromeStrategy):
    def is_palindrome(self, text: str) -> bool:
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]
    
class PalindromeContext:
    def __init__(self, strategy: PalindromeStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: PalindromeStrategy) -> None:
        self.strategy = strategy
    
    def check(self, text: str) -> bool:
        return self.strategy.is_palindrome(text)

class PalindromeFacade:
    def __init__(self) -> None:
        """
        Стратегия на проверку одиночных слов, которая будет применяться по умолчанию.
        """
        self.context = PalindromeContext(SingleWordPalindrome())

    def check_palindrome(self, text: str) -> bool:
        word_count = len(text.strip().split())
    
    if word_count == 1:
        self.context.set_strategy(SingleWordPalindrome())
    else:
        self.context.set_strategy(MultiWordPalindrome())

        return self.context.check(text)

if __name__ == "__main__":
    facade = PalindromeFacade()

    # Тесты
    ## Тест 1.  Проверка палиндрома с одним словом
    word = "Racecar"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}") # Должно вывести True

    ## Тест 2.  Одно слово, но не палиндром
    word = "Hello"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}") # Должно вывести False

    ## Тест 3. Предложение - палиндром
    sentence = "A man, a plan, a canal, Panama!"
    print(f"'{sentence}' — палиндром? {facade.check_palindrome(sentence)}") # Должно вывести True

    ## Тест 4. Предложение - не палиндром
    sentence = "Hello, world!"
    print(f"'{sentence}' — палиндром? {facade.check_palindrome(sentence)}") # Должно вывести False

    ## Тест 5. Одно слово - палиндром с разными регистрами
    word = "DeiFieD"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # Должно вывести True

    ## Тест 6. Сложная фраза - палиндром
    sentence = "Was it a car or a cat I saw?"
    print(f"'{sentence}' — палиндром? {facade.check_palindrome(sentence)}") # Должно вывести True