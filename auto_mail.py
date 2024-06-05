import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email(sender_mail: str, email_app_pswd: str,
               to_addrs: list,  body: str, 
               output_file_name: str, subject: str,
               cc_addrs: list = None):
    """
    sender_mail: email address the code will use to send
    email_app_pswd: email app password
    to_addrs: list of email address to send to
    body: body of the email to send
    output_file_name: excel file to send as attachment
    subject: email subject
    cc_addrs: cc addresses [Optional]
    """
    # Set the email server and login credentials
    with smtplib.SMTP('smtp.gmail.com', 587) as mail_server:
        mail_server.starttls()
        mail_server.login(sender_mail, email_app_pswd)
 
        from_addr = sender_mail
        
        # Create the email
        msg = MIMEMultipart()
        msg['To'] = ', '.join(to_addrs)  
        msg['From'] = from_addr
        msg['Subject'] = subject

        # Add CC recipients if provided
        # if cc_addrs:
        #     msg['Cc'] = ', '.join(cc_addrs)
        # else:
        #     cc_addrs = []

        msg.attach(MIMEText(body, 'plain'))

        file_path_1 = f'{output_file_name}.xlsx' 
        with open(file_path_1, 'rb') as binary_pdf_1:

            # Add the binary file to the email
            payload = MIMEBase('application', 'octate-stream', Name=file_path_1)
            payload.set_payload((binary_pdf_1).read())


            # Encode the binary into base64
            encoders.encode_base64(payload)
            # Add header with pdf name
            payload.add_header('Content-Decomposition', 'attachment', filename=file_path_1)
            msg.attach(payload)


            # all_recipients = to_addrs + cc_addrs
            all_recipients = to_addrs

            # Send the email
            mail_server.sendmail(from_addr, all_recipients, msg.as_string())