import smtplib
s=smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("souju1902@gmail.com","******")
message="""\
Subject: Testing mail

Hello Have a good day!!
"""

s.sendmail("souju1902@gmail.com","souju1902@gmail.com",message)
print ("success") 
s.quit()
