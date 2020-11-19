import misaka
from misaka import HtmlRenderer


def generate_rich_content(value):

    """
    use misaka to render markdown content
    https://misaka.readthedocs.io/en/latest/
    """
    """
        - skip_html:    Do not allow any user-inputted HTML in the output.
        - escape:       Escape all HTML tags, regardless of what they are.
        - hard_wrap:    Insert HTML <br> tags inside on paragraphs where the origin Markdown document had newlines 
                        (by default, Markdown ignores these newlines).
        - use_xhtml:    Output XHTML-conformant tags.
    """
    rndr = HtmlRenderer(
        flags=[]
    )

    """
    - tables:           Parse PHP-Markdown tables.
    - fenced_code:      Blocks delimited with 3 or more ~ or backticks will be considered as code, without the need to 
                        be indented. An optional language name may be added at the end of the opening fence for 
                        the code block.
    - footnotes:        Parse Markdown footnotes.
    - autolink:         Parse links even when they are not enclosed in <> characters. Autolinks for the http, 
                        https and ftp protocols will be automatically detected. Email addresses are also handled, 
                        and http links without protocol, but starting with www.
    - strikethrough:    Two ~ characters mark the start of a strikethrough, e.g. this is ~~good~~ bad.
    - underline:        Treat text surrounded by underscores (like _this_) as underlined, rather than emphasized.
    - highlight:        Treat text surrounded by double equal signs (like ==this==) as highlighted.
    - quote:            Parse inline quotes (like "this"). This allows the renderer to control how they are rendered.
    - superscript:      Parse superscripts after the ^ character; contiguous superscripts are nested together, 
                        and complex values can be enclosed in parenthesis, e.g. this is the 2^(nd) time.
    - math:             Parse inline LaTeX-style math blocks (like $$this$$).
    - math_explicit:    Parse inline LaTeX-style math blocks with a single dollar, e.g. $x + y = 3$
    - no_intra_emphasis:        Do not parse emphasis inside of words. Strings such as foo_bar_baz will not 
                                generate <em> tags.
    - space_headers:    A space is always required between the hash at the beginning of a header and its name, 
                        e.g. #this is my header would not be a valid header.
    - disable_indented_code:    Ignore indented code blocks

    """

    md = misaka.Markdown(
        rndr,
        extensions=[
            "tables",
            "fenced-code",
            "footnotes",
            "autolink",
            "strikethrough",
            "underline",
            "quote",
            "superscript",
            "math",
            # "no-intra-emphasis",
            "space-headers",
            "math-explicit",
            "disable-indented-code",
        ]
    )

    return md(value)


if __name__ == '__main__':
    markdown_text = "# this is a test text\n--- \n`autolink` \n*followed with some code* \n```\n" \
                    "import re\nre.compile(r'^Hello\\sWorld')\n```"

    print(generate_rich_content(markdown_text))
