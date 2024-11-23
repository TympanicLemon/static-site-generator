import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="h1", value="Text", props={"href": "https://www.google.com", "class": "link-to-google"})
        expected_output = 'href="https://www.google.com" class="link-to-google"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_error(self):
        node = HTMLNode(tag="h1", value="Text", props={"href": "https://www.google.com", "class": "link-to-google"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode(tag="h1", value="Text", props={"href": "https://www.google.com", "class": "link-to-google"})
        expected_output = (
            "HTMLNode:\n"
            "tag=h1\n"
            "value=Text\n"
            "children=None\n"
            "props={'href': 'https://www.google.com', 'class': 'link-to-google'}"
        )
        self.assertEqual(str(node), expected_output)


if __name__ == "__main__":
    unittest.main()
