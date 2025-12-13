import unittest

from htmlnode import HTMLNode

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

        