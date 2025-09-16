from rest_framework.throttling import SimpleRateThrottle

class GlobalRateThrottle(SimpleRateThrottle):
    '''
    Single counter shared by everyone. App-wide protection.
    '''
    scope = 'quotes_global'

    def get_cache_key(self, request, view):
        # One shared bucket of the whole API
        return self.cache_format % {'scope': self.scope, 'ident': 'ALL'}

class IPRateThrottle(SimpleRateThrottle):
    '''
    Per-IP bucket. Catches individual spammers (anon or logged-in).
    '''
    scope = 'quotes_ip'

    def get_cache_key(self, request, view):
        # Uses DRF's get_ident), which represents X-Forwarded-For behind a proxy
        ident = self.get_ident(request)
        if not ident:
            return None
        return self.cache_format % {'scope': self.scope, 'ident': ident}