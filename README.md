Honeypot Log Analyzer & Threat Mapper::

A lightweight, defensive cybersecurity project built with Python that simulates a trap (honeypot) service to detect unauthorized connection attempts and automatically analyzes attack logs.


Features:
Simulated Trap (Honeypot):Listens on a dedicated port (`2222`) to capture unauthorized access or intrusion attempts.
Real-time Logging: Automatically records precise timestamps and the attacker's IP address into an external log file (`attack_logs.txt`).
Log Analyzer:Parses the generated log files and provides a structured summary report of total attacks per IP address.



Project Structur:
HoneypotProject/
honeypot.py
analyzer.py
attack_logs.txt


How to Run & Test:

Step 1: Start the Honeypot::
Open your terminal (CMD or PowerShell), navigate to your project directory, and run the trap script:  " python honeypot.py " 
(The server will start listening and waiting for connections on port 2222)


Step 2: Simulate an Attack::
Open a new terminal window, navigate to the project folder, and run the following command to test a connection attempt: 'telnet localhost 2222'
(You can repeat this multiple times to simulate continuous intrusion attempts)


Step 3: Analyze the Logs ::
Open another new terminal window, navigate to the project directory, and run the analyzer script to view the threat intelligence report: ' python analyzer.py '


Requirements::
Python 3.x

No external third-party dependencies required (relies purely on Python's built-in socket, datetime, and collections modules).
