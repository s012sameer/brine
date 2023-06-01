import pytest
import os
import order

class TestOrderAnalyser:
	"""
	This test file is supposed to use orders.csv fril from test_data dir.
	And compare the response of the code with the expected results
	"""
	@classmethod
	def setup_method(self):
		self.order_data = order.Order_analyser(os.path.join(os.path.dirname(__file__), "test_data/orders.csv"))

	def test_get_revenue_per_month(self):
		expected_result = {'Jan 2023': 69919, 'Feb 2023': 11731, 'Mar 2023': 2499, 'Apr 2023': 11286, 'May 2023': 3849}
		assert self.order_data.get_revenue_per_month() == expected_result

	def test_get_revenue_per_product(self):
		expected_result = {'4001': 59026, '4003': 5121, '4005': 9795, '4007': 4491, '4009': 7111, '4011': 5116, '4013': 6125, '4015': 2499}
		assert self.order_data.get_revenue_per_product() == expected_result

	def test_get_revenue_per_customer(self):
		expected_result = {'10001': 59745, '10002': 6212, '10003': 8894, '10004': 4623, '10005': 3531, '10006': 3577, '10007': 2780, '10008': 5832, '10009': 4090}
		assert self.order_data.get_revenue_per_customer() == expected_result

	def test_get_top_customers_by_revenue(self):
		expected_result = {'10001': 59745, '10003': 8894, '10002': 6212, '10008': 5832, '10004': 4623}
		assert self.order_data.get_top_customers_by_revenue(count=5) == expected_result
