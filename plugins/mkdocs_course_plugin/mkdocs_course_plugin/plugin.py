from mkdocs.plugins import BasePlugin
import re

class AutoCoursePlugin(BasePlugin):

    config_scheme = []

    def on_page_markdown(self, markdown, **kwargs):

        def replacementFunc(m):
            return f"[{m.group(1)}{m.group(2)}](../../courses/{m.group(1)}{m.group(2)})"
        
        markdown = re.sub(r'~([A-Z]{3})(\d{3})', replacementFunc, markdown)

        return markdown