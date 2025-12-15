import re
from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode

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
    code = len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")
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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final_children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            clean_text = block.replace("\n", " ")
            text_nodes = text_to_textnodes(clean_text)

            children = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                children.append(html_node)
        
            paragraph_node = ParentNode("p", children)
            final_children.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            hash_count, text = extract_heading_info(block)
            
            text_nodes = text_to_textnodes(text)

            children = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                children.append(html_node)
            
            heading_node = ParentNode(f"h{hash_count}", children)
            final_children.append(heading_node)
        
        elif block_type == BlockType.QUOTE:
            clean_text = extract_quote_text(block)

            text_nodes = text_to_textnodes(clean_text)

            children = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                children.append(html_node)
            
            quote_node = ParentNode("blockquote", children)
            final_children.append(quote_node)
        
        elif block_type == BlockType.CODE:
            clean_text = extract_code_text(block)
            text_node = TextNode(clean_text, TextType.TEXT)
            html_node = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [html_node])
            pre_node = ParentNode("pre", [code_node])
            final_children.append(pre_node)
        
        elif block_type == BlockType.UNORDERED:
            item_list = extract_unordered_list(block)

            children = []
            for item in item_list:
                text_nodes = text_to_textnodes(item)
                li_children = []
                for text_node in text_nodes:
                    html_node = text_node_to_html_node(text_node)
                    li_children.append(html_node)
                
                li_node = ParentNode("li", li_children)
                children.append(li_node)
            
            ul_node = ParentNode("ul", children)
            final_children.append(ul_node)
        
        elif block_type == BlockType.ORDERED:
            item_list = extract_ordered_list(block)

            children = []
            for item in item_list:
                text_nodes = text_to_textnodes(item)
                li_children = []
                for text_node in text_nodes:
                    html_node = text_node_to_html_node(text_node)
                    li_children.append(html_node)
                
                li_node = ParentNode("li", li_children)
                children.append(li_node)
            
            ol_node = ParentNode("ol", children)
            final_children.append(ol_node)
            

    return ParentNode("div", final_children)


def extract_heading_info(block):
    stripped = block.lstrip("#")
    hash_count = len(block) - len(stripped)
    
    return hash_count, stripped.strip()

def extract_quote_text(block):
    split_lines = block.split("\n")
    cleaned_lines = [line.lstrip("> ") for line in split_lines]
    
    return " ".join(cleaned_lines)

def extract_code_text(block):
    if block.startswith("```\n") and block.endswith("```"):
        return block[4:-3]

def extract_unordered_list(block):
    lines = block.split("\n")
    cleaned_lines = [line.lstrip("- ") for line in lines]

    return cleaned_lines

def extract_ordered_list(block):
    lines = block.split("\n")
    cleaned_lines = [line.split(". ", 1)[1] for line in lines]

    return cleaned_lines
    