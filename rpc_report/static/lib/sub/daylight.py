
import datetime
import pytz


def context_timestamp(timestamp, h_begin):
	timestamp = timestamp.replace(hour=h_begin)
	tz_name = 'US/Pacific'
	timestamp = pytz.utc.localize(timestamp, is_dst=False)  # UTC = no DST
	print("step 1", timestamp)
	context_tz = pytz.timezone(tz_name)
	timestamp = timestamp.astimezone(context_tz)
	
	print("step 2", timestamp)
	timestamp = timestamp.replace(hour=h_begin)
	return timestamp.astimezone(pytz.UTC)
        
def context_remy(timestamp, h_begin):
	context_tz = pytz.timezone('US/Pacific')
	# Found today date which is the beginning day of the planning
	timestamp = timestamp.replace(hour=h_begin)
	timestamp = context_tz.localize(timestamp)
	print("Remy step 2", timestamp)
	return timestamp.astimezone(pytz.UTC)
          
         

for day, h_begin, UTC_time in [("2018-10-04", 5, "2018-10-04 12:00"),  ("2018-11-04", 5, "2018-11-04 13:00") , ("2018-12-04", 5, "2018-12-04 13:00")]:
	print("=================")
	day = datetime.datetime.strptime(day, "%Y-%m-%d")
	print(day)
	print(context_remy(day, h_begin))
	print(context_timestamp(day, h_begin))
	print(UTC_time)

	
	
