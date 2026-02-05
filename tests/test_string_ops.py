import unittest
from package_creation_tutorial.string_ops import reverse_string, count_vowels, capitalize_words

class TestStringOps(unittest.TestCase):

    def test_reverse_string(self):  # Ajoute 'self' ici
        """Test the reverse_string function."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")

    def test_count_vowels(self):  # Ajoute 'self' ici
        """Test the count_vowels function."""
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_capitalize_words(self):  # Ajoute 'self' ici
        """Test the capitalize_words function."""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")

if __name__ == '__main__':
    unittest.main()