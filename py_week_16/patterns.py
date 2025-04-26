from abc import ABC, abstractmethod

class PalindromeStrategy(ABC):
    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        pass

class SingleWordPalindrome(PalindromeStrategy):
    def is_palindrome(self, text: str) -> bool:
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]