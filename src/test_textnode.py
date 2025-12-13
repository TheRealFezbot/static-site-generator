import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a bold node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a link", TextType.LINK, "https://boot.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boots.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.boots.dev"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://picsum.photos/200")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://picsum.photos/200", "alt": "This is an image node"})
    
    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is an invalid node", TextType.UNDERLINE))

if __name__ == "__main__":
    unittest.main()