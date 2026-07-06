## High-tier AppSec engineers know how attacks look in the backend.

### The Task: 
    Write a Python script that acts as a log parser. Create a mock access.log text file on your local machine containing a mix of normal web traffic and SQLi attempts (e.g., requests with %27, UNION, SELECT, WAITFOR).

### The Logic: 
    Your script should open the file, read line by line, decode any URL-encoded payloads using urllib.parse.unquote, and flag IP addresses that trigger specific SQLi regex patterns.

### The Goal: 
    This builds your Python file-handling, string manipulation, and regex skills—all essential for parsing data, whether you are attacking or defending.