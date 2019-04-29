from collections import namedtuple
TimeInterval=namedtuple('TimeInterval',['begin','end'])

interval=TimeInterval(datetime(2018,1,1,),dattime(2018,1,2))
interval.begin


from collections import namedtuple
class TimeInterval (namedtuple('TimeInterval',['begin','end'])):
	def get_length(self):
		return self.end-self.begin

interval=TimeInterval(datetime(2018,1,1),datetime(2018,1,2))
interval.get_length()		