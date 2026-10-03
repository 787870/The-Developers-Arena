import unittest
import sys
from pathlib import Path

# Dynamically add the 'src' folder to the system path so we can import our modules
base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir / "src"))

from data_preprocessing import load_and_split_data, build_preprocessor

class TestMLPipeline(unittest.TestCase):
    
    def setUp(self):
        # Locate the dataset for testing
        self.data_path = base_dir / "data" / "house_prices.csv"
        
    def test_data_loading_and_splitting(self):
        """Test if data loads, drops ID, and splits correctly."""
        X_train, X_test, y_train, y_test = load_and_split_data(self.data_path)
        
        # 1. Verify data loaded successfully
        self.assertIsNotNone(X_train, "Training data should not be None")
        
        # 2. Verify the 80/20 split on 300 total rows
        self.assertEqual(len(X_train), 240, "Training set should have exactly 240 rows")
        self.assertEqual(len(X_test), 60, "Testing set should have exactly 60 rows")
        
        # 3. Verify 'Property_ID' was successfully dropped to prevent data leakage
        self.assertNotIn("Property_ID", X_train.columns, "Property_ID should be dropped")
        
    def test_preprocessor_builds(self):
        """Test if the preprocessor initializes properly."""
        preprocessor = build_preprocessor()
        self.assertIsNotNone(preprocessor, "Preprocessor should initialize successfully")

if __name__ == "__main__":
    unittest.main()