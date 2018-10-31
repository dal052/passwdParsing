# passwdParsing

This script will parse the UNIX /etc/passwd and /etc/groups files and combine the data into a single json output.
To run this script, please download "file_join.py" file and run the following command:

python file_join.py -g "location of groups file" -p "location of passwd file"

And the resulting file will be created in the same directory where "file_join.py" is located as "result.json" file. 
If the options are not specified, it will default to get the file from "/etc/passwd" and "/etc/groups".

