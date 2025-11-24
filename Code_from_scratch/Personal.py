#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                                 ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner B:                                                                                ###
###            Juan Bismar Conde Vargas, SID 001433923                                        ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *

# FB.5.a
# we need to pass the name of the Class import as a parameter (Mail)
class Personal(Mail): # heritance 
    """ """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY
        # Modify the body
        self._body = self.add_stats()
        pass
    
    # FB.5.b
    #
    def add_stats(self):
        """ Replace Body with sender UID and add statistics """
        # Replace 'Body' with sender UID and add statistics 
        modified_body = self._body

        # Get sender UID (before @)
        sender_uid = self._frm.split("@")[0]

        # Replace Body with UID
        modified_body = modified_body.replace("Body", sender_uid)
        modified_body = modified_body.replace("body", sender_uid)
        modified_body = modified_body.lower()

        # Calculate word statistics
        words = modified_body.replace(".", " ").replace(",", " ").split()
        words = [w for w in words if w]

        word_count = len(words)

        if word_count > 0:
            total_length = sum(len(word) for word in words)
            avg_length = total_length // word_count
            longest_length = max(len(word) for word in words)
        else:
            avg_length = 0
            longest_length = 0

        # Adding the stats to the body
        stats_text = f" Stats:Word count:{word_count}, Average word length:{avg_length}, Longest word length:{longest_length}."
        modified_body += stats_text

        return modified_body
    
    # FB New method which one override show_emails
    def show_email(self):
        """ Display personal email format """
        print("PERSONAL")
        print(f"From:{self._frm}")
        print(f"Date:{self._date}")
        print(f"Subject:{self._subject}")
        print(f"Body:{self._body}")
        print(f"Read?{self._read}")
