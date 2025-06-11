#!/usr/bin/env python3
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

def analyze_requests(log_file='sample.log'):
    """
    Analyze log file to count requests from each IP address within a 10-second window
    after their first request.
    """
    # Dictionary to store first request timestamp for each IP
    first_requests = {}
    
    # Dictionary to store count of requests within 10-second window for each IP
    request_counts = defaultdict(int)
    
    # Regular expression to extract timestamp and IP address
    log_pattern = r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (\d+\.\d+\.\d+\.\d+)'
    
    try:
        with open(log_file, 'r') as file:
            for line in file:
                # Extract timestamp and IP address
                match = re.search(log_pattern, line.strip())
                if match:
                    timestamp_str = match.group(1)
                    ip_address = match.group(2)
                    
                    # Parse timestamp
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                    
                    # If this is the first request from this IP, record it
                    if ip_address not in first_requests:
                        first_requests[ip_address] = timestamp
                        # Count the first request
                        request_counts[ip_address] = 1
                    else:
                        # Check if this request is within 10 seconds of the first request
                        first_timestamp = first_requests[ip_address]
                        if timestamp <= first_timestamp + timedelta(seconds=10):
                            request_counts[ip_address] += 1
        
        # Print results
        print(f"{'IP Address':<20} {'First Request Time':<25} {'Requests in 10s Window'}")
        print("-" * 65)
        
        # Sort by request count in descending order
        for ip, count in sorted(request_counts.items(), key=lambda x: x[1], reverse=True):
            first_time = first_requests[ip].strftime('%Y-%m-%d %H:%M:%S')
            print(f"{ip:<20} {first_time:<25} {count}")
        
        # Print total
        print("-" * 65)
        total_ips = len(request_counts)
        total_requests = sum(request_counts.values())
        print(f"Total: {total_ips} IPs, {total_requests} requests")
            
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    # Use command line argument for log file if provided
    log_file = sys.argv[1] if len(sys.argv) > 1 else 'sample.log'
    analyze_requests(log_file)