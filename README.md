# Flow Log Parser

## Description
This program parses flow log data and maps each row to a tag based on a lookup table. The program supports a default log format (version 2) and maps the `dstport` and `protocol` to tags defined in the `lookup_table.csv`.

## Assumptions
- The program only supports the default flow log format (version 2).
- Only basic CSV parsing and file handling are used.
- The lookup table CSV and flow logs should be case-insensitive.

## Installation
1. Clone this repository:
   ```bash
   git clone 
   ```
2. Download the flow logs and lookup table and place them in the project folder.

## How to Run the Program
To run the program, use the following command:
```bash
python flow_log_parser.py

