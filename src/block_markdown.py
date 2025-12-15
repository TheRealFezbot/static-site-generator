import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered"
    ORDERED = "ordered"

def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if block:
            new_blocks.append(block)
    
    return new_blocks

def block_to_block_type(block):
    lines = block.splitlines()
    
    heading = re.match(r"^#{1,6} .+", block)
    code = block.startswith("```") and block.endswith("```")
    quote = all(map(lambda x: x.startswith(">"), lines))
    unordered = all(map(lambda x: x.startswith("- "), lines))
    ordered = all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1))
        
    if heading:
        return BlockType.HEADING
    if code:
        return BlockType.CODE
    if quote:
        return BlockType.QUOTE
    if unordered:
        return BlockType.UNORDERED
    if ordered:
        return BlockType.ORDERED
    
    return BlockType.PARAGRAPH
    