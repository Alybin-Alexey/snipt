from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class BlogMiddleware:
    def process_request(self, request):
        request.blog_user = None

        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')

        if host != 'snipt.net' and host != 'snipt.localhost':
            # nick.snipt.net or nicksergeant.com or blog.nicksergeant.com

            if len(host_s) > 2:
                # nick.snipt.net or blog.nicksergeant.com

                if host_s[1] == 'snipt':
                    # nick.snipt.net or nick.snipt.localhost

                    blog_user = ''.join(host_s[:-2]).replace('-', '_')
                    request.blog_user = get_object_or_404(User, username__iexact=blog_user)
                else:
                    # blog.nicksergeant.com

                    # Get user for that domain
                    pass
            else:
                # nicksergeant.com

                # Get user for that domain
                pass
            pass

        if host == 'nicksergeant.com':
            request.blog_user = User.objects.get(id=3)
