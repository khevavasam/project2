from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class ArticlePage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    template = "home/article_page.html" 
