from datetime import datetime

d, m = input().split()
date_str = f'2009-{m}-{d}'
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj.strftime('%A'))
