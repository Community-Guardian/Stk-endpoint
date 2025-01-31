from django.urls import re_path as url, include
from . import testviews
from .views import make_stk_push
test_patterns = [
	url(r'^$', testviews.index, name='django_daraja_index'),
	url(r'^oauth/success', testviews.oauth_success, name='test_oauth_success'),
	url(r'^stk-push/success', testviews.stk_push_success, name='test_stk_push_success'),
	url(r'^business-payment/success', testviews.business_payment_success, name='test_business_payment_success'),
	url(r'^salary-payment/success', testviews.salary_payment_success, name='test_salary_payment_success'),
	url(r'^promotion-payment/success', testviews.promotion_payment_success, name='test_promotion_payment_success'),
]

urlpatterns = [
	url(r'^$', testviews.index, name='index'),
	url(r'^make-stk-push/', make_stk_push, name='make_stk_push'),

	url(r'^tests/', include(test_patterns)),
]

