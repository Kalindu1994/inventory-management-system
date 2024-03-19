import sys
import csv

def main():
    check_input()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("No CSV file Found")

    output = []
    for row in data:
        performance = product_performance(row["sold_during_last_month"])
        threshold = stock_threshold(row["stock"], row["sold_during_last_month"])
        output.append({"id": row["id"], "description": row["description"], "product_performance": performance, "stock_threshold": threshold})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "description", "product_performance_during_last_month", "stock_threshold"])
        writer.writerow({"id": "id", "description": "description", "product_performance_during_last_month": "product_performance_during_last_month", "stock_threshold": "stock_threshold"})
        for row in output:
            writer.writerow({"id": row["id"], "description": row["description"], "product_performance_during_last_month": row["product_performance"], "stock_threshold": row["stock_threshold"]})

def check_input():
    if len(sys.argv) > 3:
        sys.exit("Too Many Command-line Arguments")
    if len(sys.argv) < 3:
        sys.exit("Too Few Command-line Arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV File")


def product_performance(per):
    if 10 <= int(per) <= 20:
        return "medium"
    elif int(per) >= 20:
        return "high"
    else:
        return "low"

def stock_threshold(stock, sold_during_last_month):
    buffer_stock = 5
    if int(stock) < (int(sold_during_last_month) + buffer_stock):
        return "Need to restock"=
    elif int(stock) > (int(sold_during_last_month) + buffer_stock):
        return "Over-stocked"
    else:
        return "optimally stocked"


if __name__ == "__main__":
    main()
