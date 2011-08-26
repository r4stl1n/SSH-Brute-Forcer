SSH Brute Forcer

Simple multi threaded ssh brute forcer. Using a dictionary attack method.

Usage:

Single Ip Brute Force: 
sshBruteForcer.py -i 127.0.0.1 -p 22 -U usernames.txt -P passwords.txt

Single Ip Brute Force Specifying threads and timeout:
sshBruteForcer.py -i 127.0.0.1 -p 22 -U usernames.txt -P passwords.txt -t 15 -T 30

Multiple Ip Brute Force:
sshBruteForcer.py -I targets.txt -p 22 -U usernames.txt -P passwords.txt -t 15 -T 30

Use the -O flag to specify an output file:
sshBruteForcer.py -I targets.txt -p 22 -U usernames.txt -P passwords.txt -t 15 -T 30 -O output.txt


Example of targets.txt:
127.0.0.1:22
127.0.0.2:23