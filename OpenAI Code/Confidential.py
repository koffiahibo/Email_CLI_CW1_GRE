#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Mail Class                                                       ###
### Partner A:                                                                                ###
###            Koffi Ahibo, SID001511586                                                      ###
#################################################################################################

from Mail import Mail
import string

class Confidential(Mail):
    """Confidential mail: body is encrypted on instantiation and tag is 'conf'."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        # ensure tag is 'conf' for Confidential objects
        super().__init__(m_id, frm, to, date, subject, "conf", body)
        # encrypt _body on creation
        self._body = self.encrypt(body)

    def encrypt(self, body_text: str) -> str:
        """
        Encryption algorithm (as per spec):
        - Each alphabetic letter becomes its alphabet position * number_of_words_in_original_body
          (concatenated as digits)
        - Full stops (.) remain unchanged
        - Numbers (digits 0-9) are replaced with corresponding alphabet letters where:
            1 -> a, 2 -> b, ... 9 -> i, 0 -> j
        - Non-alphanumeric characters (except '.') will be left as-is.
        """
        if body_text is None:
            return ""

        # Count words (split by whitespace)
        words = [w for w in body_text.split() if w.strip() != ""]
        word_count = max(1, len(words))

        # mapping digits to letters per spec example (1->a ... 9->i, 0->j)
        digit_to_letter = {str(i): chr(ord('a') + (i - 1) % 26) for i in range(1, 10)}
        digit_to_letter['0'] = 'j'

        result_parts = []
        for ch in body_text:
            if ch == '.':
                result_parts.append('.')
            elif ch.isalpha():
                # position in alphabet (a=1..z=26)
                pos = ord(ch.lower()) - ord('a') + 1
                # multiply by number of words
                result_parts.append(str(pos * word_count))
            elif ch.isdigit():
                # replace digit by corresponding alphabet letter
                result_parts.append(digit_to_letter.get(ch, ch))
            else:
                # keep other characters (spaces will be handled by joining afterwards)
                result_parts.append(ch)
        # join everything preserving spacing and punctuation
        return "".join(result_parts)

    def show_email(self):
        """
        Display ONLY Confidential Mail objects in the required format.
        The spec shows a 'mailto:email1@gre.ac.uk' style. We'll include full pretty print but with header
        indicating it's confidential and preserving the encrypted body.
        """
        return (f"mailto:{self.to}\n"
                f"ID: {self.m_id}\n"
                f"From: {self.frm}\n"
                f"Date: {self.date}\n"
                f"Subject: {self.subject}\n"
                f"Tag: {self.tag}\n"
                f"Encrypted Body: {self._body}\n"
                f"Flag: {self.flag}\n"
                f"Read: {self.read}\n")
    
    # FA.7 display_conf required method
    def display_conf(self, mailbox):
        """
        Displays the header string requested followed by a pretty print of the mailbox sorted by 'from' ascending.
        The spec says: display the string "S mur fiology encrypted" followed by a pretty print.
        We'll print exactly that string and then the sorted list.
        """
        print("S mur fiology encrypted")
        # sort mailbox by frm (ascending)
        sorted_m = sorted(mailbox, key=lambda e: e.frm)
        for e in sorted_m:
            print(e.show_email())

