# MULTICHATBOTS ON DJANGO
# PROJECT STEPS/ PROJE AŞAMALARI

## TARGET/ HEDEF
- To follow the improvements about AI chat bots
- Management of multiple AI chat bots from a single window
- To learn the first steps of a simple Django project

## REQUIREMENTS/ GEREKSİNİMLER
- Knowledge of some Python 
- Knowledge of the main linux shell commands

# FIRST STAGE / İLK ETAP

## PREPARATION OF THE COVER FOLDER / KABUK KLASÖRÜNÜN HAZIRLANMASI
- cd ~/Desktop/yz_projeleri
- mkdir multichatbots_on_django
- cd  multichatbots_on_django

## INSTALLATION OF VIRTUAL ENVIRONMENT/ SANAL ORTAMIN KURULUMU
- python3 -m venv env
- source env/bin/activate
- pip install --upgrade pip

## STARTING DJANGO PROJECT/ DJANGO PROJESİNİN BAŞLATILMASI
- pip install django
- django-admin startproject multibots .
- mkdir templates
- mkdir static
- mkdir staticfiles
- mkdir media
- mkdir temp
- mkdir temp/admin
- python manage.py runserver	-> kontrol
- tree -I 'env|__pycache__'	-> kontrol

## BOTS APP/ BOTS UYGULAMASI
- python manage.py startapp bots
- tree -I 'env|__pycache__'	-> kontrol

## SETTINGS.PY
- import os
- ALLOWED_HOSTS=['127.0.0.1','*']
- 'DIRS':[os.path.join(BASE_DIR,'templates')],

## LOCALS/ YEREL BİLGİLER
LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

## COLLECTSTATIC
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# pip install django-session-timeout
SESSION_EXPIRE_SECONDS = 86400 # Expire after 24hours

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_AGE = 86400

# SECOND STAGE/ İKİNCİ ETAP

## CALLS (URLS.PY)
       urlpatterns += static(settings.STATIC_URL, 
       document_root=settings.STATIC_ROOT)
       urlpatterns += static(settings.MEDIA_URL, 
       document_root=settings.MEDIA_ROOT)

## MIGRATIONS
python manage.py makemigrations

python manage.py migrate

## SUPERUSER
python manage.py createsuperuser

## VIEWS.PY






