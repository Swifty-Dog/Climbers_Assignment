import sqlite3

from climber import Climber
from expedition import Expedition
from mountain import Mountain

import unittest
class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.climber = Climber(None, None, None, None, "17-06-2002")
        self.mountain = Mountain(None,None,None,None,4500,500, None,)
        self.expedition = Expedition(1, None, 4, None, "2002-17-06", None, "30H30", None,)
    # Test to check if the age of a climber is correct based on the date_of_birth
    def test_age_of_climber(self):
        age = self.climber.get_age()
        self.assertEqual(age,20)

    # Test to check if the amount of expeditions for a specific climber is returned correctly
    def test_amount_of_expeditions_of_climber(self):
        pass

    # Test to check the difference in height and prommence of a mountain
    def test_height_difference_mountain(self):
        difference = self.mountain.height_difference()
        self.assertEqual(difference, 4000)

        # Test to check if the amount of expeditions for a specific mountain is returned correctly
    def test_amount_of_expeditions_of_mountain(self):
        pass

    # Test to check if the returned date matches the specified format for that expedition date
    def test_expedition_date_conversion(self):
        convert_date = self.expedition.convert_date("1")
        self.assertEqual(convert_date,"06-17-2002")

#Test to check if the duration is converted from 1H19 to the specified format
    def test_expedition_duration_conversion(self):
        convert = self.expedition.convert_duration("3")
        self.assertEqual(convert, 1830)

    def test_add_climber_to_expedition(self):
        add_climber = self.expedition.add_climber("44")

        #werkt maar checkt niet goed
    # Test to check the amount of climbers on a specified expedition
    def test_amount_of_climbers_on_expedition(self):
        expedition_id_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT expedition_id FROM expedition_climbers"
        c.execute(query)
        result = c.fetchall()
        for i in result:
            i = str(i)
            i = i.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            i = int(i)
            expedition_id_list.append(i)
        expedition_id_list.sort()
        counts = dict()
        for i in expedition_id_list:
            counts[i]= counts.get(i, 0) + 1
        max_expedition = max(counts, key=lambda x:counts[x])
        print(max_expedition)
    # Test to validate if the given mountain of a specified expedition is correct
    def test_mountain_on_expedition(self):
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT id FROM expeditions"
        c.execute(query)
        result = c.fetchall()
        for i in result:
            i = str(i)
            i = i.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            i = int(i)
        print(result)