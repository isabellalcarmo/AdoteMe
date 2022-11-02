from django.urls import path
from adoteme.views.views_homepage import index
from adoteme.views.views_auth import register_user, user_registration_done
from adoteme.views.views_estados import lista_estados, criar_estado, deletar_estado
from adoteme.views.views_unidades import lista_unidades, criar_unidade, deletar_unidade, editar_unidade, visualizar_unidade, minhas_unidades
from adoteme.views.views_animal import criar_animal, deletar_animal, editar_animal
from adoteme.views.views_lista_adocao import visualizar_lista_adocao, adicionar_animal_lista, deletar_animal_lista


urlpatterns = [
    path('', index, name='home'),

    # URLs de criação de conta do usuário
    path('registration/register_user', register_user, name='register_user'),
    path('registration/registration_done', user_registration_done, name='registration_done'),

    # URLs dos Estados para adoção
    path('estados/lista_estados', lista_estados, name='lista_estados'),
    path('estados/criar_estado', criar_estado, name='criar_estado'),
    path('estados/deletar_estado/<int:estado_id>', deletar_estado, name='deletar_estado'),

    # URLs das Unidades
    path('unidades/lista_unidades/<int:estado_id>', lista_unidades, name='lista_unidades'),
    path('unidades/criar_unidade/<int:estado_id>', criar_unidade, name='criar_unidade'),
    path('unidades/deletar_unidade/<int:unidade_id>', deletar_unidade, name='deletar_unidade'),
    path('unidades/editar_unidade/<int:unidade_id>', editar_unidade, name='editar_unidade'),
    path('unidades/visualizar_unidade/<int:unidade_id>', visualizar_unidade, name='visualizar_unidade'),
    path('minhas_unidades/<int:responsavel_id>', minhas_unidades, name='minhas_unidades'),

    # URLs dos Animais
    path('unidades/animais/criar_animais/<int:unidade_id>', criar_animal, name='criar_animal'),
    path('unidades/animais/deletar_animal/<int:animal_id>', deletar_animal, name='deletar_animal'),
    path('unidades/animais/editar_animal/<int:animal_id>', editar_animal, name='editar_animal'),

    # URLs da Lista de Adoção
    path('lista_adocao/', visualizar_lista_adocao, name='lista_adocao'),
    path('lista_adocao/adicionar_animal_lista/<int:animal_id>', adicionar_animal_lista, name='adicionar_animal_lista'),
    path('lista_adocao/deletar_animal_lista/<int:animal_id>', deletar_animal_lista, name='deletar_animal_lista'),
]