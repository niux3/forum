from django.urls import reverse_lazy
from forum.forms import AdvancedSeachForm, SeachForm



def boards_urls(request):
    args = {
        'index': {
            'name': 'forum:index',
            'params': None
        },
        'last_topics': {
            'name': 'forum:last_topics',
            'params': 'derniers-sujets'
        },
        'last_posts': {
            'name': 'forum:last_posts',
            'params': 'dernieres-reponses'
        },
        'my_topics': {
            'name': 'forum:last_topics',
            'params': 'mes-sujets'
        },
        'my_posts': {
            'name': 'forum:last_posts',
            'params': 'mes-reponses'
        },
    }
    urls = {
        k: reverse_lazy(v['name'], kwargs={ 'categories': v['params'] }) if v['params'] is not None else reverse_lazy(v['name']) 
        for k, v in args.items()
    }

    return {
        'boards_urls': urls
    }

def get_search_forms(request):
    return {
        'search_form': SeachForm(),
        'advanced_search_form': AdvancedSeachForm(),
    }
