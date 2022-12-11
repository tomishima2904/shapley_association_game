# Generated by Django 4.1.3 on 2022-12-11 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(help_text='日付と時刻')),
                ('session_id', models.CharField(help_text='同ユーザーの異なる回のゲームを区別するためのID', max_length=14)),
                ('qid', models.IntegerField(blank=True, default=0, help_text='質問のID', null=True)),
                ('user_answer', models.CharField(blank=True, help_text='ユーザーの回答', max_length=20, null=True)),
                ('q_order', models.CharField(help_text='ユーザーに提示した刺激語の順', max_length=9, null=True)),
                ('u_order', models.CharField(help_text='ユーザーが役に立ったと思う刺激語の順', max_length=9, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
