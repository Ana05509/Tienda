from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ClienteViewSet, VentaViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('clientes', ClienteViewSet)
router.register('ventas', VentaViewSet)

urlpatterns = router.urls
