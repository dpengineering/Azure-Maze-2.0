from Email import Email


mail = Email('kineticmaze@gmail.com', 'kineticmaze7266!')

while True:
    mail.checkForEmailConstantly(target_body="scores", response_body="test",
                                     response_subject="Hello from the Kinetic Maze! Here are your top scores: ")