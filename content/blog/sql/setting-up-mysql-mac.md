title: Setting Up MySQL on Mac
date: 2022-07-01
tags: sql
slug: setting-up-mysql-mac

I'm using MySQL server because the book I'm currently using to learn SQL (Learn SQL by Alan Beaulieu) uses it for all the examples. 

System Overview 
    macOS Monterey version 12.4<br>
    MacBook Air (13-inch, 2017)<br>
    1.8 GHz Dual-Core Intel Core i5
    8GB 1600 MHz DDR3

#### Setting up MySQL on macOS

I'm following https://dev.mysql.com/doc/mysql-macos-excerpt/5.7/en/macos-installation-pkg.html 

1. Download the disk image (.dmg) file that contains the MySQL package installer [here](https://dev.mysql.com/downloads/mysql/).
2. Select OS Version: macOS12(x86, 64-bit) 
3. Select Download for DMG Archive
4. Select "No thanks, just start my download" when asked to Login Now.
5. Once the download is complete select the .dmg file to mount the disk image and see its contents. 
6. Double-click the MySQL installer package to open the MySQL package installer wizard. In my case the installer package is named *mysql-8.0.29-macos12-x86_64.pkg*. <br>
    Select Allow when the security message pops up.
7. Once the installer wizard is open, 
    - Select Continue to start the installation, 
    - Continue and Agree to the terms and conditions  
    - Install to begin the installation process 
8. After installation is complete, in the configuration window select "Use Strong Password Encryption".
9. Enter a password for the "root" user then select Finish.
10. Decide if you want to keep the installer around. I personally move these files to bin.
11. Open System Preferences to find that MySQL is installed.
12. Open terminal by hitting Command + Space on your keyboard and typing Terminal. Select Terminal
13. Run `mysql -u root -p` to start working with MySQL in the terminal. 
    - mysql = an SQL shell with input line editing capabilities.
    - u = (user_name) the username of the MySQL account to use for connecting to the server.
    - -u root = execute the command as the root user.
    - -p = (password) the password of the MySQL account used for connecting to the server<br>

Learn more about mysql, the MySQL command line client [here])https://dev.mysql.com/doc/refman/8.0/en/mysql.html) and from [man mysql](https://linux.die.net/man/1/mysql).

 







