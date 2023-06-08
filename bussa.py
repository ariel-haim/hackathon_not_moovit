import datetime
import numpy as np


# needs to support the following functions:
# report: given a bus, stop id, scheduled_time (s_time) and an actual time (a_time)
# the function will add the given parameters into the database of the bus


# Converts time from a (hour, minute) format to an integer
# @pre: hours, minutes is a possible time (24-hour format) ie 0 <= hour <= 23, 0 <= minute <= 59
def conv_time(hours, minutes):
    return minutes + (hours * 60)


# Returns a list with all dates between the two dates.
# @pre: d2 is a later date than d1
def generate_date_list(d1, d2):
    date_list = []
    while d1 <= d2:
        date_list.insert(d1)
        d1 += datetime.timedelta(days=1)
    return date_list


class Bus:
    def __init__(self, line_number):
        self.line_number = line_number
        self.schedule = self.schedule_buffer()
        self.arrival_DB = {}
        # arrival_DB is a database for the arrival times of the line

    # Assuming access to a database, the function will return a dictionary for the given bus where
    # Values = conv_time(time of day), Keys = Ids of the stations that the bus is supposed to stop at.
    def schedule_buffer(self):
        return None

    # Adds the data to arrival_DB
    # @pre: Assume that station_id is a valid stop of the bus
    # @pre: a_time = (hours, minutes) is a possible time (24-hour format)
    def report(self, address_id, a_time, date=datetime.date.today()):
        # The delay is the actual time - the scheduled time
        delay_time = conv_time(a_time) - self.schedule[address_id]
        self.arrival_DB[(address_id, date)] = delay_time

    # Given two dates and a station id, returns the average delay of the bus
    # within these dates of the station
    # @pre: end_date is later than beginning date
    # @pre: station_id is a valid station id and the bus is supposed to stop there
    def calc_average_by_station(self, station_id, beginning_date, end_date):
        date_list = generate_date_list(beginning_date, end_date)
        sum_number = 0
        total = 0
        for day in date_list:
            if self.arrival_DB[station_id, day]:
                total += self.arrival_DB[station_id, day]
                sum_number += 1
        return 0 if sum_number == 0 else round(total/sum_number)

    # Given a date, calculates the average delay of the bus during that day
    def calc_average_by_day(self, day):
        tuple_list = self.arrival_DB.keys()
        total = 0
        sum_number = 0
        for entrance in tuple_list:
            if entrance[1] == day and self.arrival_DB[entrance]:
                total += self.arrival_DB[entrance]
                sum_number += 1
        return 0 if sum_number == 0 else round(total/sum_number)

    # Given two dates and a station id, returns the standard deviation of the bus' delay
    # within these dates for the station
    # @pre: end_date is later than beginning date
    # @pre: station_id is a valid station id and the bus is supposed to stop there
    def calc_standard_deviation_by_station(self, station_id, beginning_date, end_date):
        date_list = generate_date_list(beginning_date, end_date)
        delay_list = [self.arrival_DB[station_id, day] for day in date_list]
        return np.std(delay_list)

    # Given a date, calculates the standard deviation of the bus' delay during that day
    def calc_standard_deviation_by_day(self, day):
        tuple_list = self.arrival_DB.keys()
        delay_list = [self.arrival_DB[entrance] for entrance in tuple_list if entrance[1] == day]
        return np.std(delay_list)
