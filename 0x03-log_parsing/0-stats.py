import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    # Regular expression patterns for each section of the log line
    patterns = [
        r'\s*(?P<ip>\S+)\s*',                                 # IP Address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',    # Date
        r'\s*"(?P<request>[^"]*)"\s*',                         # HTTP Request
        r'\s*(?P<status_code>\S+)',                             # Status Code
        r'\s*(?P<file_size>\d+)'                                # File Size
    ]
    
    # Initialize dictionary to store extracted information
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    
    # Build the log format pattern from the sub-patterns
    log_format = '{}\\-{}{}{}{}\\s*'.format(*patterns)
    
    # Match the input line against the log format pattern
    match = re.fullmatch(log_format, input_line)
    
    # If a match is found, extract the status code and file size
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('Total file size:', total_file_size, flush=True)
    
    # Sort the status codes in ascending order and print their counts
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print(status_code + ':', count, flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The dictionary storing the status code counts.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    
    # Increment the count for the status code in the dictionary
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    
    # Dictionary to store the count of each status code
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    
    try:
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1
            
            # Print statistics after every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    
    except (KeyboardInterrupt, EOFError):
        # Handle keyboard interruption (CTRL + C) or end-of-file (EOF)
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()