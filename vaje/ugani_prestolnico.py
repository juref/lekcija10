#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

country_capital_dict = {
    "Slovenija": "Ljubljana",
    "Hrvaska": "Zagreb",
    "Avstria": "Dunaj",
    "Italija": "Rim"}

drzave = []
mesta = []

for k, v in country_capital_dict.iteritems():
    drzave.append(k)
    mesta.append(v)

nakljucna_izbira = randint(0, (len(country_capital_dict) - 1))

print drzave[nakljucna_izbira]
print mesta[nakljucna_izbira]

print country_capital_dict.items()
print country_capital_dict.keys()
print country_capital_dict.values()