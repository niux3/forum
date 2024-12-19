from django import template
from forum.models import PrivateMessage


register = template.Library()

@register.inclusion_tag('includes/display_count_mp.html', takes_context=True)
def display_count_mp(context):
    current_user = context.get('request').user.id
    count = PrivateMessage.objects.filter(to_user=current_user).count()
    return {'has_mp': count > 0, 'message_count': count}

@register.inclusion_tag('includes/display_link_mp.html', takes_context=True)
def display_link_mp(context):
    current_user = context.get('request').user.id
    count = PrivateMessage.objects.filter(to_user=current_user).count()
    return {
        'has_mp': count > 0, 
        'current_user': current_user,
        'is_pluralize': count > 1,
        'message_count' : count
    }
