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

from bankcsvtoqif.banks.Banktrack import Banktrack


class TestBanktrack(unittest.TestCase):

    def setUp(self):
        self.csvDebit = """07/03/2024,07/03/2024,"INSDE, S.L824290-450119263098",,"-3114,62",,,,"1334,49",EUR,No,Educación,Unicaja,Family CCM Ck."""
        self.csvCredit = """09/03/2024,09/03/2024,AMPARO COLASTRA MILLAS,,"10,0",,,,"1128,82",EUR,No,Familia y Amigos,Unicaja,Family CCM Ck."""

    def test_can_instantiate(self):
        account_config = Banktrack()
        self.assertEqual(type(account_config), Banktrack)

    def test_debit(self):
        account_config = Banktrack()
        line = csvline_to_line(self.csvDebit, account_config)
        date = datetime(2024, 3, 7)
        description = "INSDE, S.L824290-450119263098"
        category = "Educación"
        debit = 3114.62
        credit = 0
        source_account = "Family CCM Ck."
        self.assertEqual(account_config.get_date(line), date)
        self.assertEqual(account_config.get_description(line), description)
        self.assertEqual(account_config.get_category(line), category)
        self.assertEqual(account_config.get_debit(line), debit)
        self.assertEqual(account_config.get_credit(line), credit)
        self.assertEqual(account_config.get_source_account(line), source_account)

    def test_credit(self):
        account_config = Banktrack()
        line = csvline_to_line(self.csvCredit, account_config)
        date = datetime(2024, 3, 9)
        description = "AMPARO COLASTRA MILLAS"
        category = "Familia y Amigos"
        debit = 0
        credit = 10
        source_account = "Family CCM Ck."
        self.assertEqual(account_config.get_date(line), date)
        self.assertEqual(account_config.get_description(line), description)
        self.assertEqual(account_config.get_category(line), category)
        self.assertEqual(account_config.get_debit(line), debit)
        self.assertEqual(account_config.get_credit(line), credit)
        self.assertEqual(account_config.get_source_account(line), source_account)