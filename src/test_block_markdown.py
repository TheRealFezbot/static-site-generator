import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            html,
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
            html,
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
            html,
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
            html,
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            html,
        )