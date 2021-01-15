from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import random
import time

driver = webdriver.Firefox()

fnames_filename = "fnames.txt"
lnames_filename = "lnames.txt"
states_filename = "states.txt" # i might add countries too idk
domains_filename = "domains.txt"
messagesfolder = "messages" # the first line of every message is the subject
messages = os.listdir(messagesfolder)

def read_random_line(file):
    line_num = 0
    selected_line = ""

    while 1:
        line = file.readline()
        if not line: break
        line_num = line_num + 1
        if random.uniform(0, line_num) < 1:
            selected_line = line
    file.close()
    return selected_line.rstrip()

# return a fake email address
# eventually i want to get these from something like 10minutemail.com
def generate_email(fname, lname):
    buf = ""
    if random.random() > 0.5:
        buf += fname[0:1]
        if random.random() > 0.5:
            buf += "."
        buf += lname

    else:
        buf += fname
        if random.random() > 0.5:
            buf += "."
        buf += lname[0:1]

    if random.random() > 0.5:
        buf += str(random.randrange(0, 999))

    if random.random() > 0.5:
        buf += "."
        buf += read_random_line(open(states_filename))

    if random.random() > 0.5:
        buf = buf.lower()

    buf += "@"
    buf += read_random_line(open(domains_filename))
    return buf
    

def submit():
    driver.get("https://www.doitwithoutdues.com/contact")
    assert "#DoItWithoutDues" in driver.title

    fname_box = driver.find_element_by_name("fname")
    fname_box.clear()
    lname_box = driver.find_element_by_name("lname")
    lname_box.clear()
    email_box = driver.find_element_by_name("email")
    email_box.clear()
    subject_box = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/main/section/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/form/div[1]/div[2]/input") # this will likely change if they ever update the page
    subject_box.clear()
    message_box = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/main/section/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/form/div[1]/div[3]/textarea")
    message_box.clear()
    submit_button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/main/section/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/form/div[2]/input")

    fname = read_random_line(open(fnames_filename))
    lname = read_random_line(open(lnames_filename))
    email = generate_email(fname, lname)

    fname_box.send_keys(fname)
    lname_box.send_keys(lname)
    email_box.send_keys(email)

    index = random.randrange(0, len(messages))
    with open(messagesfolder + "/" + messages[index]) as messagefile:
        lines = messagefile.readlines()
        subject_box.send_keys(lines[0])
        lines = lines[1:]
        for line in lines:
            message_box.send_keys(line)
    submit_button.click()

if __name__ == "__main__":
    try:
        submit()
        driver.close()
    except KeyboardInterrupt:
        print("Exiting")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
