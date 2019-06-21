from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post
from comments.forms import CommentForm


def post_comment(request, post_pk):
    # 先获取评论的文章,后面把评论和被评论的文章关联起来
    # 使用Django提供的get_object_404
    # 这个函数的作用是当文章存在是获取 不存在时返回404给用户
    post = get_object_or_404(Post, pk=post_pk)
    # HTTP 请求有get和post 两种 一般用户是通过表单提交数据都是post请求
    # 因此只有当客户的请求是post的时候才需要处理
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中 这是一个字典对象
        # 我们利用这些数据构造了commentform的实例这样的话Django的表单就成了
        # 当调用form_is_vaild()方法时,Django会自动的帮我们检查表单的数据是否符合格式的需求
        form = CommentForm(request.POST)
        if form.is_valid():
            # 检查是否是合法的 调用表单的save()方法保存到数据库
            # commit = False 的作用是仅仅利用,表单的数据生成comment实例,但不保存到评论数据到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章连接起来
            comment.post = post
            # 将最终的评论数保存到数据库,调用模型实例的save()方法
            comment.save()
            # 从新定向到 详情页
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {"post": post,
                       "form": form,
                       "comment_list": comment_list,
                       }
            return render(request, "blog/detail.html", context=context)
    return redirect(post)
