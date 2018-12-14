#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print ("Pozdravljeni v aplikaciji Loto, ki generira naključna števila.\n")
how_many = raw_input("Koliko naključnih števil bi želeli imeti?")



while True:
    sort = raw_input("\nBi želel urediti števila od najmanšega do največjega (da/ne)?")
    if sort.lower() == "da":
        print sorted(random.sample(range(1, 39), int(how_many)))
        break
    elif sort.lower() == "ne":
        print random.sample(range(1, 39), int(how_many))
        break
    else:
        print "\nNapaka, Prosim vnesite da ali ne!"
