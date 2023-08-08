# MULTICHATBOTS DJANGO PROJECT

In this small Django project with single app, I gathered the links of some  open-source or free to use ai chatbot applications in a single page.

Using the application, it might be easier to compare the answers given to the same prompt by different AI chatbots.

Nowadays, lots of new chatbot applications are shared to the public. You can easily add these to your portfolio.

Also, you can add different types of links to the database.

I will prepare a video about the project, explaining some details.

That project also might be a simple starting point to learn Django.

## INSTALLATION
- cd ~/Desktop/ai_projects/
- git clone https://github.com/ahmetax/MultiChatBots-on-Django.git
- or
- git clone git@github.com:ahmetax/MultiChatBots-on-Django.git

- cd MultiChatBots-on-Django
- python3 -m venv env
- source env/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt

## ESTABLISH DATABASE
- python manage.py makemigrations
- python manage.py migrate

## SUPERUSER
- python manage.py createsuperuser

## RUN
- python manage.py runserver

## DOCKER RUN
- docker-compose up


# MULTICHATBOTS DJANGO PROJESİ

Bu küçük Django projesinde tek bir uygulama ile açık kaynaklı veya ücretsiz kullanılabilen yapay zeka sohbet botu uygulamalarının bağlantılarını tek bir sayfada topladım.

Bu uygulama kullanılarak farklı yapay zeka sohbet botları tarafından aynı soruya verilen cevapları karşılaştırmak daha kolay olabilir.

Günümüzde, herkesle paylaşılan birçok yeni sohbet botu uygulaması bulunuyor. Bu uygulamaları portföyünüze kolayca ekleyebilirsiniz.

Ayrıca, veritabanına farklı türdeki bağlantıları da ekleyebilirsiniz.

Bu proje hakkında bazı detayları açıklayan bir video hazırlayacağım.

Bu proje aynı zamanda Django'yu öğrenmek için basit bir başlangıç noktası olabilir.

## KURULUM
- cd ~/Desktop/yz_projeleri/
- git clone https://github.com/ahmetax/MultiChatBots-on-Django.git
- or
- git clone git@github.com:ahmetax/MultiChatBots-on-Django.git

- cd MultiChatBots-on-Django
- python3 -m venv env
- source env/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt

## VERİTABANI OLUŞTURMA
- python manage.py makemigrations
- python manage.py migrate
    
## SUPERUSER
- python manage.py createsuperuser

## ÇALIŞTIRMA
- python manage.py runserver

## DOCKER İLE ÇALIŞTIRMA
- docker-compose up


