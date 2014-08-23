SSH Brute Forcer

Simple multi threaded SSHBrute Forcer, Standard Brute Forcing and Dictonary based attacks.

Note: The brute force method is really bad just trys random strings with different lengths. Also it will attempt to create a lot of threads if you say 1000 attempts it will create 1000 threads.. Why you might ask because no one should really ever use this feature.

Usage:

Single Ip Dictonary Attack: 
python SSHBruteForce.py -i 127.0.0.1 -d True -p 2222 -U ./usernames.txt -P ./passwords.txt

Single Ip Dictonary Attack Specifying threads and timeout:
python SSHBruteForce.py -i 127.0.0.1 -d True -p 2222 -U ./usernames.txt -P ./passwords.txt -t 15 -T 30

Multiple Ip Dictonary Attack:
python SSHBruteForce.py -I ./targets.txt -d True -p 2222 -U ./usernames.txt -P ./passwords.txt -t 15 -T 30

Single Ip BruteForce Attack:
python SSHBruteForce.py -i 127.0.0.1 -p 22 -a 100 -l 8

Multiple Ip BruteForce Attack:
python SSHBruteForce.py -I targets.txt -p 22 -a 100 -l 8

Example of targets.txt:
127.0.0.1:22
127.0.0.2:23

Example of usernames.txt:
jimmyj
derpt
marth

Example of passwords.txt:
love
god
sex
secret

For educational use only.