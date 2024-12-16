from django.shortcuts import render
from .models import Team, User, Coin

def team_list(request):
    
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def user_list(request):
    
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def coin_list(request):
    
    coins = Coin.objects.all()
    return render(request, 'coin_list.html', {'coins': coins})













"""
def edit_team(request, team_id=None):
    if team_id:
        team = get_object_or_404(Team, pk=team_id)
    else:
        team = None

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)

    return render(request, 'edit_team.html', {'form': form})

def edit_user(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form})

def edit_coin(request, coin_id=None):
    if coin_id:
        coin = get_object_or_404(Coin, pk=coin_id)
    else:
        coin = None

    if request.method == 'POST':
        form = CoinForm(request.POST, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('coin_list')
    else:
        form = CoinForm(instance=coin)

    return render(request, 'edit_coin.html', {'form': form})



"""




"""

def index(request):
    teams = Team.objects.all()  
    return render(request, 'index.html', {'teams': teams})
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('index')  
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})
def update_team(request):
    team, created = Team.objects.get_or_create(id=1)  
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = TeamForm(instance=team)
    return render(request, 'update_team.html', {'form': form})"""