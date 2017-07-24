#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proxy models for augmenting our source data tables with methods useful for processing.
"""
from __future__ import unicode_literals
import re
from django.db import models
from .divisions import OCDDivisionProxy
from opencivicdata.core.models import Post
from .organizations import OCDOrganizationProxy
from ..calaccess_raw.filertofilertype import RawFilerToFilerTypeCdProxy


class OCDPostManager(models.Manager):
    """
    Custom helpers for the OCD Post model.
    """
    def parse_office_name(self, office_name):
        """
        Parse string containg the name for an office.

        Expected format is "{TYPE NAME}[{DISTRICT NUMBER}]".

        Return a dict with two keys: type and district.
        """
        office_pattern = r'^(?P<type>[A-Z ]+)(?P<district>\d{2})?$'
        try:
            parsed = re.match(office_pattern, office_name.upper()).groupdict()
        except AttributeError:
            parsed = {'type': None, 'district': None}
        else:
            parsed['type'] = parsed['type'].strip()
            try:
                parsed['district'] = int(parsed['district'])
            except TypeError:
                pass

        return parsed

    def get_by_name(self, office_name):
        """
        Get a Post object with an office string.
        """
        parsed_office = self.parse_office_name(office_name)

        # prepare to get or create post
        label = office_name.title().replace('Of', 'of')

        if parsed_office['type'] == 'STATE SENATE':
            division = OCDDivisionProxy.senate.get(subid2=parsed_office['district'])
            organization = OCDOrganizationProxy.objects.senate()
            role = 'Senator'
        elif parsed_office['type'] == 'ASSEMBLY':
            division = OCDDivisionProxy.assembly.get(subid2=parsed_office['district'])
            organization = OCDOrganizationProxy.objects.assembly()
            role = 'Assembly Member'
        else:
            # If not Senate or Assembly, assume this is a state office
            division = OCDDivisionProxy.objects.california()
            if parsed_office['type'] == 'MEMBER BOARD OF EQUALIZATION':
                organization = OCDOrganizationProxy.objects.board_of_equalization()
                role = 'Board Member'
            elif parsed_office['type'] == 'SECRETARY OF STATE':
                organization = OCDOrganizationProxy.objects.secretary_of_state()
                role = label
            else:
                organization = OCDOrganizationProxy.objects.executive_branch()
                role = label

        # Pass it out
        return self.get_queryset().get(
            label=label,
            role=role,
            division=division,
            organization=organization
        )

    def get_or_create_by_name(self, office_name):
        """
        Get or create a Post object with an office_name string.

        Returns a tuple (Post object, created), where created is a boolean
        specifying whether a Post was created.
        """
        parsed_office = self.parse_office_name(office_name)

        # prepare to get or create post
        label = office_name.title().replace('Of', 'of')

        if parsed_office['type'] == 'STATE SENATE':
            division = OCDDivisionProxy.senate.get(subid2=parsed_office['district'])
            organization = OCDOrganizationProxy.objects.senate()
            role = 'Senator'
        elif parsed_office['type'] == 'ASSEMBLY':
            division = OCDDivisionProxy.assembly.get(subid2=parsed_office['district'])
            organization = OCDOrganizationProxy.objects.assembly()
            role = 'Assembly Member'
        else:
            # If not Senate or Assembly, assume this is a state office
            division = OCDDivisionProxy.objects.california()
            if parsed_office['type'] == 'MEMBER BOARD OF EQUALIZATION':
                organization = OCDOrganizationProxy.objects.board_of_equalization()
                role = 'Board Member'
            elif parsed_office['type'] == 'SECRETARY OF STATE':
                organization = OCDOrganizationProxy.objects.secretary_of_state()
                role = label
            else:
                organization = OCDOrganizationProxy.objects.executive_branch()
                role = label

        # Pass it out
        return self.get_queryset().get_or_create(
            label=label,
            role=role,
            division=division,
            organization=organization
        )

    def get_by_form501(self, form501):
        """
        Get a Post using data extracted from Form501Filing.

        Return Post object or None if not found.
        """
        # Try to get it using office_name
        try:
            return self.get_by_name(form501.office_name)
        except (self.model.DoesNotExist, OCDDivisionProxy.DoesNotExist):
            pass

        # Try extracting office and district from FilerToFilerTypeCd
        filer_id_office_name = RawFilerToFilerTypeCdProxy.objects.get_office_by_filer_id_and_date(
            form501.filer_id,
            form501.ocd_election.date
        )

        # If you can't find that, just quit
        if not filer_id_office_name:
            return None

        # If you can, try to get that
        try:
            return self.get_by_name(filer_id_office_name)
        except (self.model.DoesNotExist, OCDDivisionProxy.DoesNotExist):
            return None


class OCDPostProxy(Post):
    """
    A proxy on the OCD Post model with helper methods..
    """
    objects = OCDPostManager()

    class Meta:
        """
        Make this a proxy model.
        """
        proxy = True