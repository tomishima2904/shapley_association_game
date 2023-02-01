from django.db import models
from accounts.models import CustomUser

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Words(models.Model):
    qid = models.AutoField(primary_key=True, help_text="質問のID")
    answer = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=3, blank=True, null=True)
    stimulus_1 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_2 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_3 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_4 = models.CharField(max_length=20, blank=True, null=True)
    stimulus_5 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'words'


class UserAnswers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    time_ms = models.IntegerField(null=True, help_text="解答にかかった時間 (ms)")
    session_id = models.CharField(max_length=14, help_text="同ユーザーの異なる回のゲームを区別するためのID", null=False)
    qid = models.IntegerField(blank=True, null=True, help_text="質問のID", default=0)
    user_answer = models.CharField(max_length=20, blank=True, null=True, help_text="ユーザーの回答")
    q_order = models.CharField(max_length=9, help_text="ユーザーに提示した刺激語の順", null=True)
    u_order = models.CharField(max_length=9, help_text="ユーザーが役に立ったと思う刺激語の順", null=True)
