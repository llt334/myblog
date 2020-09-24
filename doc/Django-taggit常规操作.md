# Django-taggit常规操作

​    Django-taggit是一个实现了标签功能的第三方库，在Django开发中如果需要一个标签表即可使用这个插件，省得自己动手设计实现快速开发。

## 安装及设置

首先在虚拟环境中安装Django-taggit

pip install django-taggit

安装后在项目文件夹的setting.py添加‘taggit’项

```python
INSTALLED_APPS = [
    # 省略显示其他项...
    
    'taggit',
]

```

此时如果做数据迁移，同步到数据库，会发现多了一个**taggit_tag**的数据表，有三个字段分别*id, name, slug*。

## 在模型类及表单类中定义

我们需要在Articles模型类中增加标签，可以通过以下代码定义

```python
from taggit.managers import TaggableManager

class Articles(models.Model):
    # 略去其他字段定义
    
    tags = TaggableManager(blank=True)
    
    
```

做数据迁移，发现多了一个多对多的数据表

在表单类中添加tags字段

```python
class ArticleForm(forms.ModelForm):
    class Meta:
        # 略去其他代码
        
        fields = ('title', 'body', 'tags')
```

## 在视图中保存标签数据

在新建Articles中通过关联的表单类与对应模板实现数据录入及保存。

```python
@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            article_form.save_m2m()
        return redirect("article:article_list")
    else:
        columns = ArticleColumn.objects.all()
        article_form = ArticleForm()
        context = {'article_form': article_form, 'columns': columns}
        return render(request, 'article/create.html', context)
```

当在表单调用save方法保存时，如果有commit=False时，必须还要调用表单类的sava_m2m()才能保存标签表和对应的多对多表中的数据。

略去模板代码实现，需注意**输入多个标签最好用英文的逗号隔开**。

## 在模板中显示标签

我们可以用bootstrap中的badge显示标签，代码如下。

```html
<span>
    {% for tag in article.tags.all %}
        <a href="#"
           class="badge badge-secondary" 
        >
            {{ tag }}
        </a>
    {% endfor %}
</span>

```

