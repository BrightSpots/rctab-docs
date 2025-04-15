from bs4 import BeautifulSoup
from link_stripper import strip_html_links


def normalize_html(html):
    """Normalize the HTML for comparison by parsing and reformatting it."""
    soup = BeautifulSoup(html, 'html.parser')

    # Convert the BeautifulSoup object back to a string with minimal formatting
    return soup.prettify(formatter="minimal").strip()


# Existing Tests
def test_single_link():
    html = '<p>This is a <a href="http://example.com">link</a> in a paragraph.</p>'
    expected = '<p>This is a link in a paragraph.</p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_multiple_links():
    html = '<p><a href="http://example1.com">Link1</a> and <a href="http://example2.com">Link2</a> in the same line.</p>'
    expected = '<p>Link1 and Link2 in the same line.</p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_links_with_attributes():
    html = '<p>Visit <a href="http://example.com" class="external" target="_blank">our site</a> now.</p>'
    expected = '<p>Visit our site now.</p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_nested_links():
    html = '<div><p>This is a <a href="http://example.com">nested <strong>link</strong></a>.</p></div>'
    expected = '<div><p>This is a nested <strong>link</strong>.</p></div>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_code_block_retention():
    html = '<p>Here is a code block: <code>&lt;a href="http://example.com"&gt;code&lt;/a&gt;</code></p>'
    expected = '<p>Here is a code block: <code>&lt;a href="http://example.com"&gt;code&lt;/a&gt;</code></p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


# Additional Tests
def test_a_tags_within_code():
    html = '<p>Example: <code><a href="http://example.com">hello world</a></code></p>'
    expected = '<p>Example: <code><a href="http://example.com">hello world</a></code></p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_multiple_links_in_same_element():
    html = '<p>This <a href="http://example1.com">link1</a> and <a href="http://example2.com">link2</a> should remain.</p>'
    expected = '<p>This link1 and link2 should remain.</p>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_multiple_links_within_code():
    html = '<code>This is a <a href="http://example1.com">link</a> inside code and <a href="http://example2.com">another link</a> here.</code>'
    expected = '<code>This is a <a href="http://example1.com">link</a> inside code and <a href="http://example2.com">another link</a> here.</code>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_deeply_nested_a_in_code():
    html = '''
    <p>
        Example code:
        <code>
            <div>
                <span>
                    <a href="http://example.com">Nested link</a>
                </span>
            </div>
        </code>
    </p>
    '''
    expected = '''
    <p>
        Example code:
        <code>
            <div>
                <span>
                    <a href="http://example.com">Nested link</a>
                </span>
            </div>
        </code>
    </p>
    '''
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_deeply_nested_a_outside_code():
    html = '''
    <div>
        <section>
            <p>
                <a href="http://example.com">Deeply nested link</a>
            </p>
        </section>
    </div>
    '''
    expected = '''
    <div>
        <section>
            <p>
                Deeply nested link
            </p>
        </section>
    </div>
    '''
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_remove_links_with_paragraph_symbol():
    html = '<h1 id="documentation-abstracts">Documentation Abstracts<a class="headerlink" href="#documentation-abstracts" title="Permanent link">¶</a></h1>'
    expected = '<h1 id="documentation-abstracts">Documentation Abstracts</h1>'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_preserve_links_with_special_symbols():
    html = '<a href="#documentation-abstracts">Why I like special symbols like ¶</a>'
    expected = 'Why I like special symbols like ¶'
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)


def test_complex_html_with_real_code_blocks():
    html = '''
    <html>
        <body>
            <p>Some text before <a href="http://example1.com">Link1</a> and <a href="http://example2.com">Link2</a>.</p>
            <div><a href="http://example3.com">Another link</a> in a div.</div>
            <p><a href="http://example4.com">Nested <a href="http://example5.com">Inner link</a></a></p>
            <p>Real code block: <code><a href="http://example.com">code link</a> and <a href="http://example.com">another code link</a></code></p>
        </body>
    </html>
    '''
    expected = '''
    <html>
        <body>
            <p>Some text before Link1 and Link2.</p>
            <div>Another link in a div.</div>
            <p>Nested Inner link</p>
            <p>Real code block: <code><a href="http://example.com">code link</a> and <a href="http://example.com">another code link</a></code></p>
        </body>
    </html>
    '''
    assert normalize_html(strip_html_links(html)) == normalize_html(expected)
