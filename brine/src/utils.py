#!/usr/bin/env python

from datetime import datetime

def get_month(date):
	dt = datetime.strptime(date, "%d-%m-%Y")
	month_name = datetime.strptime(str(dt.month), "%m").strftime("%b")
	year = dt.year
	return f"{month_name} {str(year)}"