from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()
user_model = get_user_model()

@register.filter(name='author_details')
def author_details(author, current_user):
# @register.simple_tag(takes_context=True)
# def author_details_tag(context):
    # request = context['request']
    # current_user = request.user
    # post = context['post']
    # author = post.author

    if not isinstance(author, user_model):
        return ''
    
    if author == current_user:
        return format_html('<strong>me</strong>')
    
    prefix = ''
    suffix = ''

    if author.first_name and author.last_name:
        name = f'{author.first_name} {author.last_name}'
    else:
        name = author.username

    if author.email:
        # prefix = f'<a href="mailto:{escape(author.email)}">'
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html('</a>')

    # return mark_safe(f'{prefix}{escape(name)}{suffix}')
    return format_html('{}{}{}', prefix, name, suffix)

@register.simple_tag
def row(extra_classes=''):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
    return format_html('</div>')

@register.simple_tag
def col(extra_classes=''):
    return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endcol():
    return format_html('</div>')
