#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Interpreter program                                                            ###
###            Used to as the main program that program will manage all OutlookSim operations ###
###            automatically in response to user commands via an interactive command-line     ###
###            interface. The interpreter represents the user interacting with their mailbox. ###
### Partner A:                                                                                ###
###            Koffi Ahibo, SID001511586                                                      ###
### Partner B:                                                                                ###
###            Juan Bismar Conde Vargas, SID 001433923                                        ###
#################################################################################################
# DO NOT CHANGE FUNCTION NAMES
# replace "pass" with your own code as specified in the CW spec.

from MailboxAgent import *
import random, string

# gen_bdy Generates random text for the email body
# DO NOT MODIFY
def gen_bdy():
    """ generates email body message
        :rtype: string """
    snt = ''
    for i in range(random.randint(1,10)):
        snt += ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,10)))+' '
    return f"Body{str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."

# gen_msg generates a string of emails separated by "----"
#    Used to simulate emails in Outlook mailboxes
#    The output is a string of emails that should be used in your code as required in the CW spec.
# DO NOT MODIFY
def gen_emails():
    """ generates list of email strings
        :rtype: list """
    msgs, msg_id = [], 0
    for i in range(40):     # sent 40 email
        msg = ''
        for j in range(30): # to 30 destinations each
            msg += f"ID:{str(msg_id)}"+"\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:tag{random.randint(0, 6)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
        msgs.append(msg)
        msg_id += 1
    return msgs

# DO NOT MODIFY
def display_command_help(): # DO NOT MODIFY (used in loop function)
    """ Displays command line help """
    print('Interpreter Commands:')
    print('get <m_id> | ',      # A.1&2 Command to get and display email given email ID - e.g. get 10
          'lst | ',             # B.1 Display entire mailbox - e.g. lst
          'mv <m_id> <tag> | ', # B.2 Move email with given ID to folder indicated in given tag - e.g. mv 10 conf (i.e. change current tag to conf), then display that email
          'del <m_id> | ',      # A.3 Delete email with given ID by moving to bin - e.g. del 10 (i.e. change current tag to bin), then display that email
          'mrkr <m_id> | ',     # B.3 Mark email with given ID as Read then display that email
          'mrkf <m_id> | ',     # B.3 Mark email with given ID as Flagged then display that email
          'flt <frm> | ',       # A.4 Filter and display all emails from a given name/email address - e.g. flt email13
          'fnd <date> | ',      # B.4 Find and display all emails received on a given date - e.g. fnd 12/3/2025
          'add <email>')        # A.5&6 and B.5&6 simulate send email by adding emails to the mailbox
                                # example add prompts:
                                # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
                                # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11445. Isfffffeo afffwco sxzmp.
                                # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.

# loop repeatedly asks for command input until 'end' is entered
# DO NOT MODIFY FUNCTION NAME
# - Replace 'pass' with the code necessary to call class/methods relevant for each command
# - Completed as a group
def loop():
    mba = MailboxAgent(gen_emails())    # mba is an instance of the MailboxAgent class DO NOT MODIFY
    display_command_help()              # simply display the interpreter command-line commands as help
    line = input('mba > ')              # displays a command-line prompter for users to enter command script
    words = line.split(' ')             # separates the command from the script arguments
    command, args = words[0],words[1:]  # command is one of the interpreter script commands outlined in the help above
                                        # args is a list of arguments each command may take.
    while command != 'end':
        match command:
            # Partners A and B
            # Replace each pass statement below with a call to the relevant mba methods as described in the CW spec
            # FA/B.6
            case 'add':
                # example command prompt:
                # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
                # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11332. Isfffffeo sxzmp.
                # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.
                if len(args) == 6:
                    frm = args[0]
                    to = args[1]
                    date = args[2]
                    subject = args[3]
                    tag = args[4]
                    body_parts = " ".join(args[5:]).split("%%")
                    if len(body_parts) > 1:
                        body = body_parts[1].strip()
                    else:
                        body = body_parts[0].strip()
                    mba.add_email(frm, to, date, subject, tag, body)
                else:
                    print("Please type in format: add <from> <to> <date> <subject> <tag> %%<body>")

            case 'del':  # move email with given ID to bin folder
                # example command prompt:
                # del 10
                if len(args) == 1:
                    email = mba.get_email(args[0])
                    if email:
                        if email.tag == "bin":
                            print(f"Email with ID: {email.m_id} has already been deleted")
                        else: 
                            mba.mv_email(email.m_id, "bin")
                            print(email.show_email())
                else:
                    print("Please please type in the following format: del <email ID>, eg. \"del 10\"")
            case 'flt':
                # example command prompt:
                # flt email13
                if len(args) == 1:
                    search = args[0].lower()
                    emails_found = []
                    for email in mba._mailbox:
                        if search in email.frm.lower(): 
                            emails_found.append(email)
                    if emails_found:
                        for email in emails_found:
                            print(email.show_email())
                        print(f"\n{len(emails_found)} email(s) found from {search}")
                else:
                    print(f"No emails found from: {search}")
                    print("Please type in the following format: flt <frm>")
            case 'fnd':
                # example command prompt:
                # fnd 12/3/2025
                if len(args) == 1:
                    results = mba.find(args[0])
                    print(f"Found {len(results)} email(s) on '{args[0]}':")
                    for email in results:
                        print(email.show_email())
                    if not results:
                        print("No emamils found on this date.")
                else:
                    print("Please type in the following format: fnd <date>")

            case 'get' :                # retrieve and display email Mail object given email ID
                # example command prompt:
                # get 10
                if len(args) == 1:
                    email = mba.get_email(args[0])
                    if email != None:
                        print(email.show_email())
                    else:
                        print(f"No email found with ID: {args[0]}")
                else:
                    print("Please type in the following format: get <Email ID>, eg: \"get 23\"")
            case 'lst' :                # display entire mailbox
                # example command prompt:
                # lst
                mba.show_emails()
                
            case 'mrkr':
                # example command prompt:
                # mrkr 10
                if len(args) == 1:
                    mba.mark(args[0], "read")
                    print(mba.get_email(args[0]).show_email())
                else:
                    print("Please type in the following format: mrkr <m_id>")


            case 'mrkf':
                # example command prompt:
                # mrkf 10
                if len(args) == 1:
                    mba.mark(args[0], "flag")
                    print(mba.get_email(args[0]).show_email())
                else:
                    print("Please type in the following format: mrkf <m_id>")

            case 'mv':                  # move email with given ID to folder in given tag
                # example command prompt:
                # mv 10 conf
                if len(args) == 2:
                    email = mba.get_email(args[0])
                    if email:
                        if email.tag == args[1]:
                            print(f"The email with ID:{args[0]} is already in folder {args[1]}")
                        elif (email.tag == "conf") or (email.tag == "prsnl") :
                            print("Confidential emails and Personal emails cannot be moved to another folder")
                        elif email.tag== "bin":
                            print("Deleted emails cannot be moved to any folder")              
                        else:
                            if args[1] == "conf":
                                new_email = Confidential(email.m_id, email.frm, email.to, email.date, email.subject, "conf", email.body)
                                mba.replace_email(email, new_email)
                            elif args[1] == "prsnl":
                                new_email = Personal(email.m_id, email.frm, email.to, email.date, email.subject, "prsnl", email.body)
                                mba.replace_email(email, new_email)
                            elif args[1] == "bin":
                                del_confirm = input(
                                    "Moving email to bin folder will delete the email\n"
                                    "Do you want to continue ? (Yes/No)")
                                if del_confirm.lower() == "yes" :
                                    mba.mv_email(email.m_id, "bin")
                                    new_email = email
                                elif del_confirm.lower() == "no":
                                    print("Process cancelled")
                                else:
                                    print("No valid answer entered, proccess cancelled")
                            else:
                                new_email = email
                                mba.mv_email(new_email.m_id, args[1])
                            print(f"Email with ID: {args[0]} moved to {args[1]} folder\n")
                            print(mba.get_email(args[0]).show_email())
                            
                    else:
                        print(f"No email found with ID : {args[0]}")
                else:
                    print("Please use the following format: mv <ID> <folder_tag>")
        line = input('mba > ')
        words = line.split(' ')
        command, args = words[0], words[1:]

if __name__ == '__main__':
    loop()
