import win32com.client
session=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#session.Logon("dkumar5@yodlee.com")
inbox=session.GetDefaultFolder(6)
messages= inbox.messages
message = messages.GetFirst()
while message:
	print(message.Subject)
	message=messages.GetNext()