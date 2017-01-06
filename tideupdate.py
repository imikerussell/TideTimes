import time
from tidestore import *

if hl == "3":
	# 3 tide times today
	timenow = (time.strftime("%H:%M"))
	FMT = '%H:%M'
	if hl0 == "High":
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,05):
			if datetime.strptime(tt4, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt3
				nextlowm = th3
			else:
				nextlowtide = tt5
				nextlowm = th5
			nexthightide = tt4
			nexthighm = th4
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
				nextlowm = tt3
	else:
		from datetime import datetime, time
		now = datetime.now()
		now_time = now.time()
		if now_time >= time(0,00) and now_time <= time(6,05):
			if datetime.strptime(tt4, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt3
				nexthighm = th3
			else:
				nexthightide = tt5
				nexthighm = th5
			nextlowtide = tt4
			nextlowm = th4
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
		if now_time >= time(0,00) and now_time <= time(6,00):
			if datetime.strptime(tt4, FMT) > datetime.strptime(timenow, FMT):
				nexthightide = tt4
				nexthighm = th4
			else:
				nexthightide = tt6
				nexthighm = th6
			nextlowtide = tt5
			nextlowm = th5
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
		if now_time >= time(0,00) and now_time <= time(6,00):
			if datetime.strptime(tt4, FMT) > datetime.strptime(timenow, FMT):
				nextlowtide = tt4
				nextlowm = th4
			else:
				nextlowtide = tt6
				nextlowm = th6
			nexthightide = tt5
			nexthighm = th5
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
	print "ERROR: No tide data present."

print "Next High Tide: %s" % nexthightide
print "Next High Tide Height: %s" % nexthighm
print "Next Low Tide: %s" % nextlowtide
print "Next Low Tide Height: %s" % nextlowm
