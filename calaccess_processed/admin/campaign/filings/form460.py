#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom administration panels for campaign models.
"""
from __future__ import unicode_literals
from django.contrib import admin
from calaccess_processed import models
from calaccess_raw.admin.base import BaseAdmin


@admin.register(models.Form460Filing)
class Form460FilingAdmin(BaseAdmin):
    """
    Custom admin for the Form460Filing model.
    """
    list_display = (
        'filing_id',
        'amendment_count',
        'filer_id',
        'filer_lastname',
        'filer_firstname',
        'date_filed',
        'election_date',
        'total_contributions',
        'total_expenditures_made',
        'ending_cash_balance',
    )


@admin.register(models.Form460FilingVersion)
class Form460FilingVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460FilingVersion model.
    """
    list_display = (
        'filing',
        'amend_id',
        'filer_id',
        'filer_lastname',
        'filer_firstname',
        'date_filed',
        'election_date',
        'total_contributions',
        'total_expenditures_made',
        'ending_cash_balance',
    )


@admin.register(models.Form460ScheduleAItem)
class Form460ScheduleAItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleAItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'date_received',
        'amount',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )


@admin.register(models.Form460ScheduleAItemVersion)
class Form460ScheduleAItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleAItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'date_received',
        'amount',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )


@admin.register(models.Form460ScheduleCItem)
class Form460ScheduleCItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleCItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'date_received',
        'fair_market_value',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )


@admin.register(models.Form460ScheduleCItemVersion)
class Form460ScheduleCItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleCItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'date_received',
        'fair_market_value',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )


@admin.register(models.Form460ScheduleDItem)
class Form460ScheduleDItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleDItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'support_oppose_code',
        'ballot_measure_name',
        'candidate_lastname',
        'amount',
        'cumulative_election_amount',
        'cumulative_ytd_amount',
        'transaction_id',
    )


@admin.register(models.Form460ScheduleDItemVersion)
class Form460ScheduleDItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleDItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'support_oppose_code',
        'ballot_measure_name',
        'candidate_lastname',
        'amount',
        'cumulative_election_amount',
        'cumulative_ytd_amount',
        'transaction_id',
    )


@admin.register(models.Form460ScheduleEItem)
class Form460ScheduleEItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleEItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
    )


@admin.register(models.Form460ScheduleEItemVersion)
class Form460ScheduleEItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleEItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
    )


@admin.register(models.Form460ScheduleESubItem)
class Form460ScheduleESubItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleESubItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
        'parent_transaction_id',
        'memo_reference_number',
    )


@admin.register(models.Form460ScheduleESubItemVersion)
class Form460ScheduleESubItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleESubItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
        'parent_transaction_id',
        'memo_reference_number',
    )


@admin.register(models.Form460ScheduleGItem)
class Form460ScheduleGItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleGItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'agent_lastname',
        'agent_firstname',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
        'parent_transaction_id',
        'parent_schedule',
        'memo_reference_number',
    )


@admin.register(models.Form460ScheduleGItemVersion)
class Form460ScheduleGItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleGItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'agent_lastname',
        'agent_firstname',
        'expense_date',
        'payee_code',
        'payee_lastname',
        'payee_firstname',
        'amount',
        'cumulative_ytd_amount',
        'transaction_id',
        'parent_transaction_id',
        'parent_schedule',
        'memo_reference_number',
    )


@admin.register(models.Form460ScheduleIItem)
class Form460ScheduleIItemAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleIItem model.
    """
    list_display = (
        'filing',
        'line_item',
        'date_received',
        'amount',
        'receipt_description',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )


@admin.register(models.Form460ScheduleIItemVersion)
class Form460ScheduleIItemVersionAdmin(BaseAdmin):
    """
    Custom admin for the Form460ScheduleIItemVersion model.
    """
    list_display = (
        'filing_version',
        'line_item',
        'date_received',
        'amount',
        'receipt_description',
        'transaction_id',
        'contributor_code',
        'contributor_lastname',
        'contributor_firstname',
    )
