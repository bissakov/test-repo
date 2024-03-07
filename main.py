import os
from datetime import datetime

with open('test.txt', 'w') as f:
	f.write(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))