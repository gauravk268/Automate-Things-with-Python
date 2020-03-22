#! python3 
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',             
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',             
    'luggage': '12345'}

account = input()    # first command line arg is the account name
account = account.lower()

if account in PASSWORDS:    
    # pyperclip.copy(PASSWORDS[account])    
    print('Password for ' + account + ' copied to clipboard.') 
else:    
    print('There is no account named ' + account)
