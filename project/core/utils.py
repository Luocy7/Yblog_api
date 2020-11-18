import misaka
from misaka import HtmlRenderer


def generate_rich_content(value):
    rndr = HtmlRenderer(
        flags=[
            misaka.HTML_ESCAPE,
        ]
    )

    md = misaka.Markdown(
        rndr,
        extensions=[
            misaka.EXT_FENCED_CODE,
            misaka.EXT_AUTOLINK,
            misaka.EXT_HIGHLIGHT,
            misaka.EXT_MATH,
            misaka.EXT_TABLES,
            misaka.EXT_UNDERLINE,
            misaka.EXT_QUOTE,
            misaka.EXT_DISABLE_INDENTED_CODE,
        ]
    )

    return md(value)


if __name__ == '__main__':
    markdown_text = "# this is a test text\n--- \n`autolink` \n*followed with some code* \n```\n" \
                    "import re\nre.compile(r'^Hello\\sWorld')\n```"

    print(generate_rich_content(markdown_text))
