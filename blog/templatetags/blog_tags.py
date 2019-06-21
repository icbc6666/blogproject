from blog.models import Post,Category
from django import template


register = template.Library()


# 获取最新模板文章标签 num代表前5篇
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by("-created_time")[:num]


@register.simple_tag()
def archives():
    return Post.objects.dates("created_time","month", order="DESC")


# 分类模板标签
@register.simple_tag()
def get_categories():
    return Category.objects.all()
