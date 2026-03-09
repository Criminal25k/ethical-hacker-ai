"""
Unit tests for Ethical Hacker AI modules
"""

import unittest
from src.ai.vulnerability_detector import VulnerabilityDetector
from src.ai.threat_analyzer import ThreatAnalyzer
from src.tools.port_scanner import PortScanner
from src.tools.exploit_finder import ExploitFinder

class TestVulnerabilityDetector(unittest.TestCase):
    """Test VulnerabilityDetector class"""
    
    def setUp(self):
        self.detector = VulnerabilityDetector()
    
    def test_scan_target(self):
        """Test vulnerability scanning"""
        result = self.detector.scan_target("example.com")
        self.assertIsInstance(result, list)

class TestThreatAnalyzer(unittest.TestCase):
    """Test ThreatAnalyzer class"""
    
    def setUp(self):
        self.analyzer = ThreatAnalyzer()
    
    def test_analyze_threat(self):
        """Test threat analysis"""
        result = self.analyzer.analyze_threat("SQL Injection")
        self.assertIn('risk_level', result)

class TestPortScanner(unittest.TestCase):
    """Test PortScanner class"""
    
    def setUp(self):
        self.scanner = PortScanner("localhost")
    
    def test_initialization(self):
        """Test port scanner initialization"""
        self.assertEqual(self.scanner.target, "localhost")

class TestExploitFinder(unittest.TestCase):
    """Test ExploitFinder class"""
    
    def setUp(self):
        self.finder = ExploitFinder()
    
    def test_find_exploits(self):
        """Test exploit finding"""
        result = self.finder.find_exploits("SQL Injection")
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()