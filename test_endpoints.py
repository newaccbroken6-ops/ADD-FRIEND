#!/usr/bin/env python3
"""
Test script to verify all API endpoints are working correctly
"""

import requests
import json

BASE_URL = "http://localhost:5000"

# Configure session with headers to simulate browser requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Origin': 'http://localhost:5000',
    'Referer': 'http://localhost:5000/'
})

def test_endpoint(endpoint, description, expect_success=True):
    """Test a single endpoint and print results"""
    try:
        response = session.get(f"{BASE_URL}{endpoint}")
        expected_status = 200 if expect_success else 400
        status = "✅ PASS" if response.status_code == expected_status else f"❌ FAIL (expected {expected_status})"
        print(f"{status} {description} - Status Code: {response.status_code}")
        
        # Check CORS headers
        cors_header = response.headers.get('Access-Control-Allow-Origin', 'Not Set')
        print(f"      CORS Header: {cors_header}")
        
        # Print response content for utility endpoints
        if endpoint in ['/health', '/status', '/version', '/metrics', '/info']:
            try:
                data = response.json()
                print(f"      Response: {json.dumps(data, indent=2)[:100]}...")
            except:
                print(f"      Response: {response.text[:100]}...")
        
        return response.status_code == expected_status
    except Exception as e:
        print(f"❌ FAIL {description} - Error: {str(e)}")
        return False

def test_post_endpoint(endpoint, data, description):
    """Test a POST endpoint with data"""
    try:
        response = session.post(f"{BASE_URL}{endpoint}", json=data)
        status = "✅ PASS" if response.status_code == 200 else f"❌ FAIL (status: {response.status_code})"
        print(f"{status} {description} - Status Code: {response.status_code}")
        
        # Print response content
        try:
            data = response.json()
            print(f"      Response: {json.dumps(data, indent=2)[:200]}...")
        except:
            print(f"      Response: {response.text[:200]}...")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ FAIL {description} - Error: {str(e)}")
        return False

def test_add_friend_with_credentials(target_uid, uid, password, server_name=None):
    """Test add_friend endpoint with UID and password"""
    try:
        endpoint = f"{BASE_URL}/add_friend?player_id={target_uid}&uid={uid}&password={password}"
        if server_name:
            endpoint += f"&server_name={server_name}"
            
        response = session.get(endpoint)
        status = "✅ PASS" if response.status_code == 200 else f"❌ FAIL (status: {response.status_code})"
        print(f"{status} Add Friend with Credentials - Status Code: {response.status_code}")
        
        # Print response content
        try:
            data = response.json()
            print(f"      Response: {json.dumps(data, indent=2)[:500]}...")
        except:
            print(f"      Response: {response.text[:500]}...")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ FAIL Add Friend with Credentials - Error: {str(e)}")
        return False

def main():
    print("Testing FreeFire API Endpoints\n")
    print("=" * 50)
    
    # Test utility endpoints
    print("\nUTILITY ENDPOINTS:")
    test_endpoint("/health", "Health Check")
    test_endpoint("/status", "Status Information")
    test_endpoint("/version", "Version Information")
    test_endpoint("/metrics", "System Metrics")
    test_endpoint("/info", "API Information")
    
    # Test core functionality endpoints (these will return error responses without proper parameters)
    print("\nCORE FUNCTIONALITY ENDPOINTS:")
    test_endpoint("/add_friend", "Add Friend (without parameters)", expect_success=False)
    test_endpoint("/remove_friend", "Remove Friend (without parameters)", expect_success=False)
    test_endpoint("/get_player_info", "Get Player Info (without parameters)", expect_success=False)
    test_endpoint("/token", "Generate Token (without parameters)", expect_success=False)
    
    # Test web interface
    print("\nWEB INTERFACE:")
    test_endpoint("/", "Main Page")
    
    # Test the specific case from the user query
    print("\nSPECIFIC TEST CASE FROM USER QUERY:")
    print("Testing add friend with UID: 4501289160, Password: LINUX_NAJMI_ADMIN_L7890, Target ID: 1982843750")
    test_add_friend_with_credentials("1982843750", "4501289160", "LINUX_NAJMI_ADMIN_L7890")
    
    print("\n" + "=" * 50)
    print("Testing complete!")

if __name__ == "__main__":
    main()