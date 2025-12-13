import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        
        node = HTMLNode(props={"href": "https://www.boots.dev"})
        
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boots.dev"'
        )

    def test_props_to_html_multiple_props(self):

        node =  HTMLNode(
            props={
                "href": "https://www.boots.dev",
                "target": "_blank",
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boots.dev" target="_blank"'
        )
    
    def test_props_to_html_props_empty(self):

        node = HTMLNode(
            props={}
        )

        self.assertEqual(
            node.props_to_html(),
            ""
        )
    
    def test_props_to_html_none(self):

        node = HTMLNode()

        self.assertEqual(
            node.props_to_html(),
            ""
        )



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.boots.dev"})
        
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boots.dev">Click me!</a>'
        )
    
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "This is just some text")

        self.assertEqual(
            node.to_html(),
            "This is just some text"
        )