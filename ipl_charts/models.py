# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Matches(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    season = models.IntegerField(max_length=100)
    city = models.CharField(blank=True, null=True, max_length=50)
    date = models.DateField(blank=True, null=True)
    team1 = models.CharField(blank=True, null=True, max_length=100)
    team2 = models.CharField(blank=True, null=True, max_length=100)
    toss_winner = models.CharField(blank=True, null=True, max_length=100)
    toss_decision = models.CharField(blank=True, null=True, max_length=20)
    result = models.CharField(blank=True, null=True, max_length=50)
    dl_applied = models.IntegerField(blank=True, null=True)
    winner = models.CharField(blank=True, null=True, max_length=100)
    win_by_runs = models.IntegerField(blank=True, null=True)
    win_by_wickets = models.IntegerField(blank=True, null=True)
    player_of_match = models.CharField(blank=True, null=True, max_length=150)
    venue = models.CharField(blank=True, null=True, max_length=150)
    umpire1 = models.CharField(blank=True, null=True, max_length=150)
    umpire2 = models.CharField(blank=True, null=True, max_length=150)
    umpire3 = models.CharField(blank=True, null=True, max_length=150)

    def __str__(self):
        return(f'{self.season}')

    class Meta:
        managed = False
        db_table = 'Matches'



class Deliveries(models.Model):
    match_id = models.ForeignKey('Matches', on_delete=models.CASCADE)
    inning = models.IntegerField(blank=True, null=True)
    batting_team = models.CharField(blank=True, null=True, max_length=150)
    bowling_team = models.CharField(blank=True, null=True, max_length=150)
    over = models.IntegerField(blank=True, null=True)
    ball = models.IntegerField(blank=True, null=True)
    batsman = models.CharField(blank=True, null=True, max_length=150)
    non_striker = models.CharField(blank=True, null=True, max_length=150)
    bowler = models.CharField(blank=True, null=True, max_length=150)
    is_super_over = models.IntegerField(blank=True, null=True)
    wide_runs = models.IntegerField(blank=True, null=True)
    bye_runs = models.IntegerField(blank=True, null=True)
    legbye_runs = models.IntegerField(blank=True, null=True)
    noball_runs = models.IntegerField(blank=True, null=True)
    penalty_runs = models.IntegerField(blank=True, null=True)
    batsman_runs = models.IntegerField(blank=True, null=True)
    extra_runs = models.IntegerField(blank=True, null=True)
    total_runs = models.IntegerField(blank=True, null=True)
    player_dismissed = models.CharField(blank=True, null=True, max_length=150)
    dismissal_kind = models.CharField(blank=True, null=True, max_length=150)
    fielder = models.CharField(blank=True, null=True, max_length=150)

    def __str__(self):
        return(f'{self.match_id_id}')

    class Meta:
        managed = False
        db_table = 'Deliveries'
