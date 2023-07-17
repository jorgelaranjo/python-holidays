#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from holidays.constants import BANK
from holidays.countries.austria import Austria, AT, AUT
from tests.common import TestCase


class TestAustria(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(Austria, years=range(1900, 2050))

    def test_country_aliases(self):
        self.assertCountryAliases(Austria, AT, AUT)

    def test_new_years(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in range(1900, 2050)))

    def test_epiphany(self):
        self.assertHolidayName(
            "Heilige Drei Könige", (f"{year}-01-06" for year in range(1900, 2050))
        )

    def test_easter_monday(self):
        self.assertHolidayName(
            "Ostermontag",
            "1900-04-16",
            "1901-04-08",
            "1902-03-31",
            "1999-04-05",
            "2000-04-24",
            "2010-04-05",
            "2018-04-02",
            "2019-04-22",
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
        )

    def test_labour_day(self):
        self.assertHolidayName("Staatsfeiertag", (f"{year}-05-01" for year in range(1900, 2050)))

    def test_ascension_day(self):
        self.assertHolidayName(
            "Christi Himmelfahrt",
            "1900-05-24",
            "1901-05-16",
            "1902-05-08",
            "1999-05-13",
            "2000-06-01",
            "2010-05-13",
            "2018-05-10",
            "2019-05-30",
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
        )

    def test_whit_monday(self):
        self.assertHolidayName(
            "Pfingstmontag",
            "1900-06-04",
            "1901-05-27",
            "1902-05-19",
            "1999-05-24",
            "2000-06-12",
            "2010-05-24",
            "2018-05-21",
            "2019-06-10",
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
        )

    def test_corpus_christi(self):
        self.assertHolidayName(
            "Fronleichnam",
            "1900-06-14",
            "1901-06-06",
            "1902-05-29",
            "1999-06-03",
            "2000-06-22",
            "2010-06-03",
            "2018-05-31",
            "2019-06-20",
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
        )

    def test_assumption_day(self):
        self.assertHolidayName(
            "Mariä Himmelfahrt", (f"{year}-08-15" for year in range(1900, 2050))
        )

    def test_national_day(self):
        self.assertHolidayName(
            "Nationalfeiertag",
            (f"{year}-11-12" for year in range(1919, 1935)),
            (f"{year}-10-26" for year in range(1967, 2050)),
        )
        self.assertNoHoliday("1918-11-12", "1935-11-12", "1966-10-26")
        self.assertNoHolidayName("Nationalfeiertag", range(1900, 1919), range(1935, 1967))

    def test_all_saints_day(self):
        self.assertHolidayName("Allerheiligen", (f"{year}-11-01" for year in range(1900, 2050)))

    def test_immaculate_conception_day(self):
        self.assertHolidayName("Mariä Empfängnis", (f"{year}-12-08" for year in range(1900, 2050)))

    def test_christmas_day(self):
        self.assertHolidayName("Christtag", (f"{year}-12-25" for year in range(1900, 2050)))

    def test_st_stephens_day(self):
        self.assertHolidayName("Stefanitag", (f"{year}-12-26" for year in range(1900, 2050)))

    def test_2022(self):
        self.assertHolidays(
            Austria(years=2022),
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Staatsfeiertag"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-10-26", "Nationalfeiertag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-12-08", "Mariä Empfängnis"),
            ("2022-12-25", "Christtag"),
            ("2022-12-26", "Stefanitag"),
        )

    def test_bank_2022(self):
        self.assertHolidays(
            Austria(categories=(BANK,), years=2022),
            ("2022-04-15", "Karfreitag"),
            ("2022-12-24", "Heiliger Abend"),
            ("2022-12-31", "Silvester"),
        )

    def test_subdiv(self):
        at_holidays = Austria(subdiv=1)
        self.assertEqual("1", at_holidays.subdiv)

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Staatsfeiertag"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-10-26", "Nationalfeiertag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-12-08", "Mariä Empfängnis"),
            ("2022-12-25", "Christtag"),
            ("2022-12-26", "Stefanitag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
            ("2022-08-15", "Assumption Day"),
            ("2022-10-26", "National Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-12-08", "Immaculate Conception"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "St. Stephen's Day"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-10-26", "Національне свято"),
            ("2022-11-01", "День усіх святих"),
            ("2022-12-08", "Непорочне зачаття Діви Марії"),
            ("2022-12-25", "Різдво Христове"),
            ("2022-12-26", "День Святого Стефана"),
        )