
import smtplib  
import logging
logger = logging.getLogger(__name__)
def sendmail(subject):
  try:
        logger.info('sending email')
        conn =smtplib.SMTP('smtp-mail.outlook.com',587)  
        type(conn)  
        conn.ehlo()  
        conn.starttls()  
        conn.login('narsagoud.pulla@outlook.com','Automateme@9')  
        conn.sendmail('narsagoud.pulla@outlook.com','urs.ravis@gmail.com','subject:'+ subject)  
        conn.quit() 
  except Exception as ex:
          logger.error(ex)
