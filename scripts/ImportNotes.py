from scripts.base_env import *
from scripts.MdFileUtils import MdFile


def insert_from_dict(md_dict: dict, user):
    default_cate = Category.objects.get_or_create(name="Default")[0]
    post = Post.objects.create(
        title=md_dict.get('md_title', ''),
        markdown=md_dict.get('md_content', ''),
        created_time=md_dict.get('md_created', ''),
        author=user,
        category=default_cate
    )
    tags = md_dict.get('md_tags', '')
    if tags:
        for tag in tags:
            post.tags.add(Tag.objects.get_or_create(name=tag)[0])
        post.save()


def insert():
    clean_database()

    import_folder = Path('D:\\notes')
    import_md_files = import_folder.glob('*.md')

    user = User.objects.create_superuser("luocy", "admin@luocy.com", "luocy")

    for md_file in import_md_files:
        md_dict = MdFile(md_file=md_file.__str__()).to_dict()
        insert_from_dict(md_dict, user)


if __name__ == '__main__':
    insert()
