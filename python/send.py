import smtplib
import copy
import random 
from random import shuffle
import math


def send_message(user, pw, rec, subject, body):
    gmail_user = user
    gmail_pwd = pw
    FROM = user
    TO = rec if type(rec) is list else [rec]
    SUBJECT = subject
    TEXT = body
    
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.login(gmail_user, gmail_pwd)  
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
    server_ssl.sendmail(FROM, TO, message)
    #server_ssl.quit()
    server_ssl.close()
    print 'successfully sent the mail'

class Santas:
    def __init__(self, name, number, wshlist):
        self.name = name
        self.number = number
        self.wshlist = wshlist
        self.rec_from = [] #should only be size 2
        self.send_to = []
    
    @staticmethod
    def santasDone(santas):
        print "in checker"
        done = True
        for i in range(len(santas)):
            if len(santas[i].send_to) != 2:
                done=False
                break
            if len(santas[i].rec_from) !=2:
                done=False
                break
        return done

    
    @staticmethod
    def randomizeList(santas):
	    #will need to make a list and make sure it is correct before
        #randomly select one person from the list, make a list with out them
        #select two from the list 
        print "In randomizer"
        to_shuffle = copy.deepcopy(santas)
        chances= math.factorial(len(santas))
        for i in range(chances/2):
            shuffle(to_shuffle)
            #edge cases: person sending twice to one, person receiving from same twice
            curSanta = to_shuffle.pop()
            if len(curSanta.send_to) == 2:
              to_shuffle.append(curSanta)
              continue
            else: 
                for i in range(len(to_shuffle)):
                    givTo = to_shuffle.pop()
                    if len(givTo.rec_from) == 2:
                        to_shuffle.insert(0,givTo)
                        continue
                    elif len(givTo.rec_from) == 1:
                        if givTo.rec_from[0] == curSanta.name:
                            to_shuffle.insert(0,givTo)
                            continue
                        else:
                            givTo.rec_from.append(str(curSanta.name))
                            curSanta.send_to.append(str(givTo.name))
                            to_shuffle.insert(0,givTo)
                            to_shuffle.append(curSanta)
                            break
                    elif len(givTo.rec_from) == 0:
                        givTo.rec_from.append(str(curSanta.name))
                        curSanta.send_to.append(str(givTo.name))
                        to_shuffle.insert(0,givTo)
                        to_shuffle.append(curSanta)
                        break
                if Santas.santasDone(to_shuffle):
                    break;
                else:
                    continue
        if Santas.santasDone(to_shuffle):
            print "Success"
            return to_shuffle
        else:
            print "FAILED"
            False



def readSantas(listPeople):
    ppl = open(listPeople, 'rb')
    santas = []
    for line in ppl:
        line = line[:len(line)-1]
        array = line.split(" ")
        name = array.pop(0)
        number = array.pop(0)
        wshlist = copy.deepcopy(array)
        santas.append(Santas(name,number,wshlist))
    return santas

def Run():
    print "STAR"
    a = Santas('1','1',[])
    b = Santas('2','2',[])
    c = Santas('3','3',[])
    d = Santas('4','4',[])
    e = Santas('5','5',[])
    san = [a,b,c,d,e]
    for s in san:
        print "Santa: %s \n" %(s.name)
    l = Santas.randomizeList(san)
    if l == False:
        print "Failed"
    else:
        for s in l:
            print "Santa: %s , send: %s, %s , rec : %s , %s \n"  %(s.name, s.send_to[0], s.send_to[1], s.rec_from[0], s.rec_from[1])
