import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):

    def test_extract_title(self):
        md = "# Hello!"
        title = extract_title(md)
        self.assertEqual(
            "Hello!",
            title,
        )
    
    def test_extract_title_h2(self):
        md = "## Intro!\n# Title"
        title = extract_title(md)
        self.assertEqual(
            "Title",
            title,
        )
    
    def test_extract_title_exception(self):
        with self.assertRaises(Exception):
            extract_title("This is just some text\n## with a h2 heading")