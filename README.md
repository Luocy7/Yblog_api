# Yblog_api

本项目是学习 [HelloDjango-blog-tutorial](https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial) 后对本身 [Yblog](https://github.com/Luocy7/YBlog) 项目的重构，由原先的 Flask 转为使用 `Django REST Framework` 做前后端分离

1. 克隆代码到本地：

```
$ git clone https://github.com/Luocy7/Yblog_api.git
```

2. 设置项目环境变量

项目根目录新建`envs` 文件夹， 新建两个env文件
- `.env.local` : 本地运行环境变量
- `.env.production` : 生产环境运行环境变量

```
$ cd Yblog_api
$ mkdir envs
$ vim envs/.env.local

# 写入
DEBUG=on
SECRET_KEY=your-secret-key
# 替换为实际值
DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/DATABASE
```

**记得把`envs` 文件夹添加进`.gitignore` 文件**

默认使用本地运行环境

如果想使用生产环境变量 需配置`PROJECT_ENV` 变量为`production` 

3. 安装项目依赖

```
$ pip install -r requirements.txt
```

4. 迁移数据库

```
$ python manage.py migrate
```

5. 创建后台管理员账户

```
$ python manage.py createsuperuser
```

6. 运行开发服务器

```
$ python manage.py runserver
```
