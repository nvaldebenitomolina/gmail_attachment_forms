#!/usr/bin/env python3
# -- coding: utf-8 --

import imaplib
import email
import re 
from unidecode import unidecode
import os
import shutil 

server = 'smtp.gmail.com'
user = os.environ['EMAIL']
password = os.environ['PASSWORD']
subject = 'DIPLOMADO SOBRE '#subject line of the emails you want to download attachments from

def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    

    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

#download attachments from all emails with a specified subject line
def downloadAttachments(subject):
    m = connect(server, user, password)
    m.select("Inbox")
    p = re.compile(r'Server Status')

    typ, msgs = m.search(None, '(SUBJECT "' + subject + '")')
    msgs = msgs[0].split()
    print('Processing')
    
    for num in msgs:
        print(num)
        print('Processing ')
        
        typ, data = m.fetch(num,'(RFC822)')
        for response_part in data:
             if isinstance(response_part, tuple):
                 original = email.message_from_bytes(response_part[1])
                 print('From: '+original['From'])
                 print('Subject: '+original['Subject'])
                 if original['Subject'] == '=?UTF-8?Q?Re=3A_DIPLOMADO_SOBRE_ACCI=C3=93N_CLIM=C3=81TICA_Y_GESTI=C3=93N_MU?==?UTF-8?Q?NICIPAL?=':
                     print('Not available RE: DIPLOMADO')
                 else:
                     if original.is_multipart():
                         # Quick hack, should probably properly recurse
                         message =  original.get_payload()[0].get_payload()
                     else:
                         message = original.get_payload()
                     try:
                         name=message.split('Nombres: ')[1].split('Nacionalidad: ')[0].split(' ')[0].lower()
                         last_name=message.split('Apellidos: ')[1].split('Nombres: ')[0].split(' ')[0].lower()
                         print(unidecode(name+'_'+last_name))
                         cwd = os.getcwd()
                         outputdir=cwd+'/'+unidecode(name+'_'+last_name)
                         print(outputdir)
                         try:
                            os.mkdir(outputdir)
                         except:
                            print('exist')
                         with open(outputdir+'/'+unidecode(name+'_'+last_name)+'.txt', 'w') as out:
                            out.write(message)
                            out.close()
                         downloaAttachmentsInEmail(m, num, outputdir)
                     except:
                        print('-----------------------------------------')
                        print('Error list index out of range RE: subject')
                        print('-----------------------------------------')
    shutil.rmtree(cwd+'/'+'nancy_valdebenito/')
    shutil.rmtree(cwd+'/'+'[text*_[text*/')
    
    # for emailid in msgs:
    #     downloaAttachmentsInEmail(m, emailid, outputdir)

downloadAttachments(subject)

