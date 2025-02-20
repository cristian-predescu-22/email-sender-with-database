import smtplib
from PyQt5 import QtWidgets, QtGui

# Create the main window
app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()

# Create the input fields
to_label = QtWidgets.QLabel("To:")
to_field = QtWidgets.QLineEdit()
subject_label = QtWidgets.QLabel("Subject:")
subject_field = QtWidgets.QLineEdit()
body_label = QtWidgets.QLabel("Body:")
body_field = QtWidgets.QTextEdit()

# Create the send button
send_button = QtWidgets.QPushButton("Send")

# Create the layout
layout = QtWidgets.QFormLayout()
layout.addRow(to_label, to_field)
layout.addRow(subject_label, subject_field)
layout.addRow(body_label, body_field)
layout.addRow(send_button)
window.setLayout(layout)

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR EMAIL", "KEY")

# Send the email when the button is clicked
def on_click():
    to = to_field.text()
    subject = subject_field.text()
    body = body_field.toPlainText()
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("YOUR EMAIL", to, msg)

send_button.clicked.connect(on_click)

# Show the window
window.show()
app.exec_()

# Disconnect from the server
server.quit()






# import smtplib
# import datetime


# # Set up the SMTP server
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("cristipredescu21@gmail.com", "evucftwpbldylwty")

# # Compose email
# to = "cristipredescu21@yahoo.com"
# subject = "Sample Subject"
# body = """Sample Text"""


# # Send email
# msg = f"Subject: {subject}\n\n{body}"
# server.sendmail("cristipredescu21@gmail.com", to, msg)
# x = datetime.datetime.now()

# # Disconnect from the server
# server.quit()

# with open("Email_Text.txt", "a") as file_object:
#     # Append 'email' at the end of file
#     file_object.write(str(x) + '\n')
#     file_object.write(to + '\n')
#     file_object.write(subject + '\n')
#     file_object.write(body + '\n' + '\n')
   