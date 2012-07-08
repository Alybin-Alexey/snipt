from django.http import HttpResponseRedirect, HttpResponseBadRequest
from annoying.decorators import ajax_request, render_to
from django.template.defaultfilters import striptags
from django.shortcuts import render_to_response
from django.template import RequestContext
from snipts.utils import get_lexers_list
from django.db.models import Count
from amazon.api import AmazonAPI
from django.conf import settings
from taggit.models import Tag

import os, urllib


@ajax_request
def amazon_search(request):

    products = []
    if request.GET.get('q'):
        amazon = AmazonAPI('AKIAJJRRQPTSPKB7GYOA', 'DIYz2g5vPjcWE4/YI7wEuUVAskwJxs2llFvGyI1a', 'snipt-20')
        products = amazon.search_n(5, Keywords=request.GET.get('q'), SearchIndex='Books')

    result = []
    for product in products:
        result.append({
            'image':   product.small_image_url.replace('http://ecx.images-amazon.com/images/I/', ''),
            'price':   product.list_price,
            'review':  striptags(product.editorial_review),
            'reviews': product.reviews,
            'title':   product.title,
            'url':     product.offer_url,
        })

    return {
        'result': result
    }

def amazon_image(request):
    if 'i' in request.GET:

        img_filename = request.GET.get('i')
        img_src = 'http://ecx.images-amazon.com/images/I/{}'.format(img_filename)
        img_loc = os.path.join(settings.STATIC_ROOT, 'images', 'amazon', img_filename)

        try:
            open(img_loc)
            return HttpResponseRedirect('/static/images/amazon/' + img_filename)
        except IOError:
            urllib.urlretrieve(img_src, img_loc)
            return HttpResponseRedirect('/static/images/amazon/' + img_filename)

        return HttpResponseRedirect('/static/images/amazon/' + img_filename)
    else:
        return HttpResponseBadRequest()
    return {}

@ajax_request
def lexers(request):
    lexers = get_lexers_list()
    objects = []

    for l in lexers:

        try:
            filters = l[2]
        except IndexError:
            filters = []

        try:
            mimetypes = l[3]
        except IndexError:
            mimetypes = []

        objects.append({
            'name': l[0],
            'lexers': l[1],
            'filters': filters,
            'mimetypes': mimetypes
        })

    return {'objects': objects}
def sitemap(request):

    tags = Tag.objects.filter(snipt__public=True)
    tags = tags.annotate(count=Count('taggit_taggeditem_items__id'))
    tags = tags.order_by('-count')[:1000]

    return render_to_response('sitemap.xml',
                             {'tags': tags},
                             context_instance=RequestContext(request),
                             mimetype='application/xml')

@render_to('tags.html')
def tags(request):

    all_tags = Tag.objects.filter(snipt__public=True).order_by('name')
    all_tags = all_tags.annotate(count=Count('taggit_taggeditem_items__id'))

    popular_tags = Tag.objects.filter(snipt__public=True)
    popular_tags = popular_tags.annotate(count=Count('taggit_taggeditem_items__id'))
    popular_tags = popular_tags.order_by('-count')[:20]
    popular_tags = sorted(popular_tags, key=lambda tag: tag.name)

    return {
        'all_tags': all_tags,
        'tags': popular_tags
    }
