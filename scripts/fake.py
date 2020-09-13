from scripts.base_env import *

from django.utils import timezone
import faker


def create_superuser():
    print("create blog user")
    return User.objects.create_superuser("luocy", "admin@luocy.com", "luocy")


def create_categories_and_tags():
    print("create categories and tags")
    category_list = ["Python学习笔记", "开源项目", "工具资源", "程序员生活感悟", "test category"]

    tag_list = [
        "django",
        "Python",
        "Pipenv",
        "Docker",
        "Nginx",
        "Elasticsearch",
        "Gunicorn",
        "Supervisor",
        "test tag",
    ]
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)


def create_fake_posts():
    fake = faker.Faker("zh_CN")
    super_user = create_superuser()
    print("create fake posts")

    for _ in range(100):  # Chinese
        tags = Tag.objects.order_by("?")
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by("?").first()

        created_time = fake.date_time_between(
            start_date="-1y",
            end_date="now",
            tzinfo=timezone.get_current_timezone()
        )
        post = Post.objects.create(
            title=fake.sentence().rstrip("."),
            markdown="\n\n".join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=super_user,
        )
        post.tags.add(tag1, tag2)
        post.save()


def create_fake_friendlink():
    print("create fake friendlinks")
    fake = faker.Faker()

    for _ in range(5):
        FriendLink.objects.create(
            link_name=fake.name(),
            link_url=fake.url()
        )


clean_database()
create_categories_and_tags()
create_fake_friendlink()
create_fake_posts()
