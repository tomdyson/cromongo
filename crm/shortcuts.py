
from django.template import RequestContext
from django.shortcuts import render_to_response


def render_with_context(request, template, args={}):
    """
    Wraps render_to_response() to use context processors
    """
    return render_to_response(template, args, context_instance=RequestContext(request))

