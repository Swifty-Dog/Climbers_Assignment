import sqlite3
from mountain import Mountain
from expedition import Expedition
from climber import Climber
from datetime import datetime
import csv
class Reporter:

    # How many climbers are there? -> int
    def total_amount_of_climbers(self) -> int:
        exp = Expedition(None, None, None, None, None, None, None, None,)
        climbers = exp.get_climbers()
        climber_list = []
        count = 0
        for climber in climbers:
            if climber not in climber_list:
                climber_list.append(climber)
                count+= 1
        return count
    # What is the highest mountain? -> Mountain
    def highest_mountain(self) -> Mountain:
        data_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT height FROM mountains"
        c.execute(query)
        results = c.fetchall()
        for result in results:
            result = str(result)
            result = result.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            data_list.append(result)
        data_list.sort()
        query = "SELECT * FROM mountains ORDER BY height DESC"
        c.execute(query)
        highest = c.fetchall()
        return highest[0]

    #What is the longest and shortest expedition? -> tuple[Expedition, Expedition]
    def longest_and_shortest_expedition(self) -> tuple[Expedition, Expedition]:
        duration_list =[]

        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT id FROM expeditions"
        c.execute(query)
        ids = c.fetchall()
        for id in ids:
            exp = Expedition(id, None, None, None, None, None, None, None)
            duration = exp.convert_duration("3")
            duration_list.append(duration)

        duration_list.sort()

        return (duration_list[0], duration_list[-1])

    # Which expeditons have the most climbers -> tuple[Expedition, ...]
    def expedition_with_most_climbers(self) -> tuple[Expedition, ...]:
        expedition_id_list = []
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT expedition_id FROM expedition_climbers"
        c.execute(query)
        results = c.fetchall()
        for item in results:
            item = str(item)
            item = item.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            item = int(item)
            expedition_id_list.append(item)
        expedition_id_list.sort()
        counts = dict()
        for i in expedition_id_list:
            counts[i]= counts.get(i, 0) + 1
        max_expedition = max(counts, key=lambda x:counts[x])
        print(f"The expedition with the most climber is: Expedition {max_expedition}.")

    # Which climbers have made the most expeditions -> tuple[Climber, ...]
    # Which climbers have made the most succesful expeditions -> tuple[Climber, ...]
    def climbers_with_most_expeditions(self, only_succesful: bool = False) -> tuple[Climber, ...]:
        pass
        #werkt niet met mijn table :O
    # Which mountain has the most expeditions -> Mountain
    def mountains_with_most_expeditions(self) -> tuple[Mountain, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT name FROM mountains"
        c.execute(query)
        results = c.fetchall()
        counts = dict()
        for item in results:
            item = str(item)
            item = item.replace(",", "").replace("(", "").replace(")", "").replace("'", "").replace("'", "")
            counts[item]= counts.get(item, 0) + 1
        max_name = max(counts, key=lambda  x:counts[x])
        return max_name
    # Which expedition was the first expedition? -> Expedition
    # Which expedition was the first successful expedition? -> Expedition
    def get_first_expedition(self, only_succesful: bool = False) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT * FROM expeditions ORDER BY date success"
        c.execute(query)
        date = c.fetchall()
        return date[0]

    # Which expedition is the latest? -> Expedition
    # Which succesful expedition is the latetst? -> Expedition
    def get_latest_expedition(self, only_succesful: bool = False) -> Expedition:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "SELECT * FROM expeditions  WHERE success = 1 ORDER BY date DESC "
        c.execute(query)
        date = c.fetchall()
        return date[0]

    # Which climbers have climbed mountain Z between period X and Y? -> tuple[Climber, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Climbers Mountain Z between X and Y.csv`
    # otherwise it should just return the value as tuple(Climber, ...)
    # CSV example:
    #   Id, first_name, last_name, nationality, date_of_birth
    def get_climbers_that_climbed_mountain_between(self) -> tuple[Climber, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        start = "1985-01-01"
        end = "1990-01-01"
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        query = "SELECT id FROM mountains WHERE name=?"
        val = "Gasherbrum IV",
        c.execute(query, val)
        mountain_id = c.fetchall()
        mountain_id_data = []
        for id in mountain_id:
            id = str(id)
            id = id.replace(",", "").replace("(", "").replace(")", "")
            id = int(id)
            mountain_id_data.append(id)
        query= "SELECT * FROM expeditions"
        c.execute(query)
        expeditions_results = c.fetchall()
        expeditions = []
        for exp in expeditions_results:
            exp = str(exp)
            exp = exp.replace(",", "").replace("(", "").replace(")", "")
            expeditions.append(exp)
        for id in mountain_id_data:
            id = id - 1
            date = expeditions_results[id][4]
            check_date = datetime.strptime(date, "%Y-%m-%d")
            if start_date <= check_date <= end_date:
                id = id + 1
                query = "SELECT * from expedition_climbers"
                c.execute(query)
                results = c.fetchall()
                #data with expedition and climber ids
                expeditions_climbers_list = []
                climber_id_list = []
                not_in_climber_list = []
                for result in results:
                    result = str(result)
                    result = result.replace("(", "").replace(")", "")
                    expeditions_climbers_list.append(result)
                for climber_exp_id in expeditions_climbers_list:
                    climber_id = int(climber_exp_id.split(",")[0])
                    expedition_id = int(climber_exp_id.split(",")[1])
                    if id == expedition_id:
                        climber_id_list.append(climber_id)
                    else:
                        not_in_climber_list.append(climber_id)

                #climbers_list has the climbers that went on the mountain
                query = "SELECT * from climbers"
                c.execute(query)
                climber_info = []
                climbers_result = c.fetchall()
                climber_who_did_not = []
                for line in climbers_result:
                    line = str(line)
                    line = line.replace("(", "").replace(")", "")
                    for climber_id in climber_id_list:
                        if climber_id == int(line.split(",")[0]):
                            climber_info.append(line)
                        else:
                            if line not in climber_who_did_not:
                                climber_who_did_not.append(line)
                filename = "Climbers Mountain Z between X and Y.csv"
                headers = ["id", "first_name", "last_name", "nationality", "date_of_birth"]
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    for line in climber_info:
                        row = line.split(",")
                        writer.writerow(row)

                for info in climber_who_did_not:
                    print(info)
    # Which mountains are located in country X? ->tuple[Mountain, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Mountains in country X.csv`
    # otherwise it should just return the value as tuple(Mountain, ...)
    # CSV example:
    #   Id, name, country, rank, height, prominence, range
    def get_mountains_in_country(self) -> tuple[Mountain, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        mountain_id =[]
        query = "SELECT mountain_id FROM expeditions WHERE start_location=?"
        val = "Pakistan",
        c.execute(query,val)
        results = c.fetchall()
        for result in results:
            result = str(result)
            result = result.replace(",", "").replace("(", "").replace(")", "")
            result = int(result)
            mountain_id.append(result)
        query = "SELECT * FROM mountains"
        c.execute(query)
        data = c.fetchall()
        mountain_data = []
        for line in data:
            line = str(line)
            line = line.replace(",", "").replace("(", "").replace(")", "")
            mountain_data.append(line)
        filename = "Mountains_in_country_X.csv"
        headers = ["id", "name", "country", "rank", "height", "prominence", "range"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for id in mountain_id:
                id = id - 1
                row = mountain_data[id].split(" ")
                writer.writerow(row)
        conn.close()

    # Which climbers are from country X? -> tuple[Climber, ...]
    # Based on given parameter `to_csv = True` should generate CSV file as  `Climbers in country X.csv`
    # otherwise it should just return the value as tuple(Climber, ...)
    # CSV example:
    #   Id, first_name, last_name, nationality, date_of_birth
    def get_climbers_from_country(self) -> tuple[Climber, ...]:
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        climbers_info = []
        query = "SELECT * FROM climbers WHERE nationality = ?"
        val = "Brazil",
        c.execute(query, val)
        results = c.fetchall()
        for result in results:
            result = str(result)
            result = result.replace("(", "").replace(")", "")
            climbers_info.append(result)
        filename = "Climbers_in_country_X.csv"
        headers = ["id", "first_name", "last_name", "nationality", "date_of_birth"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for climber in climbers_info:
                row = climber.split(",")
                writer.writerow(row)
        new_query = "SELECT * FROM climbers WHERE nationality != ?"
        c.execute(new_query, val)
        all_results = c.fetchall()
        for result in all_results:
            print(result)
report = Reporter()

def main():
    #1
    print(report.total_amount_of_climbers())
    # 2
    print(report.highest_mountain())
    # 3
    print(report.longest_and_shortest_expedition())
    # 4
    report.expedition_with_most_climbers()
    # 5
    report.climbers_with_most_expeditions()
    #6
    print(report.mountains_with_most_expeditions())
    #7
    print(report.get_first_expedition())
    #8
    print(report.get_first_expedition())
    #9
    print(report.get_first_expedition())
    #10
    print(report.get_latest_expedition())
    #11
    print(report.get_climbers_that_climbed_mountain_between())
    #12
    report.get_mountains_in_country()
    #13
    report.get_climbers_from_country()

if __name__=="__main__":
    main()
