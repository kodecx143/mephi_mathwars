from django import forms
from .models import Team, User, Coin

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_id', 'team_title', 'team_score']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'team', 'is_captain']

class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = ['coin_position', 'cost', 'is_available']