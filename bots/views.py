from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.db.models import Q, F
import sys
import operator
from functools import reduce
import pickle
import os
from datetime import datetime

from .models import Bot
from .forms import BotForm, BotFilterForm
from multibots.gen_filter import gen_sorgula
from multibots.gen_filter import create_temp_and_user_if_not_exists

def home_view(request):
    if request.method == 'GET':
        query = request.GET
        pklfile = f'temp/{request.user}/bot.pkl'
        create_temp_and_user_if_not_exists(request)
        if len(query) > 0:
            # eğer ExcelResponse çağrıldıysa, pkl kaydetme!
            if request.GET.get('Filtre') == 'Export':
                pass
            else:
                # print(f"{pklfile} kaydediliyor")
                with open(pklfile, 'wb') as f:
                    pickle.dump(query, f)
        else:
            if os.path.isfile(pklfile):
                # print(f"{pklfile} okunuyor")
                if os.path.isfile(pklfile):
                    with open(pklfile, 'rb') as f:
                        query = pickle.load(f)
                    # print("query= ", query)
                    if not request.GET._mutable:
                        request.GET._mutable = True
                        request.GET = query
                        request.GET._mutable = False
    else:
        pass

    bots = Bot.objects.all()
    form = BotFilterForm(request.GET or None)
    bots, form = gen_sorgula(request, form, bots)

    context = {}
    context['bots'] = bots
    context['toplam'] = len(bots)
    context['form'] = form
    return render(request, 'bots/home.html', context=context)

def bot_remove_home_filters(request):
    # print(50*"=")
    # print("bots_remove_home_filters")
    pklfile = f'temp/{request.user}/bot.pkl'
    try:
        os.remove(pklfile)
    except: 
        pass

    return redirect("bot_home_view")

def bot_remove_list_filters(request):
    pklfile = f'temp/{request.user}/bot.pkl'
    try:
        os.remove(pklfile)
    except: 
        pass

    return redirect("bot_list")


# ---Bots-------------------------------------------------------------
# class BotsListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
class BotListView(LoginRequiredMixin, generic.ListView):
    # permission_required = 'bots.view_Bots'
    model = Bot
    # paginate_by = 10
    template_name = "bots/bot_list.html"
    login_url = '/login/'
    # queryset = Bots.objects.all()

    def get_context_data(self, **kwargs):
        # log_user(self.request, sys._getframe(  ).f_code.co_name, "BotsListView")
        # filtre form kaydı varsa burada okunacak
        if self.request.method == 'GET':
            query = self.request.GET
            print("BotListView- request.GET= ", len(query), query)
            pklfile = f'temp/{self.request.user}/bot.pkl'
            if len(query) > 0:
                # eğer ExcelResponse çağrıldıysa, pkl kaydetme!
                if self.request.GET.get('Filtre') == 'Export':
                    pass
                else:
                    print(f"{pklfile} kaydediliyor")
                    with open(pklfile, 'wb') as f:
                        pickle.dump(query, f)
            else:
                if os.path.isfile(pklfile):
                    print(f"{pklfile} okunuyor")
                    if os.path.isfile(pklfile):
                        with open(pklfile, 'rb') as f:
                            query = pickle.load(f)
                        # print("query= ", query)
                        if not self.request.GET._mutable:
                            self.request.GET._mutable = True
                            self.request.GET = query
                            self.request.GET._mutable = False
        else:
            pass

        bots = Bot.objects.all()
        form = BotFilterForm(self.request.GET or None)
        # print(form)
        # context = gen_sorgula(self.request, form, kriptos)
        bots, form = gen_sorgula(self.request, form, bots)
        # print("bots= ", bots)
        context = super(BotListView, self).get_context_data(**kwargs)
        context['bot_list'] = bots
        context['toplam'] = len(bots)
        context['form'] = form
        return context    

class BotDetailView(LoginRequiredMixin, generic.DetailView):
    model = Bot
    form_class = BotForm
    template_name = "bots/bot_detail.html"
    success_url = "/bots/list"
    login_url = '/login/'

class BotCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = BotForm
    template_name = 'bots/bot_form.html'
    login_url = '/login/'
    success_url = "/bots/list"


class BotUpdateView(LoginRequiredMixin, generic.UpdateView):
    # permission_required = 'bots.change_Bots'
    model = Bot
    form_class = BotForm
    template_name = 'bots/bot_update.html'
    # fields = "__all__"
    login_url = '/login/'
    # success_url = "/bots/list"
    success_url = "bot_update"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/bots/'+str(self.object.pk)+"/update")

class BotDeleteView(LoginRequiredMixin, generic.DeleteView):
    # permission_required = 'bots.delete_Bots'
    model = Bot
    template_name = 'bots/bot_delete.html'
    login_url = '/login/'
    success_url = '/bots/list'

def Bot_clean(request):
    if request.user:
        f='bot'
        pklfile = f'temp/{request.user}/{f}.pkl'
        if os.path.isfile(pklfile):
            os.remove(pklfile)        

    return redirect('bot_list')

def bot_clean(request):
    if request.user:
        f='bot'
        pklfile = f'temp/{request.user}/{f}.pkl'
        if os.path.isfile(pklfile):
            os.remove(pklfile)        

    return redirect('bot_list')

def link_clicked(request,pk):
    botid = pk
    print(f"id= {pk}")
    bot = Bot.objects.get(pk=pk)
    if bot.link:
        bot.counter += 1
        bot.save()
        return redirect(bot.link)
    else:
        return redirect('home_view')