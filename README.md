# SSH Log Analyzer 🔍

## 📌 Overview  
This Python script analyzes SSH login attempts by reading the `/var/log/auth.log` file, counting the number of failed login attempts per IP, and automatically blocking attackers with `iptables` once a threshold is exceeded.  

It helps system administrators prevent brute-force attacks by blocking malicious IPs after a set number of failed login attempts.

## 🚀 Features  
- Detects failed SSH login attempts from the system log (`/var/log/auth.log`)
- Counts the number of failed login attempts per IP address
- Blocks attackers automatically with `iptables` if the threshold is exceeded
- Simple to use and customizable

## 🛠 Installation  
1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/stfxn-303/ssh-log-analyzer.git
    cd ssh-log-analyzer
    ```

2. **Install dependencies** (Python’s `requests` package for Telegram alerts):
    ```bash
    pip install requests
    ```

3. **Run the script** (it requires `sudo` to modify firewall rules):
    ```bash
    sudo python3 ssh_log_analyzer.py
    ```

    This will:
    - Analyze the `/var/log/auth.log` file for failed SSH login attempts
    - Block any IP addresses that exceed the threshold of failed attempts (default is 5)

## 🖥 Example Output  
The script will print out any detected failed login attempts and block malicious IPs:
IP: 192.168.1.100 | Failed Attempts: 7 🚨 Blocking IP: 192.168.1.100 (Failed Attempts: 7)

## 🔧 Customization  
- **Change the threshold for blocking**: You can modify the `THRESHOLD` variable in the script to change the number of failed attempts before blocking an IP.
- **Telegram alerts**: You can enable Telegram alerts by adding your bot token and chat ID. Set `ENABLE_TELEGRAM_ALERTS = True` and update the variables accordingly.

## 📌 TODO  
- Add email notifications for blocked IPs
- Improve logging functionality for better tracking
- Implement automatic removal of blocked IPs after a certain time

## 📝 License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
