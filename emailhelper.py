
import smtplib  
def sendmail(subject):
        conn =smtplib.SMTP('smtp-mail.outlook.com',587)  
        type(conn)  
        conn.ehlo()  
        conn.starttls()  
        conn.login('narsagoud.pulla@outlook.com','Automateme@9')  
        conn.sendmail('narsagoud.pulla@outlook.com','urs.ravis@gmail.com',subject)  
        conn.quit() 
