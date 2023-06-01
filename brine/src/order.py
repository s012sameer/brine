#!/usr/bin/env python

import csv
import logger
from vars import *
import utils

logger = logger.get_logger(__name__)

class Order_analyser:
	def __init__(self, csv_file):
		"""
		class to open the provided order file in csv format and store data as order_data
		usage - order_data =  Order_analyser("orders.csv")
		"""
		try:
			self.order_data = []
			with open(csv_file, mode ='r') as file:
				order_lines = csv.DictReader(file)
				for line in order_lines:
					self.order_data.append(line)
		except Exception as e:
			logger.error(f"Failed to Open {csv_file}: {e}")
			exit()

	def get_total_revenue(self, query_item):
		"""
		Calculate total revenue for orders based on query field provided e.g. - ORDER_DATE, PRODUCT_ID
		"""
		revenue_data = {}
		for order in self.order_data:
			try:
				# Grouping order dates per month
				if query_item == ORDER_DATE:
					revenue_data_key = utils.get_month(order[ORDER_DATE])
				else:
					revenue_data_key = order[query_item]
				if revenue_data_key in revenue_data:
					revenue_data[revenue_data_key] += (int(order[PRODUCT_PRICE]) * int(order[QUANTITY]))
				else:
					revenue_data[revenue_data_key] = int(order[PRODUCT_PRICE]) * int(order[QUANTITY])
			except Exception as e:
				logger.error(f"Can not get revenue from {order} - {e}")
		return revenue_data

	def get_revenue_per_month(self):
		return self.get_total_revenue(ORDER_DATE)

	def get_revenue_per_product(self):
		return self.get_total_revenue(PRODUCT_ID)

	def get_revenue_per_customer(self):
		return self.get_total_revenue(CUSTOMER_ID)

	def get_top_customers_by_revenue(self, count = 10):
		"""
		Finds top customers based on revenue.
		If count provided is more than customers available in data, entire customer list in returned
		"""
		revenue_data = self.get_revenue_per_customer()
		if len(revenue_data) >= count:
			return dict(sorted(revenue_data.items(), key = lambda x:x[1], reverse = True)[0:count])
		return dict(sorted(revenue_data.items(), key = lambda x:x[1], reverse = True))


if __name__ == "__main__":
	order_data = Order_analyser("../test/test_data/orders.csv")
	print(order_data.get_revenue_per_month())
	print(order_data.get_revenue_per_product())
	print(order_data.get_revenue_per_customer())
	print(order_data.get_top_customers_by_revenue(count=5))