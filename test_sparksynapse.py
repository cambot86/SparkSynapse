# test_sparksynapse.py
"""
Tests for SparkSynapse module.
"""

import unittest
from sparksynapse import SparkSynapse

class TestSparkSynapse(unittest.TestCase):
    """Test cases for SparkSynapse class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkSynapse()
        self.assertIsInstance(instance, SparkSynapse)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkSynapse()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
