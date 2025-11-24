#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Mail Class                                                           ###
### Partner B:                                                                                ###
###            Juan Bismar Conde Vargas, SID 001433923                                        ###
#################################################################################################

from Mail import Mail
import re

class Personal(Mail):
    """Personal mail: body is modified to include sender-based statistics on creation and tag is 'prsnl'."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        # ensure tag is 'prsnl'
        super().__init__(m_id, frm, to, date, subject, "prsnl", body)
        # modify body as required
        self._body = self.add_stats(body)

    def add_stats(self, body_text: str) -> str:
        """
        Implements FB.5.b:
        - Replace the word 'Body' in the email body message with the sender’s UID (text before '@').
        - Add statistics at the end: "Stats: Word count:X, Average word length:X, Longest word length:X."
        """
        if body_text is None:
            body_text = ""

        # get UID from sender (before '@')
        uid = self.frm.split('@')[0] if '@' in self.frm else self.frm

        # Replace first occurrence of 'Body' (case-sensitive as examples) with uid
        modified = body_text.replace("Body", uid, 1)

        # Now compute statistics over words in the modified body (strip punctuation at ends)
        # We'll consider words separated by whitespace and remove trailing punctuation from words.
        words = re.findall(r"\b\w+\b", modified)
        word_count = len(words)
        if word_count == 0:
            avg_len = 0
            max_len = 0
        else:
            lengths = [len(w) for w in words]
            avg_len = sum(lengths) // word_count  # integer average as spec example
            max_len = max(lengths)

        stats = f" Stats:Word count:{word_count}, Average word length:{avg_len}, Longest word length:{max_len}."

        # Ensure a single space before stats (if body ends with punctuation ensure spacing)
        if not modified.endswith(' '):
            modified = modified.rstrip() + stats
        else:
            modified = modified + stats

        return modified

    def show_email(self):
        """
        Display ONLY Personal Mail objects in the required format.
        The spec shows a special format; provide a compact display highlighting modified body.
        """
        return (f"PERSONAL MAIL\n"
                f"ID: {self.m_id}\n"
                f"From: {self.frm}\n"
                f"To: {self.to}\n"
                f"Date: {self.date}\n"
                f"Subject: {self.subject}\n"
                f"Tag: {self.tag}\n"
                f"Body: {self._body}\n"
                f"Flag: {self.flag}\n"
                f"Read: {self.read}\n"
                f"{type(self).__name__}")

    # FB.7 display_psnl required method
    def display_psnl(self, mailbox):
        """
        Displays the string "Persontology" followed by a pretty print of the mailbox sorted by date descending.
        We'll print "Persontology" exactly and then the sorted list.
        Dates are in format D/M/YYYY as per gen_emails; we'll parse them naïvely to sort.
        """
        print("Persontology")
        def parse_date(dstr):
            try:
                parts = dstr.split('/')
                if len(parts) == 3:
                    day = int(parts[0])
                    month = int(parts[1])
                    year = int(parts[2])
                    return (year, month, day)
            except Exception:
                pass
            return (0,0,0)
        sorted_m = sorted(mailbox, key=lambda e: parse_date(e.date), reverse=True)
        for e in sorted_m:
            print(e.show_email())
