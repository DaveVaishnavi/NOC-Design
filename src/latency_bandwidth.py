# latency_bandwidth.py

def calculate_latency_and_bandwidth(interface_monitor_output):
    total_latency = 0
    total_bandwidth = 0
    num_transactions = 0
    
    for transaction in interface_monitor_output:
        if transaction["TxnType"] == "Rd":
            latency_start = transaction["Timestamp"]
            latency_end = find_data_timestamp(transaction, interface_monitor_output)
            latency = latency_end - latency_start
            total_latency += latency
        elif transaction["TxnType"] == "Wr":
            total_bandwidth += 32  # Assuming fixed data width of 32 bytes per transfer
        
        num_transactions += 1
    
    average_latency = total_latency / num_transactions
    average_bandwidth = total_bandwidth / num_transactions
    
    return average_latency, average_bandwidth

def find_data_timestamp(transaction, interface_monitor_output):
    for subsequent_transaction in interface_monitor_output:
        if subsequent_transaction["TxnType"] == "Data" and subsequent_transaction["Timestamp"] > transaction["Timestamp"]:
            return subsequent_transaction["Timestamp"]
    return None
