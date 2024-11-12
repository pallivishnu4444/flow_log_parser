import csv
from collections import defaultdict, Counter

def load_lookup_table(lookup_file):
    """Load lookup table from CSV and return a dictionary mapping (dstport, protocol) to tag."""
    lookup_table = {}
    with open(lookup_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Normalize case for protocol and strip whitespaces
            dstport = row['dstport'].strip()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            lookup_table[(dstport, protocol)] = tag
    return lookup_table

def parse_flow_logs(flow_log_file, lookup_table):
    """Parse flow logs and categorize each row based on lookup table."""
    tag_counts = Counter()
    port_protocol_counts = Counter()

    with open(flow_log_file, mode='r') as file:
        for line in file:
            parts = line.split()
            dstport = parts[5].strip()
            protocol = 'tcp' if parts[7] == '6' else 'udp' if parts[7] == '17' else None
            
            if protocol:
                lookup_key = (dstport, protocol)
                tag = lookup_table.get(lookup_key, 'Untagged')
                tag_counts[tag] += 1
                port_protocol_counts[lookup_key] += 1

    return tag_counts, port_protocol_counts

def write_output(output_file, tag_counts, port_protocol_counts):
    """Write output for tag counts and port/protocol combination counts to file."""
    with open(output_file, mode='w') as file:
        # Write Tag Counts
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")

        # Write Port/Protocol Combination Counts
        file.write("\nPort/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

if __name__ == '__main__':
    # File paths (replace these with actual file paths)
    lookup_file = 'lookup_table.csv'
    flow_log_file = 'flow_logs.txt'
    output_file = 'output_results.txt'

    # Load the lookup table
    lookup_table = load_lookup_table(lookup_file)

    # Parse flow logs and get tag and port/protocol counts
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)

    # Write the results to the output file
    write_output(output_file, tag_counts, port_protocol_counts)

    print(f"Processing complete. Results saved to {output_file}")
