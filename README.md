# Log Analysis Tools

A collection of Python scripts for analyzing web server log files.

## Overview

This repository contains tools for extracting insights from web server logs, including:

- User agent analysis
- Request frequency analysis
- IP address activity monitoring
- Endpoint popularity analysis

## Scripts

### analyze_user_agents.py

Analyzes log files to count requests from each user agent type.

```bash
python analyze_user_agents.py [log_file]
```

**Features:**
- Categorizes user agents by browser and platform
- Provides a summary of request counts by user agent type
- Handles common log formats

### analyze_requests.py

Analyzes log files to count requests from each IP address within a 10-second window after their first request.

```bash
python analyze_requests.py [log_file]
```

**Features:**
- Identifies IP addresses with high request frequency
- Calculates request counts within configurable time windows
- Helps detect potential automated traffic or DoS attempts

### count_endpoints.py

Analyzes log files to count requests for each endpoint.

```bash
python count_endpoints.py [log_file]
```

**Features:**
- Counts requests by HTTP method and endpoint
- Identifies most frequently accessed resources
- Helps understand traffic patterns and resource usage

## Log Format

The scripts expect logs in the following format:

```
YYYY-MM-DDThh:mm:ss.sssZ IP_ADDRESS - - [DD/Mon/YYYY:hh:mm:ss +0000] "METHOD PATH HTTP/1.1" STATUS_CODE - "REFERRER" "USER_AGENT"
```

Example:
```
2025-06-03T10:09:02.588Z 197.159.135.110 - - [03/Jun/2025:10:09:02 +0000] "GET /favicon.ico HTTP/1.1" 200 - "http://108.129.212.117:8080/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
```

## Requirements

- Python 3.6+
- Standard library modules only (no external dependencies)

## Usage Examples

### Analyzing User Agents

```bash
python analyze_user_agents.py sample.log
```

Output:
```
User Agent Type      Request Count
----------------------------------------
Chrome (Linux)       182
Chrome (Windows)     42
Safari (Mac)         53
Firefox              21
Internet Explorer    6
Edge                 0
Other                167
----------------------------------------
Total                471
```

### Analyzing Request Frequency

```bash
python analyze_requests.py sample.log
```

Output:
```
IP Address           First Request Time        Requests in 10s Window
-----------------------------------------------------------------
197.159.135.110      2025-06-03 10:09:02       182
154.161.35.247       2025-06-03 10:09:02       113
196.61.35.158        2025-06-03 10:08:37       54
185.195.59.88        2025-06-03 10:09:06       53
154.161.141.194      2025-06-03 10:09:02       42
129.222.148.186      2025-06-03 10:08:57       21
154.161.40.25        2025-06-03 10:09:29       6
-----------------------------------------------------------------
Total: 7 IPs, 471 requests
```

### Analyzing Endpoint Popularity

```bash
python count_endpoints.py sample.log
```

Output:
```
Endpoint                                 Request Count
-------------------------------------------------------
GET /                                    408
GET /favicon.ico                         316
-------------------------------------------------------
Total                                    724
```

## Screenshots

The repository includes screenshots of the analysis results for quick reference:

- `screenshots/user_agents.png` - Visual representation of user agent distribution
- `screenshots/request_frequency.png` - Chart showing IP address request frequency
- `screenshots/endpoint_popularity.png` - Graph of most accessed endpoints

These screenshots provide a visual summary of the analysis results and can be used in reports or presentations.

## Future Enhancements

- Add support for additional log formats
- Implement geographic IP analysis
- Create visualization tools for log data
- Support for distributed log analysis
- Add response time analysis
- Implement anomaly detection for unusual traffic patterns
- Add export functionality for CSV/JSON formats
- Create interactive dashboard for real-time monitoring