## Postmoterm

An outage occurred on an isolated ‘Ubuntu 14.04’ container running an Apache web server. GET request led to 500 internal server error when the response was supposed t be an HTML file
This error lasted for over an hour from 19:00 – 20:00(WAT).
This error was caused by the whitespace while naming the file which resulted in the file not loading and giving an error message instead
Debugging process
1.	Checked running process
2.	Looked into the sites folder to determine if the server was serving content located in the right directory
3.	After running strace several times and finally found an error message indicating no such file or directory
4.	Sorting through the mentioned directory through the error message and found trailing white space
5.	Tested another curl on the server after the correction. 200 A-ok
6.	Wrote a puppet manifest to automate fixing of the error 
	
The outage was not a server error but an application problem so it is advised to test the application before deploying so as to prevent anything like this from happening 

