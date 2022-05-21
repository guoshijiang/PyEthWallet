from django.contrib import admin

from wallet.models import (
    Asset,
    Wallet,
    Tx,
)

@admin.register(Asset)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "chain_name", "unit")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "name")


@admin.register(Wallet)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "chain_name")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "address")


@admin.register(Tx)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ("id", "tx_hash", "amount")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "tx_hash")
