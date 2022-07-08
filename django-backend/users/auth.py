from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class CoolTokenAuthentication(TokenAuthentication):
    def enforce_csrf(self, request):
        return


class CoolSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
