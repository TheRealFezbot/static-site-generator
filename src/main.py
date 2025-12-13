from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    htmltest = HTMLNode("p", "This is a HTMLNode",)
    leaftest = LeafNode("a", "This is a link", {"href": "https://www.boots.dev"})
    parenttest = ParentNode("div", [htmltest, leaftest])
    
    print(htmltest)
    print(leaftest)
    print(parenttest)


if __name__ == "__main__":
    main()