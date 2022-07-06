title: How to Uninstall MySQL on Mac
date: 2022-07-01
tags: sql
slug: uninstall-mysql-mac


I'm uninstalling MySQL to do the install from scratch for the purpose of writing the "Setting up MySQL on Mac" blogpost. 

I'm following steps from [Asya's](https://nektony.com/how-to/uninstall-mysql-on-mac) article.

Key notes:

- For this to work, we're gonna have to remove all supporting files for MySQL server
- Applications usually store their service file in the Library folder but might sprinkle them around your device. 
    - What is the Library folder? 
    - A folder that comes with your Mac and is used to store settings, preferences, cache etc... It can be found in the root directory (usually Macintosh HD) [1](https://www.macrumors.com/how-to/reveal-library-folder-in-macos/ ), [2](https://support.apple.com/en-gb/guide/mac-help/mchlp1143/mac)
- Tread carefully, deleting service files can damage your system. 

#### Steps to Uninstall

1. Open System Preferences by hitting Command ⌘ + Space on your keyboard then typing System Preferences
2. Select MySQL (usually located way at the bottom of the window). In the MySQL window, select Uninstall.
3. Remove MySQL database using the Terminal command line. See steps below. 
4. Open Terminal by hitting Command ⌘ + Space on your keyboard then typing Terminal
5. We will now enter a series of commands to back up and remove the databases. Hit return after each command.
    1. To back up data: <br>
    `mysqldump`
    2. To check if MySQL processes are working in the background: <br>
    [`ps -ax | grep mysql`]({filename}/blog/sql/ps-ax-grep-mysql.md) <br>
    A result like the following tells us that the only running process is the grep command and no mysql processes are running:
    
        > 728135 ttys000    0:00.01 grep mysql
    
    3. To remove the msql directory (if required, enter your user password): <br>
    `sudo rm /usr/local/mysql`<br>
        - sudo = short for "superuser do", allows one to run commands as super user
        - rm = stands for remove, is used to delete files and directories 1
        - /usr/local/mysql = specifies the directory to remove 
    4. To remove MySQL files (press enter after each command):
    `sudo rm -rf /usr/local/var/mysql`
        - "-r" = (-recursive), recursively deletes everything in a directory  
        - "-f" = (-force), used to avoid prompts asking if you want to remove the file 1   
    `sudo rm -rf /usr/local/mysql*`<br>
    `sudo rm ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist`<br>
    `sudo rm -rf /Library/StartupItems/MySQLCOM`<br>
    `sudo rm -rf /Library/PreferencePanes/My*`<br>
    Edit /etc/hostconfig and remove the line MYSQLCOM=-YES- <br>
    Remove MySQL preferences: <br>
    `rm -rf ~/Library/PreferencePanes/My*`<br>
    `sudo rm -rf /Library/Receipts/mysql*`<br>
    `sudo rm -rf /Library/Receipts/MySQL*`<br>
    `sudo rm -rf /private/var/db/receipts/*mysql*`<br>

6. Restart your Mac to ensure all MySQL processes are killed. MySQL should now be uninstalled completely.
