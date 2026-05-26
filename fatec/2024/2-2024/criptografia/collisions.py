import hashlib
import threading
import csv

# Create a list of 10 strings
strings = ["word", "word2", "Word", "Word2", "hello", "world", "python", "code", "test", "example", "sample", "data"]

# Create a table to store the results
table = []

# Define a function to calculate the hashes and check for collisions
def calculate_hashes(string):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    sha1_hash = hashlib.sha1(string.encode()).hexdigest()
    
    # Add the results to the table
    table.append({"string": string, "hash": md5_hash, "algorithm": "md5", "collision": 0})
    table.append({"string": string, "hash": sha1_hash, "algorithm": "sha1", "collision": 0})
    
    # Check for collisions
    for row in table:
        for i in range(1000000):  # Teste com 1 milhão de entradas
            if row["string"] != string and row["hash"] in [md5_hash, sha1_hash]:
                row["collision"] += 1

# Use multithreading to speed up the process
threads = []
for string in strings:
    thread = threading.Thread(target=calculate_hashes, args=(string,))
    threads.append(thread)
    thread2 = threading.Thread(target=collision, args=(string,))
    threads.append(thread2)
    thread.start()
    thread2.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Check for collisions between all hashes
for i in range(len(table)):
    for j in range(i+1, len(table)):
        if table[i]["hash"] == table[j]["hash"]:
            table[i]["collision"] += 1
            table[j]["collision"] += 1


# Output the table as a CSV file
with open("./output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["string", "hash", "algorithm", "collision"])
    for row in table:
        writer.writerow([row["string"], row["hash"], row["algorithm"], row["collision"]])
