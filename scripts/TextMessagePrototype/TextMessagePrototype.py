import smtplib
content="Certified monkey moment in your house"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender='primatedetection@gmail.com'
recipient='9789792742@vtext.com'
mail.login( 'primatedetection@gmail.com', 'M0nk3y1ng@r0und' )
header='To:'+recipient+'\n'+'From:'\
+sender+'\n'+'subject:Monkey Event\n'
content=header+content
mail.sendmail(sender,recipient, content)
mail.close()

