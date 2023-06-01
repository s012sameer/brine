from flask import Flask, request, jsonify, abort
import os
import logger
from order import Order_analyser

logger = logger.get_logger(__name__)

app = Flask(__name__)

app_dir = os.path.dirname(__file__)
#order_data = Order_analyser(os.path.join(app_dir, "../test/test_data/orders.csv"))
"""
Assuming that we are mounting our host dir having orders.csv to /data dir of the container
"""
order_data = Order_analyser("/data/orders.csv")

@app.before_request
def valid_parameters():
    """
    Validates parameters provided in URL
    """
    parameter = request.args.get("per")
    if parameter:
        if parameter in ("topcustomer", "customerid", "productid", "month"):
            if parameter == "topcustomer":
                if len(request.args) != 2 or not request.args.get("count", type = int):
                    abort(404)
            elif len(request.args) != 1:
                abort(404)
        else:
            abort(404)

@app.route("/")
def get_order_data():
    return order_data.order_data

@app.route("/revenue")
def get_revenue_per_parameter():
    parameter = request.args.get("per")
    if parameter == "topcustomer":
        count = int(request.args.get("count"))
        logger.info(f"Getting top {count} customers with maximum revenue")
        return order_data.get_top_customers_by_revenue(count = count)
    elif parameter == "customerid":
        logger.info("Getting revenue generated per customer")
        return order_data.get_revenue_per_customer()
    elif parameter == "productid":
        logger.info("Getting revenue generated per product")
        return order_data.get_revenue_per_product()
    elif parameter == "month":
        logger.info("Getting revenue generated per month")
        return order_data.get_revenue_per_month()


if __name__ == "__main__":
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=False, host='0.0.0.0', port=port)
    except Exception as e:
        logger.error(f"Failed to run: {e}")
