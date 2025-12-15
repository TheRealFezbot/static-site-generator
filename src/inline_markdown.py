import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue
        
        split_node = old_node.text.split(delimiter)

        if len(split_node) % 2 == 0:
            raise Exception("Invalid markdown syntax: no closing delimiter found")
        
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                new_list.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_list.append(TextNode(split_node[i], text_type))

    return new_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)

        if not images:
            new_list.append(old_node)
            continue
        
        current_text = old_node.text
        for (alt, url) in images:
            image_md = f"![{alt}]({url})"
            before, after = current_text.split(image_md, 1)
            if before:
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(alt, TextType.IMAGE, url))
            
            current_text = after

        if current_text:
            new_list.append(TextNode(current_text, TextType.TEXT))
    
    
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)

        if not links:
            new_list.append(old_node)
            continue
        
        current_text = old_node.text
        for (title, url) in links:
            link_md = f"[{title}]({url})"
            before, after = current_text.split(link_md, 1)
            if before:
                new_list.append(TextNode(before, TextType.TEXT))
            new_list.append(TextNode(title, TextType.LINK, url))
            
            current_text = after

        if current_text:
            new_list.append(TextNode(current_text, TextType.TEXT))
    
    
    return new_list


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes