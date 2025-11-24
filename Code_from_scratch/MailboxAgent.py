#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            This file introduces the MailboxAgent class which instances store and manage   ###
### Mail objects                                                                              ###
### Partner A:                                                                                ###
###            Koffi Ahibo, SID001511586                                                      ###
### Partner B:                                                                                ###
###            Juan Bismar Conde Vargas, SID 001433923                                        ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, m_id):
        """ this method loops through mailbox and return the email 
            corresponding to the id provided 
        """
        for email in self._mailbox:
            if email.m_id == m_id :
                return email
        return None
    # FA.3
    # 
    def del_email(self, m_id):
        """  """
        for email in self._mailbox:
            if email.m_id == m_id:
                email._tag = "bin"
                break

    # FA.4
    # 
    def filter(self, frm):
        """  """
        emails = []
        for email in self._mailbox:
            if email._frm == frm:
                emails.append(email)
        return emails

    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        """ Display all emails in table format """
        # Display all emails in table format base
        print(f"{"Id:":<4}|{"from:":<20}|{"To:":<20}|{"Date:":<13}|{"subject:":<11}|{"Tag:":<7}|{"Body:"}")
        
        for email in self._mailbox:
            print(f"{email.m_id:<4}|{email.frm:<20}|{email.to:<20}|{email.date:<13}|{email.subject:<11}|{email.tag:<7}|{email.body}")
        

    # FB.2
    # 
    def mv_email(self, m_id, tag):
        """ Move email to different forder """
        for email in self._mailbox:
            if email.m_id == m_id:
                email.tag = tag
                print(f"Email {m_id} moved to: '{tag}'")
                email.show_email()
                return f"Email {m_id} moved to: '{tag}'"
        print(f"Email with ID {m_id} not found.")


    # FB.3
    # 
    def mark(self, m_id, m_type):
        """ Mark email as read or flagged """
        for email in self._mailbox:
            if email.m_id == m_id:
                if m_type.lower() == "read":
                    email.read = True
                    print(f"Email {m_id} marked as read:")
                elif m_type.lower() == 'flag':
                    email.flag = True
                    print(f"Email {m_id} marked as flagged:")
                email.show_email()
                return
        print(f"Email with ID {m_id} not found.")

    # FB.4
    # 
    def find(self, date):
        """ Find all emails from specfic date """
        results = []
        for email in self._mailbox:
            if email.date == date:
                results.append(email)
        return results

    # FB.5
    # 
    def sort_from(self):
        """  """

        pass


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        """ Add new email to mailbox """
        # code must generate unique m_id
        if self.__gen_mailbox:
            max_id = max([int(email.m_id) for email in self._mailbox])
            new_id = str(max_id + 1)
        else:
            new_id = 0
        
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                new_email = Confidential(new_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_email)
                print(f"Confidential email added with ID '{new_id}'")
                #new_email.show_email()
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                new_email = Personal(new_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_email)
                print(f"Personal email added with ID '{new_id}'")
                #new_email.show_email()

            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                new_email = Mail(new_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_email)
                print(f"Email added with ID '{new_id}'")
                #new_email.show_email()
                
    def replace_email(self, old_email, new_email):
        for i in range(len(self._mailbox)):
            if self._mailbox[i].m_id == old_email.m_id:
                self._mailbox[i] = new_email
                break