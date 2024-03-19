from project import check_input, product_performance, stock_threshold
import pytest

def main():
    test_input()
    test_performance()
    test_stock_()

def test_input():
    with pytest.raises(SystemExit):
        check_input()

def test_performance():
    assert product_performance(8) == "low"
    assert product_performance(15) == "medium"
    assert product_performance(24) == "high"

def test_stock():
    assert stock_threshold(10, 20) == "Need to restock"
    assert stock_threshold(10, 2) == "Over-stocked"
    assert stock_threshold(10, 5) == "optimally stocked"

if __name__ == "__main__":
    main()
