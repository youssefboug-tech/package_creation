from package_creation_tutorial.string_ops import reverse_string, count_vowels, capitalize_words

def main():
    """Fonction principale pour démontrer les opérations sur les chaînes."""
    test_string: str = "hello world"
    
    print(f"Original string: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Vowel count: {count_vowels(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")

if __name__ == "__main__":
    main()