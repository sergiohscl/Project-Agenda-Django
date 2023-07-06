# Instalando ambiente virtual
python3 -m venv venv

# Ativando e desativando ambiente virtual
. venv/bin/activate

deactivate

# Instalando django no ambinete virtual
pip install django

# Iniciando project django
django-admin startproject project .

# Rodando django-admin
python manage.py runserver

# criando app
python manage.py startapp contact

# Configure o .gitignore
# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

