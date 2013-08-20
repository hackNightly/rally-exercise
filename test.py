import unittest
import templar

class TestTemplar(unittest.TestCase):

  def setUp(self):
    self.vars     = {'name': 'Darrell', 'occupation': 'hacker', 'age': 26}
    self.template = 'My name is ${name} and I am ${${age}} years old. I consider myself a ${occupation}.'
    self.words    = templar._get_words(self.template)

  def test_get_words(self):
    # should be iterable
    self.assertTrue(hasattr(self.words, '__iter__'))

  def test_get_token_key(self):
    token = '${RALLYDEV}'
    key   = templar._get_token_key(token)
    self.assertTrue(key == 'RALLYDEV')

  def test_missing_var(self):
    vars     = {'one': 1}
    template = 'Count to two. ${one}, ${two}'
    # raises error since variable 'two' is missing
    self.assertRaises(KeyError, templar.parse, vars, template)

  def test_parse(self):
    sentence = templar.parse(self.vars, self.template)
    self.assertEqual('My name is Darrell and I am ${26} years old. I consider myself a hacker.', sentence)

if __name__ == '__main__':
    unittest.main()
