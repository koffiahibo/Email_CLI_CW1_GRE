from Mail import *
from Interpreter import *
from MailboxAgent import *
from Personal import*
from Confidential import*


###################################################################################################
# COMP1811 - CW1 Outlook Simulator
# Full Test File
#
###################################################################################################


def print_header(title):
    print("\n" + "=" * 95)
    print(title)
    print("=" * 95)


# -----------------------------------------------------------
# 1. Test default Mail class
# -----------------------------------------------------------
def test_mail():
    print_header("TEST 1: Mail Class")

    m = Mail(10, "sam@gre.ac.uk", "juan@gre.ac.uk", "1/1/2025",
             "Hello", "tag0", "Body text")

    print("Mail created:")
    print(m.show_email())

    print("\nTesting setters:")
    m.flag = True
    m.read = True
    m.tag = "tag3"
    print(m.show_email())


# -----------------------------------------------------------
# 2. Test Confidential class encryption + display
# -----------------------------------------------------------
def test_confidential():
    print_header("TEST 2: Confidential Class")

    c = Confidential(20, "staff@gre.ac.uk", "student@gre.ac.uk", "2/2/2025",
                     "Bank", "conf", "Sensitive info: £500")

    print("Confidential created (should be encrypted):")
    print(c.show_email())

    print("\nDecrypt check (internal):")
    print("Encrypted:", c._body)
    print("Decrypted:", c.decrypt(c._body))


# -----------------------------------------------------------
# 3. Test Personal class statistics
# -----------------------------------------------------------
def test_personal():
    print_header("TEST 3: Personal Class")

    p = Personal(30, "me@gre.ac.uk", "friend@gre.ac.uk", "3/3/2025",
                 "Chill", "prsnl", "Let's hang out tomorrow!")

    print("Personal email created:")
    print(p.show_email())

    print("\nWord count:", p.word_count())
    print("Contains 'hang'?:", p.contains("hang"))
    print("Contains 'uni'?:", p.contains("uni"))


# -----------------------------------------------------------
# 4. Test MailboxAgent core features
# -----------------------------------------------------------
def test_mailbox_agent():
    print_header("TEST 4: MailboxAgent Core Tests")

    # Initial mailbox with two emails
    initial_msgs = [
        "ID:0\nFrom:a@gre.ac.uk\nTo:b@gre.ac.uk\nDate:1/1/2025\nSubject:s0\nTag:tag0\nBody:Hello world\nFlag:False\nRead:False\n",
        "ID:1\nFrom:c@gre.ac.uk\nTo:d@gre.ac.uk\nDate:2/1/2025\nSubject:s1\nTag:tag1\nBody:Another email\nFlag:False\nRead:False\n"
    ]

    mba = MailboxAgent(initial_msgs)

    print("SHOW initial mailbox:")
    mba.show_emails()


    # ---- TEST get_email ----
    print_header("TEST 4A: get_email")
    e0 = mba.get_email("0")
    print(e0.show_email())

    # ---- TEST mark (read/flag) ----
    print_header("TEST 4B: mark read + flag")
    mba.mark("0", "read")
    mba.mark("1", "flag")

    print(mba.get_email("0").show_email())
    print(mba.get_email("1").show_email())

    # ---- TEST move email ----
    print_header("TEST 4C: move email")
    mba.mv_email("1", "tag4")
    print(mba.get_email("1").show_email())

    # ---- TEST delete (move to bin/tag1) ----
    print_header("TEST 4D: delete email -> tag1")
    mba.del_email("0")
    print(mba.get_email("0").show_email())

    # ---- TEST filter ----
    print_header("TEST 4E: filter")
    results = mba.filter("a@gre")
    print("Filter results:", len(results))
    for e in results:
        print(e.show_email())

    # ---- TEST find ----
    print_header("TEST 4F: find emails by date")
    results = mba.find("2/1/2025")
    print("Found:", len(results))
    for e in results:
        print(e.show_email())


# -----------------------------------------------------------
# 5. Test Add Email / Class Selection / m_id generation
# -----------------------------------------------------------
def test_add_email():
    print_header("TEST 5: Add Email System")

    mba = MailboxAgent([])

    print("\nAdd general:")
    mba.add_email("x@gre.ac.uk", "y@gre.ac.uk", "9/9/2025", "s2", "tag0", "General body")
    mba.show_emails()

    print("\nAdd confidential:")
    mba.add_email("bank@gre.ac.uk", "me@gre.ac.uk", "10/10/2025", "bank", "conf", "PIN: 1234")
    mba.show_emails()

    print("\nAdd personal:")
    mba.add_email("friend@gre.ac.uk", "me@gre.ac.uk", "11/11/2025", "chill", "prsnl", "See you later!")
    mba.show_emails()

    print("\nCheck m_id uniqueness:")
    ids = [e.m_id for e in mba._mailbox]
    print("IDs =", ids, "Unique =", len(ids) == len(set(ids)))


# -----------------------------------------------------------
# 6. Test end-to-end scenario: full workflow
# -----------------------------------------------------------
def test_end_to_end():
    print_header("TEST 6: END-TO-END FULL SYSTEM TEST")

    mba = MailboxAgent([])

    # Add multiple mails
    mba.add_email("email1@gre.ac.uk", "me@gre.ac.uk", "1/5/2025", "hello", "tag0", "Body 1 test")
    mba.add_email("friend@gre.ac.uk", "me@gre.ac.uk", "1/5/2025", "yo", "prsnl", "Wanna play ball today?")
    mba.add_email("bank@gre.ac.uk", "me@gre.ac.uk", "1/5/2025", "alert", "conf", "Balance: £500")

    print("\nInitial mailbox:")
    mba.show_emails()

    print_header("Move confidential to another tag")
    mba.mv_email("2", "conf")
    print(mba.get_email("2").show_email())

    print_header("Mark email as read & flagged")
    mba.mark("0", "read")
    mba.mark("1", "flag")
    mba.show_emails()

    print_header("Filter by sender 'friend'")
    for e in mba.filter("friend"):
        print(e.show_email())

    print_header("Find by date 1/5/2025")
    for e in mba.find("1/5/2025"):
        print(e.show_email())

    print_header("Delete one email")
    mba.del_email("1")
    mba.show_emails()


# -----------------------------------------------------------
# RUN ALL TESTS
# -----------------------------------------------------------
if __name__ == "__main__":
    test_mail()
    test_confidential()
    test_personal()
    test_mailbox_agent()
    test_add_email()
    test_end_to_end()

    print("\n\nALL TESTS FINISHED.")
    print("=" * 95)

