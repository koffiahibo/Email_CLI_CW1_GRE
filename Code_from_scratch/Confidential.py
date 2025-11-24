#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            Koffi Ahibo, SID001511586                                                      ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FA.5.a
class Confidential(Mail):
    """ """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
        super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
        self._body = self.encrypt() # such that the encrypted body is reassigned to our old body
        self._tag = "conf"

# FA.5.b
    def encrypt(self):
        """ """
        body = self.body
        body_length = len(body.split(" "))
        encrypt_body = []
        for character in body:
            if character.isalpha() : #To check if the character is a letter or not
                character = body_length * int(ord(character.lower()) - 96)
            elif character.isdigit(): #To check if the character is a digit or not
                character = chr(int(character) + 96 )
            else:  # ensures that any other character (like quotes for.eg) are left unchanged
                character = character
            encrypt_body.append(str(character))
        return "".join(encrypt_body)
# FA.5.c modified show_email() method overriding the one in Mail class
    def show_email(self):
        return (f"CONFIDENTIAL \n"
            f"From:{self.frm}\n"
            f"Date:{self.date} \n"
            f"Subject:{self.subject} \n"
            f"Encrypted body message:{self.body} \n"
            f"Flagged?{self.flag} \n")
