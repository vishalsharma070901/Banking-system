# Generated by Django 4.0.6 on 2023-06-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_transaction', models.DecimalField(decimal_places=2, max_digits=12)),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Deposit'), (2, 'Withdrawal'), (3, 'Interest'), (4, 'Transfer')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='accounts.userbankaccount')),
                ('transfer_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfer_to', to='accounts.userbankaccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]