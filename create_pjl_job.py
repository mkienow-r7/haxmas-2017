#!/usr/bin/env python
import sys

def get_binary_data(path):
    data = None
    with open(path, "rb") as binary_file:
        data = binary_file.read()
    return data

escape_sequence = '%-12345X'
commands = [
        escape_sequence + '@PJL JOB NAME = "Haxmas 2017"',
        '@PJL ENTER LANGUAGE = PCL',
        get_binary_data("metasploit-haxmas.pcl"),
        escape_sequence + '@PJL EOF',
        escape_sequence
        ]

sys.stdout.write("\r\n".join(commands))
sys.stdout.flush()
