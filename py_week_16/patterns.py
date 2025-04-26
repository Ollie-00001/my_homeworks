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
        self.context = PalindromeContext(SingleWordPalindrome())

    def check_palindrome(self, text: str) -> bool:
        word_count = len(text.strip().split())
    
    if word_count == 1:
        self.context.set_strategy(SingleWordPalindrome())
    else:
        self.context.set_strategy(MultiWordPalindrome())

    return self.context.check(text)