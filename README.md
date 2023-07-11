# Instalando ambiente virtual
python3 -m venv venv

# Ativando e desativando ambiente virtual
. venv/bin/activate

deactivate

# Instalando django no ambiente virtual
pip install django

# Iniciando project django
django-admin startproject project .

# Rodando django-admin
python manage.py runserver

# Migrando a base de dados do Django
python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário
python manage.py createsuperuser
python manage.py changepassword USERNAME

# criando app
python manage.py startapp contact

# arquivos estáticos
python manage.py collectstatic

# executando o script de dados fakes
python utils/create_contacts.py

# Configure o .gitignore
# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT


## Trabalhando com o model do Django
# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')