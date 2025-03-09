# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 07:36:44 2025

@author: Stefan Pauliuk
"""

# from https://github.com/IAMconsortium/nomenclature/blob/main/nomenclature/countries.py

import os
import logging

import pycountry

logger = logging.getLogger(__name__)

# `nomenclature` uses pycountry to (optionally) add all countries and ISO3 codes
# For readability and in line with conventions of the IAMC community,
# several "standard" country names are shortened
# Please keep this list in sync with `templates/model-registration-template.xlsx`
PYCOUNTRY_NAME_OVERRIDE = {
    "Bolivia, Plurinational State of": "Bolivia",
    "Holy See (Vatican City State)": "Vatican",
    "Micronesia, Federated States of": "Micronesia",
    "Congo, The Democratic Republic of the": "Democratic Republic of the Congo",
    "Iran, Islamic Republic of": "Iran",
    "Korea, Republic of": "South Korea",
    "Korea, Democratic People's Republic of": "North Korea",
    "Lao People's Democratic Republic": "Laos",
    "Syrian Arab Republic": "Syria",
    "Moldova, Republic of": "Moldova",
    "Tanzania, United Republic of": "Tanzania",
    "Venezuela, Bolivarian Republic of": "Venezuela",
    "Palestine, State of": "Palestine",
    "Taiwan, Province of China": "Taiwan",
    "Türkiye": "Turkey",  # revert change in pycountry on Sep 29, 2023
    "Virgin Islands, British": "British Virgin Islands",
    "Virgin Islands, U.S.": "United States Virgin Islands",
}
PYCOUNTRY_NAME_ADD = [
    dict(
        name="Kosovo",
        alpha_3="KOS",  # see https://olympics.com/ioc/kosovo
        alpha_2="XK",  # see https://en.wikipedia.org/wiki/XK_(user_assigned_code)
        note="Kosovo is recognized under UNSC resolution 1244, "
        "using preliminary alpha_3 and alpha_2 codes (ISO-3166-1 not assigned)",
    ),
]

# the European Commission uses alternative ISO2 codes
ALTERNATIVE_ALPHA2_CODES = {
    "EL": "GR",
    "UK": "GB",
}


class Countries(pycountry.ExistingCountries):
    """List of countries based on simplified ISO 3166 database

    This list follows the :class:`nomenclature.countries` module based on
    country names using ISO 3166-1, but it simplifies several country names
    for readability and in line with conventions of the IAMC community.
    """

    def __init__(self):
        super().__init__(os.path.join(pycountry.DATABASE_DIR, "iso3166-1.json"))

        # modify country names
        for iso_name, nc_name in PYCOUNTRY_NAME_OVERRIDE.items():
            obj = self.get(name=iso_name)
            obj.name = nc_name
            obj.iso_name = iso_name
            obj.note = "Name changed from ISO 3166 in line with community standards"
            self.indices["name"][nc_name.lower()] = obj

        # add countries that are not officially recognized
        # but relevant for IAM community
        for entry in PYCOUNTRY_NAME_ADD:
            obj = self.data_class(**entry)
            self.objects.append(obj)

            for key, value in entry.items():
                # Lookups and searches are case insensitive. Normalize here.
                value = value.lower()
                if key in self.no_index:
                    continue
                index = self.indices.setdefault(key, {})
                if value in index:
                    raise ValueError(f"Index conflict for country {key}: {value}")
                index[value] = obj

    def get(self, **kwargs):
        """Get a specific country by attribute

        Parameters
        ----------
        name : str
            Country name
        alpha_3 : str
            Alpha-3 code (ISO3)
        alpha_2 : str
            Alpha-2 code (ISO2)

        Returns
        -------
        :class:`pycountry.Country`

        """
        country = super().get(**kwargs)

        # special handling for alpha-2 codes used by the European Commission
        if country is None and "alpha_2" in kwargs:
            country = super().get(alpha_2=ALTERNATIVE_ALPHA2_CODES[kwargs["alpha_2"]])
            if country is not None:
                logger.info(
                    f"You are using non-standard alpha-2 codes for {country.name}."
                )

        return country

    @property
    def names(self):
        return [country.name for country in self.objects]


# Initialize `countries` for direct access via API and in codelist module
countries = Countries()