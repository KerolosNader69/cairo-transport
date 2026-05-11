#!/usr/bin/env python3
"""
Quick test script to verify the API endpoints work correctly.
Run this locally before deploying to production.
"""

import requests
import sys
import json

# Change this to your local or production URL
BASE_URL = "http://localhost:8000"

def test_endpoint(name, url, method="GET", data=None):
    """Test a single endpoint and print results."""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"URL: {url}")
    print(f"Method: {method}")
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        else:
            response = requests.post(url, json=data, timeout=10)
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ SUCCESS")
            data = response.json()
            # Print first few keys or items
            if isinstance(data, dict):
                print(f"Response keys: {list(data.keys())[:5]}")
            elif isinstance(data, list):
                print(f"Response items: {len(data)} items")
                if len(data) > 0:
                    print(f"First item keys: {list(data[0].keys()) if isinstance(data[0], dict) else 'N/A'}")
        else:
            print(f"❌ FAILED")
            print(f"Response: {response.text[:200]}")
            
        return response.status_code == 200
        
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR - Is the server running?")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    """Run all endpoint tests."""
    print("="*60)
    print("API ENDPOINT TEST SUITE")
    print("="*60)
    
    tests = [
        ("Health Check", f"{BASE_URL}/health", "GET"),
        ("Network Summary", f"{BASE_URL}/network/summary", "GET"),
        ("Network Nodes", f"{BASE_URL}/network/nodes", "GET"),
        ("Network Edges", f"{BASE_URL}/network/edges", "GET"),
        ("DB Summary", f"{BASE_URL}/db/summary", "GET"),
        ("DB Demand Pairs", f"{BASE_URL}/db/demand-pairs", "GET"),
        ("DB Bus Routes", f"{BASE_URL}/db/bus-routes", "GET"),
    ]
    
    results = []
    for test in tests:
        success = test_endpoint(*test)
        results.append((test[0], success))
    
    # Print summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Ready to deploy.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Fix issues before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
