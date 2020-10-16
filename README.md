# WABot
A Whatsapp Bot that can be used to manage Whatsapp chats

It is composed of a Python class "WABot" that has methods that can be used to manage and possibly automate Whatsapp chats.
Made using Selenium and the webdriver for Chrome which use Whatsapp Web.

HOW TO USE:
- modify the path on the options with your user path of the WebDriver for easy access without scanning QR code every time.

SIMPLE EXAMPLE OF USE (using terminal and ipython)
* $ ipython (open iypthon)
* In [1]: from WABot import WABot
* In [2]: WA = WABot()
* Connection was successul
* In [3]: WA.send_msg("John","Hello")
* Message Hello was sent to John
* In [4]: WA.delete_last_msg("John")
* Last message from John's chat was deleted
* In [5]: WA.close_chat()"""
