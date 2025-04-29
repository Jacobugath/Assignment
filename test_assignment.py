import unittest
import data_ingestion

class Testingestion(unittest.TestCase):
    def test_dic(self):
        for i in data_ingestion.get_csv_data():
            self.assertTrue("transaction_id" in i, f"Key 'transaction_id' not found in dictionary")
            self.assertTrue("product_id" in i, f"Key 'product_id' not found in dictionary")
            self.assertTrue("quantity" in i, f"Key 'quantity' not found in dictionary")
            self.assertTrue("sale_amount" in i, f"Key 'sale_amount' not found in dictionary")
        for i in data_ingestion.get_json_data():
            self.assertTrue("product_id" in i, f"Key 'product_id' not found in dictionary")
            self.assertTrue("product_name" in i, f"Key 'product_name' not found in dictionary")
            self.assertTrue("category" in i, f"Key 'category' not found in dictionary")
            self.assertTrue("price" in i, f"Key 'price' not found in dictionary")
            self.assertTrue("availability" in i, f"Key 'availability' not found in dictionary")



if __name__ == '__main__':
    unittest.main()