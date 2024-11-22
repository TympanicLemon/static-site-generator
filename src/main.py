from textnode import TextNode, TextType


def main():
    node = TextNode("Hi there!", TextType.BOLD, "www.google.com")
    print(node)


main()
