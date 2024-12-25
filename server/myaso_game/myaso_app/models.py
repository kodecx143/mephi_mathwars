from django.db import models


class Team(models.Model):
    team_id = models.IntegerField(default=0) 
    team_title = models.CharField(max_length=255, unique=True,default='') 
    team_score = models.IntegerField(default=0) 
    def __str__(self):
        return self.team_title

class User(models.Model):
    user_id = models.IntegerField(default=0)   
    user_name = models.CharField(max_length=150,default='')  
    team = models.ForeignKey(Team, on_delete=models.CASCADE)  
    is_captain = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.user_name} (Captain: {self.is_captain})"

class Coin(models.Model):
    coin_position = models.IntegerField(default=0)
    cost = models.IntegerField(default=2)  
    is_available = models.BooleanField(default=True)  

    def __str__(self):
        return f"Coin at {self.coin_position}, Cost: {self.cost}, Available: {self.is_available}"

class Task(models.Model):
    text =models.CharField(max_length=1000,default='')
    turns=models.IntegerField(default=2)
    answer=models.CharField(max_length=100,default='')
    task_id = models.IntegerField(default=0)  
    def __str__(self):
        return f"Answer {self.answer}"