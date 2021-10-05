from markdown.test_tools import TestCase


class TestHr(TestCase):
    def test_markdown_formatting(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                # Header
                ## Subheader
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <h1>Header</h1>
                <h2>Subheader</h2>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format="html",
        )

    # def test_valid_image(self):
    #     self.assertMarkdownRenders(
    #             self.dedent(
    #                 """
    #                 [img:bye]
    #                 """
    #             ),
    #             self.dedent(
    #                 """
    #                 <img src="/media/images/uploads/bye.png">
    #                 """
    #             ),
    #             output_format='html'
    #         )
