# https://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.contrib import messages
from django.db.models import Q

import time

MAXSATIR = 50
BHARFX = "Iİ"
KHARFX = "ıi"

def kucukharfyap(sozcuk):
    ss = ''
    for i in range(len(sozcuk)):
        ok = False
        for j in range(len(BHARFX)):
            if sozcuk[i] == BHARFX[j]:
                ss += KHARFX[j]
                ok = True
                break
        if ok == False:
            ss += sozcuk[i]
    ss = ss.lower()
    return ss

def buyukharfyap(sozcuk):
    ss = ''
    for i in range(len(sozcuk)):
        ok = False
        for j in range(len(KHARFX)):
            if sozcuk[i] == KHARFX[j]:
                ss += BHARFX[j]
                ok = True
                break
        if ok == False:
            ss += sozcuk[i]
    ss = ss.upper()
    return ss

# logfile = open('timelog.log', "a")
def print_toplam_gecen_sure(func):
    def ic_fonksiyon(*arg):
        # global gentoplam
        t0 = time.perf_counter()  # fonksiyonun başlangıç zamanı
        orijinal_fonksiyon = func(*arg)  # Orijinal fonksiyon
        t = time.perf_counter() # fonksiyonun bitiş zamanı
        fad = func.__name__  # fonksiyonun adı
        with open('timelog.log', "a") as logfile:
            print(f"{fad:20s} {(t - t0) * 1000.0:0.3f} ms {time.strftime('%d.%m.%Y %H:%M:%S', time.localtime())}",
                  file=logfile, flush=True)
        # print(f"{fad:20s} {(t - t0)*1000.0:0.3f} ms", file=logfile, flush=True)
        # gentoplam+=(t-t0)*1000
        return orijinal_fonksiyon
    return ic_fonksiyon

def log_user(username, fad, idno='',  kod='', klas='',):
    with open('userlog.log', "a") as f:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {username} {fad} {idno} {kod} {klas}",
              file=f, flush=True)

def log_scripts(username, fad, idno='',  kod='', request=None):
    with open('userscripts.log', "a") as f:
        ss = str(request).split('&')
        s= ss[0]
        for s1 in ss[1:]:
            s2 = s1.split('=')
            if len(s2)==2:
                if (s2[0]>'') and (s2[1]>''):
                    s += '&'+s1

        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {username} {fad} {idno} {kod} {s}",
              file=f, flush=True)
        # print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {username} {fad} {idno} {kod} {s} | {request}",
        #       file=f, flush=True)
    # print(s)

@login_required()
def show_last_users(request):
    permissions = request.user.get_user_permissions()
    # print(permissions)
    if 'admin.view_logentry' in permissions:
        # print("yetki tamam")
        last_users=[]
        with open('userlog.log', "r") as f:
            last_users = f.readlines()
        if last_users:
            last_users = last_users[-1:-500:-1]
            # last_users = last_users[-1:-25:-1]
        print(len(last_users))
        return render(request, 'home.html', {"last_users": last_users})
    return redirect("/")


def export_csv(model, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.title),
            smart_str(obj.description),
        ])
    return response

export_csv.short_description = u"Export CSV"



if __name__ == "__main__":
    pass


