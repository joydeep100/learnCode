======================
Top 100 Linux Commands
======================

File and Directory Management
=============================

1. ls - List directory contents
      $ ls -l

2. cd - Change directory
      $ cd /home/user/documents

3. pwd - Print current directory
      $ pwd

4. mkdir - Create directories
      $ mkdir new_folder

5. rmdir - Remove empty directories
      $ rmdir empty_folder

6. rm - Remove files or directories
      $ rm file.txt

7. cp - Copy files or directories
      $ cp source.txt destination.txt

8. mv - Move or rename files or directories
      $ mv oldname.txt newname.txt

9. touch - Create empty file or update timestamp
      $ touch newfile.txt

10. find - Search for files in a directory hierarchy
      $ find /home -name '*.txt'

11. locate - Find files by name
      $ locate filename.txt

12. cat - Concatenate and display file content
      $ cat file.txt

13. less - View file content, allowing navigation
      $ less file.txt

14. head - Display the first part of a file
      $ head -n 10 file.txt

15. tail - Display the last part of a file
      $ tail -n 10 file.txt

16. du - Estimate file space usage
      $ du -sh /home/user/

17. df - Report filesystem disk space usage
      $ df -h

18. chmod - Change file permissions
      $ chmod 755 file.txt

19. chown - Change file owner and group
      $ chown user:group file.txt

20. ln - Create symbolic and hard links
      $ ln -s /path/to/file symlink_name


File Viewing and Editing
========================

21. nano - Simple text editor
      $ nano file.txt

22. vim - Advanced text editor
      $ vim file.txt

23. grep - Search for patterns within files
      $ grep 'pattern' file.txt

24. awk - Pattern scanning and text processing
      $ awk '{print $1}' file.txt

25. sed - Stream editor for filtering and transforming text
      $ sed 's/old/new/g' file.txt

26. diff - Compare two files line by line
      $ diff file1.txt file2.txt

27. sort - Sort lines of text files
      $ sort file.txt

28. uniq - Report or omit repeated lines
      $ uniq file.txt

29. wc - Count lines, words, and characters in a file
      $ wc -l file.txt

30. cut - Remove sections from each line of files
      $ cut -d':' -f1 /etc/passwd


System Information and Monitoring
=================================

31. uname - Print system information
      $ uname -a

32. top - Display running processes
      $ top

33. htop - Interactive process viewer
      $ htop

34. ps - Report process status
      $ ps aux

35. free - Display memory usage
      $ free -h

36. uptime - Show system uptime
      $ uptime

37. who - Show who is logged in
      $ who

38. whoami - Print effective user ID
      $ whoami

39. id - Print user and group information
      $ id

40. hostname - Show or set the system's hostname
      $ hostname

41. df -h - Show disk space usage in human-readable format
      $ df -h

42. du -sh - Summarize the size of a directory
      $ du -sh /home/user

43. uname -r - Display kernel version
      $ uname -r

44. dmesg - Print or control the kernel ring buffer
      $ dmesg

45. lscpu - Display CPU architecture info
      $ lscpu

46. lsblk - List information about block devices
      $ lsblk

47. lsusb - List USB devices
      $ lsusb

48. lspci - List PCI devices
      $ lspci

49. iostat - Report CPU and I/O statistics
      $ iostat

50. vmstat - Report virtual memory statistics
      $ vmstat


Network Commands
================

51. ping - Test network connectivity
      $ ping google.com

52. curl - Transfer data to/from a server
      $ curl https://example.com

53. wget - Non-interactive network downloader
      $ wget https://example.com/file.txt

54. ifconfig - Configure network interfaces
      $ ifconfig

55. ip - Show/manipulate routing, devices, policy routing, and tunnels
      $ ip a

56. netstat - Print network connections, routing tables, interface statistics
      $ netstat -tuln

57. ss - Dump socket statistics
      $ ss -tuln

58. nslookup - Query DNS for domain names or IP addresses
      $ nslookup google.com

59. traceroute - Trace the route to a network host
      $ traceroute google.com

60. dig - DNS lookup utility
      $ dig google.com

61. ssh - Secure Shell for remote login
      $ ssh user@hostname

62. scp - Secure copy files between hosts
      $ scp file.txt user@remote:/path

63. rsync - Remote file and directory synchronization
      $ rsync -av /source/ /destination/

64. nmap - Network exploration tool and security scanner
      $ nmap -sP 192.168.1.0/24


User and Permission Management
==============================

65. adduser - Add a user to the system
      $ sudo adduser username

66. deluser - Remove a user from the system
      $ sudo deluser username

67. passwd - Update a user’s password
      $ passwd username

68. su - Substitute user identity
      $ su - username

69. sudo - Execute a command as another user
      $ sudo command

70. groups - Show user groups
      $ groups username

71. usermod - Modify a user account
      $ sudo usermod -aG group username

72. chown - Change file owner and group
      $ chown user:group file.txt

73. chmod - Change file access permissions
      $ chmod 755 file.txt

74. umask - Set default file permissions
      $ umask 022

75. ps aux - View running processes for all users
      $ ps aux


Process Management
==================

76. kill - Terminate a process by PID
      $ kill 1234

77. killall - Kill processes by name
      $ killall process_name

78. xkill - Kill a GUI application
      $ xkill

79. jobs - List background jobs
      $ jobs

80. bg - Resume a stopped job in the background
      $ bg %1

81. fg - Bring a background job to the foreground
      $ fg %1

82. nohup - Run a command immune to hangups
      $ nohup command &


Compression and Archiving
=========================

83. tar - Archive files
      $ tar -cvf archive.tar /path/to/files

84. gzip - Compress files
      $ gzip file.txt

85. gunzip - Decompress `.gz` files
      $ gunzip file.txt.gz

86. zip - Compress files into a zip archive
      $ zip archive.zip file.txt

87. unzip - Extract a zip archive
      $ unzip archive.zip


Package Management (Debian/Ubuntu)
==================================

88. apt-get - Package management command-line tool
      $ sudo apt-get update

89. apt-cache - Query package information
      $ apt-cache search package_name

90. dpkg - Debian package manager
      $ dpkg -i package.deb

91. apt install <package> - Install a package
      $ sudo apt install vim

92. apt update - Update package lists
      $ sudo apt update

93. apt upgrade - Upgrade installed packages
      $ sudo apt upgrade

94. apt remove <package> - Remove a package
      $ sudo apt remove vim


Package Management (Red Hat/CentOS/Fedora)
==========================================

95. yum - Package manager for RPM-based distributions
      $ sudo yum update

96. rpm - Install, update, and query packages
      $ rpm -ivh package.rpm

97. dnf - Updated package manager for Fedora
      $ sudo dnf install vim


System Shutdown and Restart
===========================

98. shutdown - Shut down the system
      $ sudo shutdown -h now

99. reboot - Reboot the system
      $ sudo reboot

100. systemctl - Control the systemd system and service manager
      $ sudo systemctl start service_name