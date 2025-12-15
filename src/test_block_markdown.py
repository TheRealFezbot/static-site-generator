import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
            blocks,
        )

    def test_markdown_to_blocks_no_text(self):
        md = ""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [],
            blocks
        )
    
    def test_markdown_to_blocks_no_text(self):
        md = "\n\n\nThis is a **bolded** paragraph\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            [
                "This is a **bolded** paragraph"
            ],
            blocks
        )