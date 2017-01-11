import time
from tidestore import *
from tidestorex import *

if hl == "3":
	# 3 tide times today
	timenow = (time.strftime("%H:%M"))
	FMT = '%H:%M'
	if hl0 == "High":
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,2):
			if datetime.strptime(ttx4, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = ttx3
				nextlowm = thx3
			else:
				nextlowtide = ttx5
				nextlowm = thx5
			nexthightide = ttx4
			nexthighm = thx4
		else:
			from datetime import datetime, time
			if datetime.strptime(tt0, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt0
				nexthighm = th0
			elif datetime.strptime(tt2, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt2
				nexthighm = th2
			else:
				nexthightide = tt4
				nexthighm = th4
			if datetime.strptime(tt1, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt1
				nextlowm = th1
			else:
				nextlowtide = tt3
				nextlowm = th3
	else:
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,2):
			if datetime.strptime(ttx4, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = ttx3
				nexthighm = thx3
			else:
				nexthightide = ttx5
				nexthighm = thx5
			nextlowtide = ttx4
			nextlowm = thx4
		else:
			if datetime.strptime(tt0, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt0
				nextlowm = th0
			elif datetime.strptime(tt2, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt2
				nextlowm = th2
			else:
				nextlowtide = tt4
				nextlowm = th4
			if datetime.strptime(tt1, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt1
				nexthighm = th1
			else:
				nexthightide = tt3
				nexthighm = th3
elif hl == "4":
	# 4 tide times today
	timenow = (time.strftime("%H:%M"))
	FMT = '%H:%M'
	if hl0 == "High":
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,2):
			if datetime.strptime(ttx4, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = ttx4
				nexthighm = thx4
			else:
				nexthightide = ttx6
				nexthighm = thx6
			nextlowtide = ttx5
			nextlowm = thx5
		else:
			if datetime.strptime(tt0, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt0
				nexthighm = th0
			elif datetime.strptime(tt2, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt2
				nexthighm = th2
			else:
				nexthightide = tt4
				nexthighm = th4
			if datetime.strptime(tt1, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt1
				nextlowm = th1
			elif datetime.strptime(tt3, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt3
				nextlowm = th3
			else:
				nextlowtide = tt5
				nextlowm = th5
	else:
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,2):
			if datetime.strptime(ttx4, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = ttx4
				nextlowm = thx4
			else:
				nextlowtide = ttx6
				nextlowm = thx6
			nexthightide = ttx5
			nexthighm = thx5
		else:
			if datetime.strptime(tt0, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt0
				nextlowm = th0
			elif datetime.strptime(tt2, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt2
				nextlowm = th2
			else:
				nextlowtide = tt4
				nextlowm = th4
			if datetime.strptime(tt1, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt1
				nexthighm = th1
			elif datetime.strptime(tt3, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt3
				nexthighm = th3
			else:
				nexthightide = tt5
				nexthighm = th5
else:
	# Tide data not present or incorrect
	print ("ERROR: No tide data present.")

tidelocation = tl

print ("Tide Times Location: %s" % tidelocation)
print ("Next High Tide: %s" % nexthightide)
print ("Next High Tide Height: %s" % nexthighm)
print ("Next Low Tide: %s" % nextlowtide)
print ("Next Low Tide Height: %s" % nextlowm)
