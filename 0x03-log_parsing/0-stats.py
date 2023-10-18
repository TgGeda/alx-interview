#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

# Initialize variables
total_file_size = 0
status_code_counts = {}

line_count = 0
try:
    # Read input line by line from stdin
    for line in sys.stdin:
        line_count += 1
        
        # Parse the input line
        parts = line.split()
        if len(parts) >= 7:
            ip_address = parts[0]
            status_code = parts[-3]
            file_size = int(parts[-2])
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for status_code in sorted(status_code_counts.keys()):
                count = status_code_counts[status_code]
                print(f"{status_code}: {count}")
            print()
except KeyboardInterrupt:
    pass

# Print final statistics
print("Total file size:", total_file_size)
for status_code in sorted(status_code_counts.keys()):
    count = status_code_counts[status_code]
    print(f"{status_code}: {count}")
