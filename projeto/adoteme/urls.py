from django.urls import path
from adoteme.views.views_homepage import index
from adoteme.views.views_auth import register_user, user_registration_done
from adoteme.views.views_estados import lista_estados, criar_estado, deletar_estado


urlpatterns = [
    path('', index, name='home'),

    # URLs de criação de conta do usuário
    path('registration/register_user', register_user, name='register_user'),
    path('registration/registration_done', user_registration_done, name='registration_done'),

    # URLs dos Estados para adoção
    path('estados/lista', lista_estados, name='lista_estados'),
    path('estados/criar_estado', criar_estado, name='criar_estado'),
    path('estados/deletar_estado/<int:estado_id>', deletar_estado, name='deletar_estado'),
]