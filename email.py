
# Email Class
class Email:
    # Constructor method with instance variables email_address, subject_line, email_content and has_been_read
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    # Method to change has_been_read variable from false to true.
    def mark_as_read(self):
        has_been_read = True

# -------------------------------- Functions ---------------------------------------------------
    
# Initialization of empty Inbox list.   
Inbox = []
# Method to save emails to inbox.
def populate_inbox():
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Great work on the bootcamp!")
    email2 = Email("sender2@example.com", "Congratulations!", "Your excellent marks!")
    email3 = Email("sender3@example.com", "Important Announcement", "Please read this message carefully.")
    Inbox.extend([email1, email2, email3])
    
# Method to list emails.
def list_emails():
    for index, email in enumerate(Inbox):
        print(f"{index} {email.subject_line}")

# Method to read email on specific index.
def read_email(index):
    email = Inbox[index]
    print(f"\nEmail: {email.email_address}\nSubject: {email.subject_line}\n\n{email.email_content}\n")
    email.mark_as_read()
    print(f"Email: {email.email_address} marked as read.\n")

# Calling populate_inbox Method.
populate_inbox()

# ------------------------------------ Menu Options -------------------------------------------

while True:
    # Showing menu to user.
    print('''
-------------------------------------------------------------------------------------------
    
                                Welcome to the Email Simulator!
    
-------------------------------------------------------------------------------------------
          
    1. Read an email
    2. View unread emails
    3. Quit application
          
-------------------------------------------------------------------------------------------
''')
    # Getting user choice.
    user_choice = input("Please choose the option (1, 2, or 3): ")
    # showing list of email to user and asking which email user want to read.   
    if user_choice == "1":
        print()
        print("--------------------------------------------------------------------------")
        print()
        list_emails()
       
        print()
        email_index = int(input("Enter the index of the email you want to read: "))
        print()
        print("--------------------------------------------------------------------------")
        print()
        read_email(email_index)
    # showing unread emails to user if there is any, otherwise printing no unread emails.    
    elif user_choice == "2":
        unread_emails = [email for email in Inbox if not email.has_been_read]
        if unread_emails:
            print("Unread Emails:")
            for email in unread_emails:
                print(email.subject_line)
            print()
        else:
            print("No unread emails.\n")
    # Quiting program.        
    elif user_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Oops - incorrect input.") # in case user enter incorrect option.