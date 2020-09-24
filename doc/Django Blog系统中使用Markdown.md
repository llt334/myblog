# Django中使用Markdown

**说明：**本文档详细记录了在开发blog系统中如何显示markdown文档。

## 1.安装插件及生成CSS文件

### 1.1首先在当前的开发环境中使用pip安装markdown。

```powershell
pip install Markdown
```

### 1.2安装Pygments支持代码高亮。

```powershell
pip install pygments
```

### 1.3使用Pyments在static目录下生成css文档

先在进入static文件夹中，再生成对应的css文件

```powershell
cd static
pygments -S monokai -f html -a .codehilite > monokai.css
```

**注：**其他样式可以在[官网下载](https://github.com/richleland/pygments-css)

## 2.在系统中引用CSS及文章主体中显示markdown格式。

### 2.1在模板文件导入CSS文件

```html
<link rel="stylesheet" href="{% static 'monokai.css'%}">
```

### 2.2在detail函数中让body字段markdown语法渲染成对应的html

```python
# 引入markdown
import markdown
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
        ])
    # 其他代码略...
```

### 2.3在显示博客的模板中增加safe过滤器

为了让body字段的html语法有效展示出来必须在对应的模板中加上safe过滤器。

```html
<div>
    {{article.body|safe}}
</div>
```

## 3.缺陷及问题

pygments提供的样式并不能很好的显示表格，可以使用jquery为table元素增加bootstarp的class样式，把本文2.3的代码段做修改。

```html
<div id="article_body">
      {{ article.body | safe }}
 </div>
<!--略过其他代码-->
<!--引入jquery 对body字段的id中的table元素增加class样式-->
<script src="{% static 'js/jquery-3.3.1.js' %}"></script>
<script>
     $("#article_body table").addClass("table table-bordered")
</script>
```



**注：** *另外在代码高亮中部分字体与背景颜色相似不能清晰的显示出来。*

