"""Views for the demo — plain functions: HttpRequest in, HttpResponse out.

In a real project these live in the app's views.py and are referenced by
name in urls.py.
"""

from django.http import HttpResponse, HttpResponseNotFound

from .models import Article


def home(request):
    """A view is *just* a callable: HttpRequest in, HttpResponse out."""
    return HttpResponse("<h1>Django demo</h1><p>Welcome!</p>")


def article_detail(request, article_id: int):
    """ORM query + a tiny bit of HTML. This is the 'server-side rendering'
    part of Django: the view builds HTML for the browser."""
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return HttpResponseNotFound("<p>Article not found.</p>")

    # F-strings in HTML are a demo shortcut; real Django uses templates
    # (article.html with {{ article.title }} placeholders).
    html = f"<h1>{article.title}</h1><p>{article.body}</p>"
    return HttpResponse(html)


def article_list(request):
    """A list endpoint — again, view + ORM + HTML."""
    items = "".join(f"<li>{a.title} ({a.views} views)</li>" for a in Article.objects.all())
    return HttpResponse(f"<ul>{items}</ul>")
