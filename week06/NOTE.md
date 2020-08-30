#### 创建 Django 项目
```BASH
django-admin startproject douban
```

#### 创建应用
```BASH
cd project_dir
python manage.py startapp index
```

#### Django 启动服务背后做了些什么
1. 解析运行参数；
2. 加载 runserver 模块；
3. 检查 settings.py 中的配置。INSTALL_APPS是否正确，IP端口是否被占用， ORM 是否能成功读取；
4. 实例化 WSGUServer；
5. 动态创建接收 HTTP 请求的类。