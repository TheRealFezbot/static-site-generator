import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

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
    
    def test_block_to_block_type_heading(self):
        block = block_to_block_type("#### Heading")
        self.assertEqual(
            BlockType.HEADING,
            block
        )
    
    def test_block_to_block_type_code(self):
        block = block_to_block_type(
            """```
code block
```"""
        )
        self.assertEqual(
            BlockType.CODE,
            block
        )
    
    def test_block_to_block_type_quote(self):
        block = block_to_block_type(
            """>This is a Quote
>This is another quote
>This also
"""
        )
        self.assertEqual(
            BlockType.QUOTE,
            block
        )
    
    def test_block_to_block_type_unordered(self):
        block = block_to_block_type(
            """- This is an unordered list
- This is another
- This also
"""
        )
        self.assertEqual(
            BlockType.UNORDERED,
            block
        )
    
    def test_block_to_block_type_ordered(self):
        block = block_to_block_type(
            """1. This is an ordered list
2. This is another
3. This also
"""
        )
        self.assertEqual(
            BlockType.ORDERED,
            block
        )
    
    def test_block_to_block_type_paragraph(self):
        block = block_to_block_type("This is just some text")

        self.assertEqual(
            BlockType.PARAGRAPH,
            block
        )
    
    def test_block_to_block_type_wrong_heading(self):
        block = block_to_block_type("####Heading")
        self.assertEqual(
            BlockType.PARAGRAPH,
            block
        )
    
    def test_block_to_block_type_ordered_wrong(self):
        block = block_to_block_type(
            """1. This is an ordered list
1. This is another
2. This also
"""
        )
        self.assertEqual(
            BlockType.PARAGRAPH,
            block
        )