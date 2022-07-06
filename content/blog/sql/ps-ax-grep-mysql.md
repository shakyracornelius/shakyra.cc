title: ps -ax | grep mysql
date: 2022-07-01
modified: 2022-07-02
tags: sql
slug: ps-ax-grep-mysql

Used to check for the MySQL processes working in the background. 

#### ps

Short for Process Status, the ps command is used to list the status of running processes in the system. By default, it only lists processes of the current user. 

#### -ax

An option passed to ps which allows one to list all process, even beyond the current user. 
- - specifies a standard output. often used as synonym for stdin or stdout.
- a lists processes for all users
- x shows processes not attached to a terminal (i.e. not initiated by users through a terminal) 

#### | grep

- grep with a pipe allows one to search for specific processes. The use of the pipe here is called "piping", which redirects the output of one command to the input of another command.

#### mysql

specifies mysql processes 
