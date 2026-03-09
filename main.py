"""
Main entry point for Ethical Hacker AI System
"""

from src.ai.vulnerability_detector import VulnerabilityDetector
from src.ai.threat_analyzer import ThreatAnalyzer
from src.tools.port_scanner import PortScanner
from src.tools.network_analyzer import NetworkAnalyzer
from src.tools.exploit_finder import ExploitFinder

def main():
    """Main function to demonstrate the system"""
    print("=" * 60)
    print("Ethical Hacker AI System - v1.0")
    print("=" * 60)
    
    # Initialize modules
    vuln_detector = VulnerabilityDetector()
    threat_analyzer = ThreatAnalyzer()
    exploit_finder = ExploitFinder()
    
    # Example usage
    print("\n[*] Starting security analysis...")
    
    # Scan for vulnerabilities
    vulnerabilities = vuln_detector.scan_target("example.com")
    print(f"[+] Found vulnerabilities: {len(vulnerabilities)}")
    
    # Analyze threats
    threat_result = threat_analyzer.analyze_threat("SQL Injection")
    print(f"[+] Threat analysis: {threat_result}")
    
    # Find exploits
    exploits = exploit_finder.find_exploits("SQL Injection")
    print(f"[+] Found exploits: {len(exploits)}")
    
    print("\n[*] Security analysis complete!")

if __name__ == "__main__":
    main()