from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type
from bs4 import BeautifulSoup
import logging

# Configure logging
logger = logging.getLogger('link_stripper')
logger.setLevel(logging.INFO)  # Change to DEBUG for more detailed logs
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def strip_html_links(html):
    """
    Remove all <a> tags not inside <code> blocks, preserving their inner text.
    Remove <a> tags containing the '¶' symbol entirely.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Unwrap <a> tags not inside <code> and remove <a> tags with '¶' symbol
    for tag in soup.find_all('a'):
        # Check if the <a> tag has '¶' as its content and remove it
        if tag.get_text(strip=True) == '¶':
            logger.debug(f"Removing <a> tag with '¶' symbol: {tag}")
            tag.decompose()  # Remove the entire <a> tag and its contents
        elif not tag.find_parent('code'):
            logger.debug(f"Unwrapping <a> tag with href: {tag.get('href')}")
            tag.unwrap()
        else:
            logger.debug(f"Preserving <a> tag within <code>: {tag.get('href')}")

    return str(soup)


class LinkStripperPlugin(BasePlugin):
    config_scheme = (
        ('target_files', Type(list, default=[])),  # Allows specifying multiple target files
    )

    def on_page_content(self, html, page, config, files):
        """
        Modify the HTML content of each page to strip <a> tags outside <code> blocks.
        This hook is called for each page during both build and serve.
        """
        target_files = self.config.get('target_files', [])

        # If target_files is empty, process all pages
        if not target_files or page.file.dest_path in target_files:
            logger.info(f"Processing page: {page.file.src_path}")

            # Strip <a> tags as per the defined function
            cleaned_html = strip_html_links(html)

            return cleaned_html
        else:
            logger.debug(f"Skipping page: {page.file.src_path}")
            # If not a target file, return the original HTML
            return html
