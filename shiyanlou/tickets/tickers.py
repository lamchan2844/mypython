#! /usr/bin/env python
#-*-encoding:utf-8-*-#
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets beijing shanghai 2016-08-25
"""
import requests
from docopt import docopt
from prettytable import PrettyTable
from stations import stations
class TrainCollection(object):
	header = 'train station time duration first second softsleep hardsleep hardseat'.split()
	def __init__(self,rows):
		self.rows = rows
	def _get_duration(self,row):
		'''
		get the time of train
		'''
		duration = row.get('lishi').replace(':','h')+'m'
		if duration.startswith('00'):
			return duration[4:]
		if duration.startswith('0'):
			return duration[1:]
		return duration
	@property
	def trains(self):
		for row in self.rows:
			train = [
				#train number
				row['station_train_code'],
				#start_station,arrival_station
				'\n'.join([colored('green',row['from_station_name']),colored('red',row['to_station_name'])]),
				#start_time,arrival_time
				'\n'.join([colored('green',row['start_time']),colored('red',row['arrive_time'])]),
				#duration_time
				self._get_duration(row),
				#first-class seats
				row['zy_num'],
				#second-class seats
				row['ze_num'],
				#soft-sleeper
				row['rw_num'],
				#hard-sleeper
				row['yw_num'],
				#hard-seater
				row['yz_num']
			]
			yield train
	def pretty_print(self):
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains:
			pt.add_row(train)
		print(pt)
def colored(color,text):
	table ={
		'red':'\033[91m',
		'green':'\033[92m',
		'nc':'\033[0m'
	}
	cv = table.get(color)
	nc = table.get('nc')
	return ''.join([cv, text, nc])
	
def cli():

	arguments = docopt(__doc__)
	from_station = stations.get(arguments['<from>'])
	to_station = stations.get(arguments['<to>'])
	date = arguments['<date>']
	url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date,from_station,to_station)
	#print url
	r = requests.get(url,verify=False)
	#print r.json()
	rows = r.json()['data']['datas']
	#print rows
	trains = TrainCollection(rows)
	trains.pretty_print()
if __name__=='__main__':

	cli()
