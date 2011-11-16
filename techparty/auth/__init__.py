#encoding=utf-8
from django.utils import simplejson

from social_auth.backends import ConsumerBasedOAuth, OAuthBackend, USERNAME

# weibo configuration
WEIBO_SERVER = 'api.t.sina.com.cn'
WEIBO_REQUEST_TOKEN_URL = 'http://%s/oauth/request_token' % WEIBO_SERVER
WEIBO_ACCESS_TOKEN_URL = 'http://%s/oauth/access_token' % WEIBO_SERVER

WEIBO_AUTHORIZATION_URL = 'http://%s/oauth/authorize' % WEIBO_SERVER
WEIBO_CHECK_AUTH = 'http://%s/account/verify_credentials.json' % WEIBO_SERVER


class WeiboBackend(OAuthBackend):
    """新浪微博OAuth验证的Backend
    """
    name = 'weibo'
    EXTRA_DATA = [('name', 'name'), ('description', 'description'),
                  ('profile_image_url', 'avatar')]
    # 格式: (返回键值，存储至数据库的名称)

    def get_user_details(self, response):
        """获取新浪微博用户的帐号信息"""

        return {USERNAME: response['screen_name'],
                'profile_image_url': response['profile_image_url'],
                'description': response['description'],
                'email': ''}  # email一项一定要，哪怕是空的，否则创建用户失败!


class WeiboAuth(ConsumerBasedOAuth):
    AUTHORIZATION_URL = WEIBO_AUTHORIZATION_URL
    REQUEST_TOKEN_URL = WEIBO_REQUEST_TOKEN_URL
    ACCESS_TOKEN_URL = WEIBO_ACCESS_TOKEN_URL
    SERVER_URL = WEIBO_SERVER
    AUTH_BACKEND = WeiboBackend
    SETTINGS_KEY_NAME = 'WEIBO_CONSUMER_KEY'
    SETTINGS_SECRET_NAME = 'WEIBO_CONSUMER_SECRET'

    def user_data(self, access_token):
        """Return user data provided"""
        request = self.oauth_request(access_token, WEIBO_CHECK_AUTH)
        json = self.fetch_response(request)
        try:
            return simplejson.loads(json)
        except ValueError:
            return None

BACKENDS = {
    'weibo': WeiboAuth,
}
