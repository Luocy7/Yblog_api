import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import deque


class MdFile(object):

    def __init__(self, md_str: str = None, md_file: str = None, md_dict: dict = None):
        """

        :param md_str: Markdown String Content
        :param md_file: Markdown File
        :param md_dict: format: {
                                "md_name": file_name,
                                "md_title": md_title,
                                "md_created": md_created,
                                "md_modified": md_modified,
                                "md_tags": md_tags,
                                "md_content": md_content
                                }
        """

        self.md_file = md_file
        self.md_str = md_str
        self.md_dict = md_dict

        self.md_name = ''
        self.md_title = ''
        self.md_tags = []
        self.md_created = None
        self.md_modified = None
        self.md_content = ''

        if self.md_str:
            self.parse_md_from_str()
        elif self.md_file:
            self.parse_md_from_file()
        elif self.md_dict:
            self.parse_md_from_dict()
        else:
            raise KeyError

    def parse_md_from_file(self):
        md_file = Path(self.md_file)
        self.md_name = md_file.stem
        self.md_str = md_file.read_text(encoding='utf-8')
        self.parse_md_from_str()

    def parse_md_from_str(self):
        content_lines = self.md_str.split('\n')

        head_data = None

        try:
            head_10 = deque([_line.strip() for _line in content_lines[0:10]])
            while head_10:
                line = head_10.popleft()
                if line == "---":
                    index = 1
                    while head_10:
                        line = head_10.popleft()
                        index += 1
                        if line == "---":
                            head_data = [meta.strip() for meta in content_lines[1:index - 1] if meta.strip()]
                            self.md_content = "\n".join(content_lines[index:])
                            break
        except IndexError:
            pass

        if head_data:
            for line in head_data:
                if line.startswith('title'):
                    self.md_title = line.replace('title: ', '').strip().replace('\\', '-')
                elif line.startswith('created'):
                    self.md_created = utc2local(line[10:-1])
                elif line.startswith('modified'):
                    self.md_modified = utc2local(line[11:-1])
                elif line.startswith('tags'):
                    self.md_tags = re.search(r"\[(.*)\]", line).group(1).split(',')
                    self.md_tags = [tag.replace('/', '-') for tag in self.md_tags]
        else:
            self.md_title = self.md_name

    def parse_md_from_dict(self):
        self.md_name = self.md_dict.get('md_name', self.md_name)
        self.md_title = self.md_dict.get('md_title', self.md_title)
        self.md_created = self.md_dict.get('md_created', self.md_created)
        self.md_modified = self.md_dict.get('md_modified', self.md_modified)
        self.md_tags = self.md_dict.get('md_tags', self.md_tags)
        self.md_content = self.md_dict.get('md_content', self.md_content)

    def to_dict(self) -> dict:
        if self.md_dict:
            return self.md_dict

        return {
            "md_name": self.md_name,
            "md_title": self.md_title,
            "md_created": self.md_created,
            "md_modified": self.md_modified,
            "md_tags": self.md_tags,
            "md_content": self.md_content
        }

    def to_str(self) -> str:
        if self.md_str:
            return self.md_str

        head_template = """---
tags: [{0}]
title: {1}
created: '{2}'
modified: '{3}'
---
"""
        head = head_template.format(
            ','.join(self.md_tags),
            self.md_title,
            self.md_created,
            self.md_modified
        )
        return head + self.md_content

    def to_file(self, export_file: str):
        """

        :param export_file: Export MarkDown File Path
        :return:
        """
        export_file = Path(export_file)
        export_file.write_text(self.to_str(), encoding='utf-8')


def utc2local(utcstr: str) -> str:
    utc_date = datetime.strptime(utcstr, "%Y-%m-%dT%H:%M:%S.%fZ")
    local_date = utc_date + timedelta(hours=8)
    return datetime.strftime(local_date, '%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    md_file_instance = "D:\\notes\\Httpie.md"
    md_str_instance = """---
    tags: [Linux/Develop, System, V2ray]
    title: This is a title
    created: '2019-10-11T08:28:52.029Z'
    modified: '2020-02-15T14:37:12.812Z'
    ---
    # This is a H1 title"""
    markd = MdFile(md_file=md_file_instance)
    # print(markd.to_str())
    print(markd.to_dict())
