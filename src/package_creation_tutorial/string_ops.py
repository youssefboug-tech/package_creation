# Every function have docstrings and use strong typing

def reverse_string(s: str) -> str:
    """
    Reverse the given string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """Compte le nombre de voyelles dans la chaîne."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def capitalize_words(s: str) -> str:
    """Met en majuscule la première lettre de chaque mot."""
    return ' '.join(word.capitalize() for word in s.split())