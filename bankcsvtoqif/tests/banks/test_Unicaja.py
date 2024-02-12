# -*- coding: utf-8 -*-


# BankCSVtoQif - Smart conversion of csv files from a bank to qif
# Copyright (C) 2015-2016  Nikolai Nowaczyk
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest
from datetime import datetime
from bankcsvtoqif.tests.banks import csvline_to_line

from bankcsvtoqif.banks.Unicaja import Unicaja


class TestUnicaja(unittest.TestCase):

    def setUp(self):
        self.csv = """05/02/2024,05/02/2024,STARBUCKS COMERCIO  02 02 2024,-3.80,EUR,"6,787.87",EUR,1960,0048,,,"""

    def test_can_instantiate(self):
        account_config = Unicaja()
        self.assertEqual(type(account_config), Unicaja)

    def test_getters(self):
        account_config = Unicaja()
        line = csvline_to_line(self.csv, account_config)
        date = datetime(2024, 2, 5)
        description = "STARBUCKS COMERCIO 02 02 2024"
        category = ""
        debit = 3.80
        credit = 0
        self.assertEqual(account_config.get_date(line), date)
        self.assertEqual(account_config.get_description(line), description)
        self.assertEqual(account_config.get_debit(line), debit)
        self.assertEqual(account_config.get_credit(line), credit)
