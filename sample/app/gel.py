from  django.core.urlresolvers import reverse

from app.contents.views import news_pager
from app.contents.models import News

def urls():      
    for i in [
                '/index.html',
                '/contact.html',
                '/news/index.html',
            ]:
        yield i

    #:News list pages
    for n in range(1,news_pager().num_pages+1):  
        yield reverse('contents_news_page',kwargs={'page':n} )

    #:News items
    for n in News.objects.all():
        yield  n.get_absolute_url()
