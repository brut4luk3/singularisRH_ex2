from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'plan', views.PlanViewSet)
router.register(r'customerplan', views.CustomerPlanViewSet)
router.register(r'contract', views.ContractViewSet)
router.register(r'contractrule', views.ContractRuleViewSet)
router.register(r'parkmovement', views.ParkMovementViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]