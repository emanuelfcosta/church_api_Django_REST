
from django.contrib import admin
from django.urls import path,include
from church.views import MembersViewSet,ChurchViewSet,FinancialViewSet,OccasionViewSet,PrayerViewSet,StudyViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('members', MembersViewSet)
router.register('churches', ChurchViewSet)
router.register('financial', FinancialViewSet)
router.register('occasions', OccasionViewSet)
router.register('prayers', PrayerViewSet)
router.register('studies', StudyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
