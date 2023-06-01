This Application provides API endpoints to analyze data provided in orders.csv file.
The orders.csv file is required to be available in "./data" directory which gets mounted inside the container when run.

Building docker image
# docker build --tag order_analyser .

Testing the code functionality
# docker run -t --name docker_analyser_app_test order_analyser -m pytest test/test.py

Running application in background
# docker run -d --name docker_analyser_app -p 5000:5000 -v ${PWD}/data:/data order_analyser

API endpoints exposed for tasks - 
1. Total revenue generated for each month - http://127.0.0.1:5000/revenue?per=month
2. Total revenue generated by each product - http://127.0.0.1:5000/revenue?per=productid
3. Total revenue generated by each customer - http://127.0.0.1:5000/revenue?per=customerid
4. Top 10 customers by revenue generated - http://127.0.0.1:5000/revenue?per=topcustomer&count=10