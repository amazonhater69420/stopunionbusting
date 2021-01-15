from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import os
import sys
import random
import time

print("Initializing browser...")
driver_options = webdriver.FirefoxOptions()
driver_options.add_argument("--headless")
driver = webdriver.Firefox(options=driver_options)
print("Initialized.")

fnames_filename = "fnames.txt"
lnames_filename = "lnames.txt"
states_filename = "states.txt" # i might add countries too idk
domains_filename = "domains.txt"
messagesfolder = "messages" # the first line of every message is the subject
messages = os.listdir(messagesfolder)

# Return a randomly selected line from the given file.
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

# Return a fake email address.
def generate_email(fname, lname):
    buf = ""

    # Randomly abbreviate the first or last name,
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

    # Occasionally append a random number.
    if random.random() > 0.5:
        buf += str(random.randrange(0, 999))

    # Occasionally append a state.
    if random.random() > 0.5:
        buf += "."
        buf += read_random_line(open(states_filename))

    # Occasionally make lowercase.
    if random.random() > 0.5:
        buf = buf.lower()

    # Append a random domain.
    buf += "@"
    buf += read_random_line(open(domains_filename))
    return buf

def submit():
    # Fetch the website.
    driver.get("https://www.doitwithoutdues.com/contact")
    # Ensure it was fetched correctly.
    assert "#DoItWithoutDues" in driver.title

    # Fill out the form.

    # Locate and clear out existing values in form fields.
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

    # Generate random names and emails.
    fname = read_random_line(open(fnames_filename))
    lname = read_random_line(open(lnames_filename))
    email = generate_email(fname, lname)

    # Insert names and emails into form fields.
    fname_box.send_keys(fname)
    lname_box.send_keys(lname)
    email_box.send_keys(email)

    # Select a random message to send.
    index = random.randrange(0, len(messages))
    with open(messagesfolder + "/" + messages[index]) as messagefile:
        # Read the message file.
        lines = messagefile.readlines()
        subject_box.send_keys(lines[0])
        lines = lines[1:]
        # Insert its contents into the form.
        for line in lines:
            message_box.send_keys(line)

    # Submit the form.
    submit_button.click()

# Parse command line arguments.
def parse_options():
    print("Parsing arguments...")
    parser = argparse.ArgumentParser(description='Destroy some scabs.')

    # Loop the script.
    parser.add_argument('--loop',
                    nargs='?', # Support 0 or 1 argument.
                    const=1000, # --loop without an argument is 1000 ms.
                    default=-1, # Unspecified means no looping.
                    type=int, # Convert to an integer.
                    metavar='milliseconds', # displayed in --help
                    help='run every [default=1000] ms' # displayed in --help
                )
    parser.add_argument('--report',
                    default=10, # Unspecified means every 10 iterations.
                    type=int, # Convert to an integer.
                    metavar='iterations', # displayed in --help
                    help='Report every [iterations] times.' # displayed in --help
                )

    return parser.parse_args()
    print(args.accumulate(args.integers))

# Run the script.
def main():
    try:
        print("Starting script...")
        options = parse_options()

        if options.loop == -1:
            print("Executing once...")
            submit()
            print("Complete.")
            driver.close()
        else:
            print("Executing every %d ms until cancelled." % options.loop)
            count = 0
            while True:
                time.sleep(options.loop / 1000) # Jeez why is this full seconds?
                count += 1
                submit()
                if count % options.report == 0:
                    print("Executed %d times." % count)
            driver.close()
    except KeyboardInterrupt:
        print("Script cancelled, cleaning up...")
        print("Have a nice day comrade :)")
        try:
            driver.close()
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
    main()
