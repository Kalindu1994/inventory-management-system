# Inventory Management System with Performance Analysis

Video Demo:  <https://youtu.be/qVTEdaNnm50>

Description:

This project is an inventory Management System with Performance Analysis aimed at automating inventory management tasks and analyzing product performance based on historical sales data for Small business. The system reads input data from a CSV file containing information about products, such as ID, description, current stock, and sales during the last month. It then processes this data to provide insights into product performance and stock thresholds.

Project Components:

Main Functionality:
    The main functionality of the project is implemented in the main() function, which orchestrates the entire process. It reads input data from the CSV file, calculates product performance, determines stock thresholds, and writes the results to an output CSV file.

Input Validation:
    The check_input() function ensures that the correct number of command-line arguments is provided and that the arguments are CSV files. It raises SystemExit if any validation checks fail.

Product Performance Analysis:
    The product_performance() function analyzes the performance of each product based on the quantity sold during the last month. It categorizes products as "low," "medium," or "high" performers based on predefined thresholds.

Stock Threshold Calculation:
    The stock_threshold() function calculates the stock threshold for each product based on its current stock level and sales during the last month. It determines whether the product needs to be restocked, is overstocked, or is optimally stocked.

Testing:
    The project includes unit tests implemented using pytest to ensure the correctness of the implemented functions. Test cases cover input validation, product performance analysis, and stock threshold calculation.

Project Explanation (500 words):

The Inventory Management System with Performance Analysis project is designed to simplify inventory management tasks for businesses while providing insights into product performance.

When you run the project, it prompts you to provide input and output CSV files containing product information. The system then processes this data to generate a report containing the performance analysis and stock thresholds for each product.

The system begins by validating the input provided by the user. It checks if the correct number of command-line arguments is provided and if the arguments are CSV files. If any validation checks fail, the system exits gracefully.

Once the input is validated, the system reads the product data from the input CSV file. For each product, it calculates the performance based on the quantity sold during the last month. Products are categorized as "low," "medium," or "high" performers depending on their sales performance.

Next, the system calculates the stock threshold for each product. It considers the current stock level and the quantity sold during the last month to determine whether a product needs to be restocked, is overstocked, or is optimally stocked.

Finally, the system writes the results to an output CSV file, providing a comprehensive report on product performance and stock thresholds.

In summary, the Inventory Management System with Performance Analysis automates inventory management tasks and provides valuable insights into product performance, helping businesses make informed decisions about their inventory levels and stocking strategies.
