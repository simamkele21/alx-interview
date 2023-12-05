#!/usr/bin/python3

""" Web Server Log Analyzer """

import sys


def show_log_summary(stats, total_size):
    """ Display web server log summary """
    print(f"File size: {total_size}")
    for code, count in sorted(stats.items()):
        if count > 0:
            print(f"{code}: {count}")


http_status = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
log_count = 0
total_bytes = 0

try:
    for log_line in sys.stdin:
        if log_count > 0 and log_count % 10 == 0:
            show_log_summary(http_status, total_bytes)

        log_parts = log_line.split()
        log_count += 1

        try:
            # format: <IP Address> - [<date>]
            # "GET /projects/260 HTTP/1.1" <status code> <file size>
            total_bytes += int(log_parts[-1])
        except Exception:
            pass

        try:
            # format: <IP Address> - [<date>]
            # "GET /projects/260 HTTP/1.1" <status code> <file size>
            status_code = log_parts[-2]
            if status_code in http_status:
                http_status[status_code] += 1
        except Exception:
            pass

    show_log_summary(http_status, total_bytes)

except KeyboardInterrupt:
    show_log_summary(http_status, total_bytes)
    raise