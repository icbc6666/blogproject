from django.db import models
from django.contrib.auth.models import User
#django.contrib.auth.models
# Create your models here.
from django.urls import reverse


class Category(models.Model):
    """分类模型"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签模型"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章模型"""
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文 这里用了 textFIeld
    body = models.TextField()
    # 文章的创建时间和最后一次的修改时间
    created_time= models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章的摘要 可以没有文章的摘要 但是默认的情况 charfield 要求我们必须传入数据否则就报错
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签 分类与标签的模型 我们已经定义在上面
    # 这里把文章对应的数据库表和分类, 标签对应的数据库表关联了起来,但是关联形式不同
    # 我们规定一篇文章只是对应于一个分类,但是一个分类下应该有很多文章 所以用到了foreignkey 即一对多的的关联关系
    # 而对于标签来说,一篇文章可以有多个标签,同时一个标签下也可以有多篇文章,所以我们使用manytomanyfield ,表明是多对多的关系
    # 同时我们规定了文章可以没有标签,因此为标签tags,指定了blank = True
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者,这里是从auth.model 导入的
    # 这里我们通过foreignkey把文章和user关联起来
    # 我们规定了一篇文章只有一个作者,而一个作者可以写很多文章,所以是一对多的关联关系
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 自定义get_absoulte_url方法
    # 从django.url 中引入reverse

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']




