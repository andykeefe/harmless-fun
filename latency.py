#  Information about this program at the bottom of this page. 

from subprocess import check_output
from time import sleep, strftime
from datetime import date


def pinger(target_host, max_tests=11):
    count = 1
    total_latency = 0
    
    with open("tests.txt", "a") as f:
        while count < max_tests:
            output = check_output(['ping', '-c', '1', target_host], universal_newlines=True)
            
            """ 

                check_output runs a command with some arguments. In this case,
                we run 'ping -c 1 target_host', meaning we send one packet for each
                command, storing the result in a newline to variable 'output'

            """
            
            latency = output.split("time=")[-1].split(" ")[0]
            # latency = output.split('time=")[-1].split("ms")[0]

            """

                This is an elegant way to extract only the latency value, without
                any other extraneous information. The output variable will be full
                of full ping outputs, such as:
                        
                        Reply from 10.0.0.1: bytes=32 time=7 ms TTL=53
                
                Note that the output for ping is different on Linux vs Windows, the 
                main difference (for the purpose of this program) being that Linux 
                automatically puts a space after the latency value and Windows doesn't.
                
                Comment out line 24 and uncomment line 25 if using Windows.

            """
            
            total_latency += float(latency)
            print(f"Test #{count} --> Latency: {latency} ms")
            count += 1
            sleep(0.01)
        
        average_latency = round(total_latency / (max_tests - 1), 1)
        
        if count == max_tests:
            print(f"\nAverage latency: ~{average_latency} ms")
            print("-------------------------------------------------")
            print("                TEST COMPLETE")
            print("-------------------------------------------------\n")
        
        f.write("---------------------------------------------------------\n")
        f.write(f"Date: {strftime('%m/%d/%Y')}\nTtarget: {target_host}")
        f.write(f"\nAverage latency: {average_latency} ms\n")


if __name__ == '__main__':
    target = input("Y/n: Specify a target address?\n")
    
    if target.lower() in('y', 'yes'):
        to_be_pinged = input("Enter an address to be pinged: ")
        print(f"\nTarget: {to_be_pinged}")
        pinger(to_be_pinged)

    else:
        print("Default target: fountaindale.org")
        pinger("fountaindale.org")

"""

        This is a program for testing the latency of a network. To give it more malleability,
    it asks the user if they'd like to input an address to target. This functionality could
    be useful if there are suspected network disruptions occuring. Testing the latency of your
    router, for example, could give basic information on its performance. 
    
        The default is fountaindale.org, so if the user prompts anything but "yes" in response 
    to the request for a target, it will ping that. 

        This test runs a simple ping scan, stores the latency values, and calculates an average
    latency over the course of the max_tests variable. It's currently set to 50 tests, but can
    be change to any value. For example, if you wanted to run 100 tests, the max_tests variable
    can be set to 101. 

        Every latency value is printed, as well as the average latency. For record keeping, we store
    the date, target address, and average latency of the test. 

"""
