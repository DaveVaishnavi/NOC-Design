# utils.py

def read_interface_monitor_output(file_path):
    """
    Function to read interface monitor output from a file.
    Returns a list of dictionaries representing each transaction.
    """
    transactions = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Skip empty lines
                parts = line.split()
                timestamp = int(parts[0])
                txn_type = parts[1]
                data = parts[2] if len(parts) > 2 else None
                transaction = {"Timestamp": timestamp, "TxnType": txn_type, "Data": data}
                transactions.append(transaction)
    return transactions

def set_max_buffer_size(buffer_id, num_entries):
    """
    Function to set the maximum buffer size for a given buffer ID.
    """
    # Implementation to set the maximum buffer size goes here
    print(f"Set buffer size of buffer {buffer_id} to {num_entries}")

def set_arbiter_weights(agent_type, weight):
    """
    Function to set the arbiter weights for a given agent type (CPU or IO).
    """
    # Implementation to set the arbiter weights goes here
    print(f"Set arbiter weight for {agent_type} to {weight}")

def throttle():
    """
    Function to throttle the operating frequency.
    """
    # Implementation to throttle the operating frequency goes here
    print("Throttling the operating frequency")
