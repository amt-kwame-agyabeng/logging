import re
import sys
from collections import defaultdict

def count_endpoints(log_file='sample.log'):
    """
    Analyze log file to count the number of times each endpoint was accessed.
    """
    # Dictionary to store counts for each endpoint
    endpoint_counts = defaultdict(int)
    
    # Regular expression to extract HTTP method and endpoint
    # Pattern matches: "GET /path/to/endpoint HTTP/1.1"
    endpoint_pattern = r'"(\w+) ([^"\s]+) HTTP/[0-9.]+"'
    
    try:
        with open(log_file, 'r') as file:
            for line in file:
                # Extract HTTP method and endpoint
                match = re.search(endpoint_pattern, line)
                if match:
                    method = match.group(1)  # GET, POST, etc.
                    endpoint = match.group(2)  # /path/to/endpoint
                    
                    # Combine method and endpoint for more detailed analysis
                    # Or use just endpoint if you only care about the path
                    key = f"{method} {endpoint}"
                    
                    endpoint_counts[key] += 1
        
        # Print results
        print(f"{'Endpoint':<30} {'Request Count'}")
        print("-" * 45)
        
        # Sort by count in descending order
        for endpoint, count in sorted(endpoint_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{endpoint:<30} {count}")
        
        # Print total
        print("-" * 45)
        print(f"{'Total':<30} {sum(endpoint_counts.values())}")
            
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    # Use command line argument for log file if provided
    log_file = sys.argv[1] if len(sys.argv) > 1 else 'sample.log'
    count_endpoints(log_file)