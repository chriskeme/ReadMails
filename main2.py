import poplib
from email import parser
import time

def seeit():
    username = 
    password =


    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(username)
    pop_conn.pass_(password)
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:a
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    for message in messages:
        print message['subject']
        var = message._payload[0]._payload
    pop_conn.quit()


starttime=time.time()

while True:
    k = 2
    print "tick"
    seeit()
    time.sleep(k)