import re
import sys
from collections import defaultdict

def analyze_user_agents(log_file='sample.log'):
    """
    Analyze log file to count requests from each user agent type.
    """
    # Dictionary to store counts for each user agent
    user_agent_counts = defaultdict(int)
    
    # Regular expression to extract user agent
    user_agent_pattern = r'"([^"]*)"$'
    
    try:
        with open(log_file, 'r') as file:
            for line in file:
                # Extract user agent from the end of the log line
                match = re.search(user_agent_pattern, line.strip())
                if match:
                    full_user_agent = match.group(1)
                    
                    # Categorize user agent by browser/platform
                    if "Chrome" in full_user_agent and "Safari" in full_user_agent:
                        if "Macintosh" in full_user_agent:
                            agent_type = "Chrome (Mac)"
                        elif "Windows" in full_user_agent:
                            agent_type = "Chrome (Windows)"
                        elif "Linux" in full_user_agent:
                            agent_type = "Chrome (Linux)"
                        else:
                            agent_type = "Chrome (Other)"
                    elif "Safari" in full_user_agent and "Macintosh" in full_user_agent and "Chrome" not in full_user_agent:
                        agent_type = "Safari (Mac)"
                    elif "Firefox" in full_user_agent:
                        agent_type = "Firefox"
                    elif "MSIE" in full_user_agent or "Trident" in full_user_agent:
                        agent_type = "Internet Explorer"
                    elif "Edge" in full_user_agent:
                        agent_type = "Edge"
                    else:
                        agent_type = "Other"
                    
                    user_agent_counts[agent_type] += 1
        
        # Print results
        print(f"{'User Agent Type':<20} {'Request Count'}")
        print("-" * 40)
        
        # Sort by count in descending order
        for agent_type, count in sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{agent_type:<20} {count}")
        
        # Print total
        print("-" * 40)
        print(f"{'Total':<20} {sum(user_agent_counts.values())}")
            
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    # Use command line argument for log file if provided
    log_file = sys.argv[1] if len(sys.argv) > 1 else 'sample.log'
    analyze_user_agents(log_file)