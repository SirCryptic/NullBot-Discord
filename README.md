# Nullbot-Reboot - [BETA] - Discord Auditing Bot

NullBot Beta is a multi-purpose Discord bot for system administrators and security enthusiasts. The bot is capable of executing commands through Discord to perform various tasks, such as detecting the operating system and finding open ports on a host using Nmap, and scanning a web server for vulnerabilities using Nikto. The bot is also equipped with an authorization system to prevent unauthorized users from running certain commands. This bot was developed by [SirCryptic](https://github.com/sircryptic) of [NullSecurityTeam](https://github.com/orgs/NULL-Security-Team), and is open-source under the [MIT license](https://github.com/SirCryptic/Nullbot-Reboot/blob/main/LICENSE).

# Changelog
<details>
  <summary>Click to expand!</summary>
  
  - Now splits the output into chunks of 2000 characters to fit in Discord messages (Sends in multiple messages if too large)
  
  - Added a check if the input is a domain name
  </details>


# Installation Instructions

1. Install the required Python packages using pip: `pip install -r requirements.txt`
2. Create a new Discord bot account on the Discord developer portal.
3. Add the bot to your server by following the instructions in the Discord developer portal.
4. Copy the bot token and replace the value of `client.run('your_bot_token')` in `nullbot.py` with the bot token.

# Running The Bot
```
sudo python3 nullbot.py
```

## How do I use the bot?

To use the bot, you can type the following commands ...

- `!console help` - Displays the list of available functions
- `!console nmap [host]` - Detect OS & Find Open Ports On A Host
- `!console nikto -h [host]` - Scan a web server for vulnerabilities


 # ⚠️ Foot Notes / Q&A ⚠️

Q: Why do i have to run this as root?

A: Unfortunatly you have to run the bot as root or the nmap command doesnt function properly and prompts you on the host machine to input your password.

Q: Can anyone Execute Commands & Scan the host machine?

A: NO! Only specific rolls can execute certain commands and localhost/all ip ranges regarding the host machine are blocked.

Q: How do i change the roles or what roles are pre defined ?

A: You Can feel free to change the roles in the code itself while your inputting your bot token, the pre defined roles are as follows: 
`Root` `Moderator` `NullBot User`
