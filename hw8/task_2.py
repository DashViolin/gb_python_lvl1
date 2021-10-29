import re


def parse_log_line(line, parser):
    try:
        match = parser.search(line)
        remote_addr = match.group(1)
        request_datetime = match.group(4)
        request_type = match.group(5)
        requested_resource = match.group(6)
        response_code = match.group(8)
        response_size = match.group(9)
        return (
            remote_addr,
            request_datetime,
            request_type,
            requested_resource,
            response_code,
            response_size,
        )
    except Exception as ex:
        print(f'Log parsing error at {line} ({ex})')


log_parser = re.compile(r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)?\s*" (\d{3}) (\S+)')
parsed_rows = []
with open('nginx_logs.txt') as file:
    log_line = file.readline().strip()
    while log_line:
        parsed_rows.append(parse_log_line(log_line, log_parser))
        log_line = file.readline().strip()

print(len(parsed_rows))
