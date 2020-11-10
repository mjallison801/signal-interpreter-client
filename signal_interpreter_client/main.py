# main.py assignment 2

from server_communication_handler import post_message
import argparse

in_parser = argparse.ArgumentParser()
in_parser.add_argument("--signal", action="store", help="payload to be sent to the server")

payload = in_parser.parse_args()

sig_dict = {'signal' : payload.signal}

if __name__ == "__main__":
    url_name = "http://127.0.0.1:5000/"
    srvr_response = post_message(url_name,sig_dict)
    print(srvr_response)