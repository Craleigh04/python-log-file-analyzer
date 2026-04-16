def get_unique_messages(filename):
    #Extracts and returns a list of unique event messages from the log file.
    messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) > 2:
                    # Uses append to add the message to the list
                    message = parts[2]
                    if message not in messages:  # Checks if message is not already in the list
                        messages.append(message)

        # Ensures the last message doesn't end with a newline
        if messages:
            last_message = messages[-1]
            if last_message.endswith('\n'):
                messages[-1] = last_message.rstrip('\n')

        return messages
    except Exception as e:
        with open("finalProjExceptions.txt", "a") as error_file:
            error_file.write("Error reading file in get_unique_messages: " + str(e) + "\n")
        print("An error occurred while reading the file. Please check finalProjExceptions.txt for details.")
        return []


def get_ips_by_octet(filename, octet):
    #Finds and returns unique IPs where the first or fourth octet matches the user input.
    unique_ips = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) > 1:
                    ip = parts[1]
                    octets = ip.split('.')
                    if len(octets) == 4 and (octets[0] == octet or octets[3] == octet):
                        # Uses append to add the IP to the list
                        if ip not in unique_ips:  # Ensure no duplicates
                            unique_ips.append(ip)

        # Ensure the last IP doesn't end with a newline
        if unique_ips:
            last_ip = unique_ips[-1]
            if last_ip.endswith('\n'):
                unique_ips[-1] = last_ip.rstrip('\n')

        return unique_ips
    except Exception as e:
        with open("finalProjExceptions.txt", "a") as error_file:
            error_file.write("Error reading file in get_ips_by_octet: " + str(e) + "\n")
        print("An error occurred while processing the file. Please check finalProjExceptions.txt for details.")
        return []


def count_events_per_node(filename):
    #Count occurrences of each node in the log file and return as a dictionary.
    node_counts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) > 0:
                    node = parts[0].strip('[]')
                    # Use append to update counts (though append isn't needed for a dict)
                    if node in node_counts:
                        node_counts[node] += 1
                    else:
                        node_counts[node] = 1
        
        return node_counts
    except Exception as e:
        with open("finalProjExceptions.txt", "a") as error_file:
            error_file.write("Error reading file in count_events_per_node: " + str(e) + "\n")
        print("An error occurred while counting events. Please check finalProjExceptions.txt for details.")
        return {}
 