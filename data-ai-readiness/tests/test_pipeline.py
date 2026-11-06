import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from pipeline import assess_quality,read_rows
class TestDemo(unittest.TestCase):
    def test_order_count(self): self.assertEqual(len(read_rows('erp_orders.csv')),10)
    def test_orphan_customer(self): self.assertIn('UNKNOWN_CUSTOMER',{x['rule'] for x in assess_quality()})
    def test_bad_quality(self): self.assertIn('INVALID_DEFECT_COUNT',{x['rule'] for x in assess_quality()})
    def test_price_missing(self): self.assertIn('INVALID_PRICE',{x['rule'] for x in assess_quality()})
if __name__=='__main__':unittest.main()
