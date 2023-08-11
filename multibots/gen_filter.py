from django.db.models import Q, F
import operator
from functools import reduce
from django.conf import settings
import os

def create_temp_and_user_if_not_exists(request):
    user = request.user.username
    temp_dir='temp/'
    user_dir = f"{temp_dir}/{user}/"
    # print(temp_dir,user_dir)
    if os.path.exists(user_dir):
        return
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)

def gen_sorgula(request, form, satirlar):
    # print()
    # print(5*"gen_sorgula_")
    context = dict()
    if request.method == 'GET':
        # isnull metodunu döngü içinde uygula
        # https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
        try:
            if form['tarih1'].value() > '':
                satirlar = satirlar.filter(Q(tarih__gte=form['tarih1'].value()))
                # print("tarih1, len(satirlar)=", len(satirlar))
            if form['tarih2'].value() > '':
                satirlar = satirlar.filter(Q(tarih__lte=form['tarih2'].value()))
                # print("tarih2, len(satirlar)=", len(satirlar))
        except:
            pass
        # print(form.fields)
        for ff in form.fields:
            # print(ff, form[ff].value(),type(form[ff]),form[ff].field.widget.input_type)
            yff = ff
            try:
                if ff in ['tarih1', 'tarih2', 'tarih', 'sort', 'nozero', 'showfields']:
                    continue
                # print(f"field={ff} input_type={form[ff].field.widget.input_type}")
                if form[ff].value() == None:
                    continue
                elif (form[ff].field.widget.input_type == 'checkbox'):
                    # print('completed->checkbox: ', form[ff].value())
                    if  (form[ff].value() == True):
                        filter = yff + "__" + 'icontains'
                        satirlar = satirlar.filter(Q(**{filter: form[ff].value()}))
                    elif (form[ff].value() == False):
                        continue
                elif (form[ff].field.widget.input_type == 'select'):
                    # print('completed->select: ', form[ff].value())
                    if  (form[ff].value() == True):
                        filter = yff + "__" + 'icontains'
                        satirlar = satirlar.filter(Q(**{filter: form[ff].value()}))
                    elif (form[ff].value() == False):
                        filter = yff + "__" + 'icontains'
                        satirlar = satirlar.filter(Q(**{filter: form[ff].value()}))
                    else:
                        continue
                elif ff in ['category']: 
                    filter = yff + "__name__" + 'icontains'
                    satirlar = satirlar.filter(Q(**{filter: form[ff].value()}))
                elif ff in ['user']: 
                    filter = yff + "__username__" + 'icontains'
                    satirlar = satirlar.filter(Q(**{filter: form[ff].value()}))
                elif form[ff].value() > '':
                    # print(ff, form[ff].value())
                    if '<None>' in form[ff].value():
                        filter = yff + "__" + 'isnull'
                        satirlar = satirlar.filter(**{filter: True})
                    elif '<Empty>' in form[ff].value():
                        filter1 = yff + "__" + 'isnull'
                        filter2 = yff + "__" + 'lt'
                        satirlar = satirlar.filter(Q(**{filter1: True}) |
                                                   Q(**{filter2: '!'}))
                    elif '<Full>' in form[ff].value():
                        filter1 = yff + "__" + 'isnull'
                        filter2 = yff + "__" + 'gt'
                        satirlar = satirlar.filter(Q(**{filter1: False}),
                                                   Q(**{filter2: ''}))
                    elif '<->' in form[ff].value():
                        filter1 = yff + "__" + 'gte'
                        filter2 = yff + "__" + 'lte'
                        pp = form[ff].value().split('<->')
                        if len(pp) == 2:
                            # print(Q(**{filter1: pp[0]}), Q(**{filter2: pp[1]}))
                            satirlar = satirlar.filter(Q(**{filter1: pp[0]}),
                                                       Q(**{filter2: pp[1]}))
                    else:
                        filter1 = yff + "__" + 'icontains'
                        filter2 = yff + "__" + 'iregex'
                        # print("filter1= ", filter1)
                        # print("filter2= ", filter2)
                        satirlar = satirlar.filter(Q(**{filter1: form[ff].value()}) |
                                                   Q(**{filter2: form[ff].value()}))
            except Exception as e:
                print(f"\nfiltre hatası field={yff}: {form[yff].value()}", str(e))
                pass

        # sort alanında bir şeyler var mı?
        if ('sort' in form.fields) and (form['sort'].value()) and (form['sort'].value()>''):
            # satirlar = satirlar.order_by(form['sort'].value)
            s1 = form['sort'].value()
            s = s1.split(',')
            # print("sort -> ", s, len(s))
            if len(s) > 1:
                if len(s)==2:
                    satirlar = satirlar.order_by(s[0].strip(),s[1].strip())
                elif len(s) == 3:
                    satirlar = satirlar.order_by(s[0].strip(), s[1].strip(),s[2].strip())
                else:
                    pass
            else:
                satirlar = satirlar.order_by(s1)


        context = {
            # 'header': header,
            'satirlar': satirlar,
            'form': form,
        }

    # check for showfilters checkbox
    query = request.GET.get('showfilters')
    print("showfilters", query)

    # print("1. aşama satır sayısı=", len(satirlar))
    # QUERY PART
    query = request.GET.get('qq')
    if query:
        # print("arama sorgusu yapılıyor: ", query)
        # https://stackoverflow.com/questions/4720079/django-query-filter-with-variable-column
        # https://www.cyberhavenprogramming.com/blog/2019/4/23/django-q-object-how-make-many-complex-multiple-and-dynamic-queries-python-reduce-function-functools-or-operator-and-requestget-search-fields-parameters/

        q = []
        for yff in form.fields:
            ff = yff

            if ff in ['tarih1', 'tarih2','tarih', 'sort', 'nozero']:
                pass
            elif (form[ff].field.widget.input_type == 'checkbox'):
                pass
            elif ff in ['category']: 
                filter = yff + "__name__" + 'icontains'
                q.append(Q(**{filter: query}))
            elif ff in ['user']: 
                filter = yff + "__username__" + 'icontains'
                q.append(Q(**{filter: query}))
            else:
                filter1 = ff + "__" + 'icontains'
                q.append(Q(**{filter1: query}))
                filter1 = ff + "__" + 'iregex'
                q.append(Q(**{filter1: query}))

        # print("form.fields = ", form.fields)
        # print("q= ", q)
        try:
            # print("REDUCE= ", reduce(operator.or_, q))
            satirlar = satirlar.filter(reduce(operator.or_, q)).distinct()
        except Exception as e:
            print(f"\nqq hatası field={yff}: ", str(e))
            pass
        
        context = {
            # 'header': header,
            'satirlar': satirlar,
            'form': form,
        }
    # return context
    # print(satirlar)
    # print("len(satirlar)= ",len(satirlar))
    return satirlar, form
