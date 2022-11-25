<h1 align="center">AdoteMe</h1>

<div align="center">
Luiza Bretas (1911867) & Isabella Carmo (1911907)

Servidor: http://isabellalcarmo.pythonanywhere.com/adoteme/
</div>

## 🐶 Sobre o AdoteMe
Nosso projeto consiste em um site para adoção de animais domésticos.

É fornecida uma lista de Estados brasileiros que possuem unidades de adoção. Em cada uma dessas unidades o usuário pode visualizar suas informações, assim como verificar quais animais estão para adoção e adicioná-los à sua lista de adoção, caso desejem.

## 🐱 Tipos de Usuário
O AdoteMe possui três tipos de usuário: O cliente, o veterinário e o administrador.

O cliente inicia sua navegação clicando em "Estados para adoção", disponível no painel à esquerda. Ao clicar em um dos Estados exibidos na tela, o usuário acessa a lista de unidades de adoção disponíveis no estado em questão e, similarmente, ao clicar no nome de alguma das unidades exibidas, o mesmo alcança uma página que contém mais informações sobre a unidade de adoção em questão, junto com os nomes de todos os animais da unidade que estão para adoção. Caso ele deseje adotar um dos animais, ele deverá clicar no símbolo representado por "➕" para adicionar o animal à sua lista de adoção e deverá preencher os dados com os motivos do desejo de sua adoção pelo animal escolhido. Ademais, o usuário também poderá acessar tal lista de adoção clicando em "Meus animais", disponível no painel à esquerda. Em tal página, ele poderá excluir animais da sua lista de adoção e também poderá visualizar quais que o mesmo já adotou.

O veterinário pode realizar todas as mesmas ações que um cliente pode pois, afinal, qualquer pessoa pode realizar uma adoção. Além do mais, o mesmo pode gerenciar só (e somente) sua unidade de adoção caso o mesmo possua alguma. Para isso, basta clicar em "Minhas Unidades", disponível no painel à esquerda e, caso ele possua alguma, o mesmo poderá visualizar as informações da sua unidade de adoção e também alterá-las, assim como poderá adicionar novos animais para adoção à sua unidade. Caso o mesmo não possua uma unidade, ele poderá clicar em "Estados para adoção", disponível no painel à esquerda, escolher um Estado de preferência e clicar em "Nova Unidade" para adicionar sua unidade ao Estado escolhido. Ademais, o mesmo, ao clicar para visualizar as informações de sua unidade e, caso houver algum animal para adoção, clicar no nome de um dos animais, ele alcançará uma página no qual lhe mostrará quais pessoas querem adotar tal animal. O mesmo poderá realizar a aprovação da adoção do animal para a pessoa escolhida. O mesmo também pode visualizar quais animais já foram adotados na unidade.

O administrador é o único usuário com o poder de realizar todas as opções de CRUD, sendo com os Estados, as unidades de adoção e os animais em suas respectivas unidades de adoção. O mesmo terá acesso à todas as páginas, tanto as do cliente como as do veterinário.

No momento do cadastro, o usuário tem somente as opções de escolher entre "cliente" e "veterinário".

## 🐰 Funcionalidades
Usamos o framework Bootstrap, além de customizarmos alguns elementos no nosso próprio arquivo de estilos. Além disso, realizamos o uso, de JQuery, AJAX, e da biblioteca de fontes "FontAwesome". Temos operações de CRUD para os estados, unidades de adoção, listas de adoção e animais, onde nem todas essas tabelas têm todas as 4 operações.

Dentre as funcionalidades do sistema, destacamos a função de completar automaticamente, caso desejável, o campo "tipo do animal" na página de adicionar o animal em uma unidade de adoção, feito usando AJAX e JQuery, que sugere ao usuário os tipos de animais baseados nos tipos já existentes no banco de dados. Além disso, fizemos a validação de alguns campos chave dos formulários através de scripts em javascript, possibilitando informar o usuário durante o preenchimento do formulário.
