import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from comments.forms import CommentForm
from .models import Post, Category


# 博客首页
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 博客详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',

                                  ])
    # 导入commentform
    form = CommentForm()
    # 获取这篇文章下的全部评论
    comment_list = post.comment_set.all()
    # 将文章的,表单以及文章下的评论作为模板变量传给detail.html模板,以便渲染相应的数据
    context = {"post": post,
               "form": form,
               "comment_list": comment_list
    }
    return render(request, 'blog/detail.html', context=context)


# 博客的归档
def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by("-created_time")
    return render(request,'blog/index.html', context={"post_list": post_list})


# 分类页面
def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by("-created_time")
    return render(request, 'blog/index.html', context={'post_list': post_list})

# def detail


