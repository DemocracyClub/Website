from django import test

from .. import renderers


class MarkdownRendererTestCase(test.TestCase):
    def test_render_to_html(self):
        """The Markdown Renderer should be able to translate Markdown to HTML"""
        expected = "<p><em>Markdown FTW!!</em></p>"
        self.assertEqual(expected, renderers.markdown("*Markdown FTW!!*"))
