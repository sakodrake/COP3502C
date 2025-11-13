from functions import * 
import unittest

class TestPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(37))
        self.assertFalse(is_prime(-1))
    
    def test_non_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(13 * 17))

    def test_too_small(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-11))

class TestRemoveVowels(unittest.TestCase):
     def test_all_vowels(self):
        # All vowels removed leaves empty string
        self.assertEqual(remove_vowels("aeiouAEIOU"), "")

     def test_some_vowels(self):
        self.assertEqual(remove_vowels("Hello World"), "Hll Wrld")
        self.assertEqual(remove_vowels("Python"), "Pythn")

     def test_no_vowels(self):
        self.assertEqual(remove_vowels("rhythm"), "rhythm")
        self.assertEqual(remove_vowels("brrr"), "brrr")

if __name__ == "__main__":
    unittest.main()






