# encoding=utf-8

from django.db import models
from common.models import (
    Asset,
    BaseModel,
    DecField,
)
TransWay = [(x, x) for x in ["input", "output"]]
WalletStatus = [(x, x) for x in ["success", "failure"]]
from common.helpers import dec, d0


class Wallet(BaseModel):
    asset = models.ForeignKey(
        Asset,
        related_name="user_wallet_asset",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="资产",
    )
    chain_name = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="链名称",
    )
    pubkey = models.CharField(
        max_length=512,
        default="",
        blank=True,
        null=True,
        verbose_name="公钥",
    )
    privkey = models.CharField(
        max_length=512,
        default="",
        blank=True,
        null=True,
        verbose_name="私钥",
    )
    address = models.CharField(
        max_length=128,
        default="",
        blank=True,
        null=True,
        verbose_name="地址",
    )
    balance = DecField(
        default=d0,
        verbose_name="钱包余额"
    )
    in_amount = DecField(
        default=d0,
        verbose_name="钱包入账"
    )
    out_amount = DecField(
        default=d0,
        verbose_name="钱包出账"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "地址表"
        verbose_name_plural = "地址表"

    def __str__(self):
        return self.address

    def as_dict(self):
        return {
            "address": self.address,
        }


class Tx(BaseModel):
    asset = models.ForeignKey(
        Asset,
        related_name="wallet_record_asset",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="资产",
    )
    chain_name = models.CharField(
        max_length=100,
        default="",
        blank=True,
        null=True,
        verbose_name="链名称",
    )
    from_addr = models.CharField(
        max_length=128,
        default="",
        blank=True,
        null=True,
        verbose_name="转出地址",
    )
    to_addr = models.CharField(
        max_length=128,
        default="",
        blank=True,
        null=True,
        verbose_name="转入地址",
    )
    amount = DecField(
        default=d0,
        verbose_name="转账金额"
    )
    tx_fee = DecField(
        default=d0,
        verbose_name="转账手续费"
    )
    tx_hash = models.CharField(
        max_length=128,
        default="",
        blank=True,
        null=True,
        verbose_name="交易Hash",
    )
    comment = models.CharField(
        max_length=128,
        default="",
        blank=True,
        null=True,
        verbose_name="备注",
    )
    direction = models.CharField(
        max_length=100,
        choices=TransWay,
        default="input",
        verbose_name="充值提现",
    )
    status = models.CharField(
        max_length=100,
        choices=WalletStatus,
        default="success",
        verbose_name="状态",
    )

    class Meta:
        verbose_name = "交易记录表"
        verbose_name_plural = "交易记录表"

    def __str__(self):
        return ""

    def as_dict(self):
        return {"tx_hash": self.tx_hash}


