# test_latency_bandwidth.py

import unittest
from latency_bandwidth import calculate_latency_and_bandwidth

class TestLatencyBandwidth(unittest.TestCase):

    def test_basic_scenario(self):
        # Test basic scenario with a few transactions
        interface_monitor_output = [
            {"Timestamp": 0, "TxnType": "Rd", "Data": "-"},
            {"Timestamp": 2, "TxnType": "Wr", "Data": "hxxxxxxxx"},
            {"Timestamp": 4, "TxnType": "Wr", "Data": "hyyyyyyyy"},
            {"Timestamp": 10, "TxnType": "Data", "Data": "hzzzzzzzz"}
        ]
        avg_latency, avg_bandwidth = calculate_latency_and_bandwidth(interface_monitor_output)
        self.assertAlmostEqual(avg_latency, 5.5, delta=0.01)
        self.assertAlmostEqual(avg_bandwidth, 32, delta=0.01)

    # Additional test cases can be added to cover different scenarios and edge cases

if __name__ == '__main__':
    unittest.main()
