# Generated by Django 2.2.7 on 2022-05-21 14:13

import common.models
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('chain_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='链名称')),
                ('pubkey', models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='公钥')),
                ('privkey', models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='私钥')),
                ('address', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='地址')),
                ('balance', common.models.DecField(decimal_places=30, default=Decimal('0E-18'), max_digits=65, verbose_name='钱包余额')),
                ('in_amount', common.models.DecField(decimal_places=30, default=Decimal('0E-18'), max_digits=65, verbose_name='钱包入账')),
                ('out_amount', common.models.DecField(decimal_places=30, default=Decimal('0E-18'), max_digits=65, verbose_name='钱包出账')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否是有效')),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_wallet_asset', to='common.Asset', verbose_name='资产')),
            ],
            options={
                'verbose_name': '地址表',
                'verbose_name_plural': '地址表',
            },
        ),
        migrations.CreateModel(
            name='Tx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('chain_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='链名称')),
                ('from_addr', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='转出地址')),
                ('to_addr', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='转入地址')),
                ('amount', common.models.DecField(decimal_places=30, default=Decimal('0E-18'), max_digits=65, verbose_name='转账金额')),
                ('tx_fee', common.models.DecField(decimal_places=30, default=Decimal('0E-18'), max_digits=65, verbose_name='转账手续费')),
                ('tx_hash', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='交易Hash')),
                ('comment', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='备注')),
                ('direction', models.CharField(choices=[('input', 'input'), ('output', 'output')], default='input', max_length=100, verbose_name='充值提现')),
                ('status', models.CharField(choices=[('success', 'success'), ('failure', 'failure')], default='success', max_length=100, verbose_name='状态')),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_record_asset', to='common.Asset', verbose_name='资产')),
            ],
            options={
                'verbose_name': '交易记录表',
                'verbose_name_plural': '交易记录表',
            },
        ),
    ]
