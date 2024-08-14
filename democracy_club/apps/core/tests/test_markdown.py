from markdown.test_tools import TestCase


class TestHr(TestCase):
    def test_markdown_formatting(self):
        (self.assertMarkdownRenders("# Header", "<h1>Header</h1>"),)

    def test_image(self):
        self.assertMarkdownRenders(
            """![Image](http://humane man.jpg "The most humane man.")""",
            """<p><img alt="Image" src="http://humane man.jpg" title="The most humane man." /></p>""",
        )

    def test_blank_image(self):
        self.assertMarkdownRenders(
            """![Blank]()""", """<p><img alt="Blank" src="" /></p>"""
        )

    def test_combined_link_text(self):
        self.assertMarkdownRenders(
            """[Text[[[[[[[]]]]]]][]](http://link.com) more text""",
            """<p><a href="http://link.com">Text[[[[[[[]]]]]]][]</a> more text</p>""",
        )

    def test_single_quote(self):
        self.assertMarkdownRenders(
            """[test](link"notitle)""",
            """<p><a href="link&quot;notitle">test</a></p>""",
        )

    def test_multiline_codeblock(self):
        self.assertMarkdownRenders(
            "    # Line 1\n    # Line 2\n",
            self.dedent(
                """
                <pre><code># Line 1
                # Line 2
                </code></pre>
                """
            ),
        )
