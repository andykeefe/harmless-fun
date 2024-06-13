#  Info about this program on GitHub, at bottom of code
#  In repository harmelss-fun

from subprocess import check_output
from time import sleep, strftime

def pinger(target_host, max_tests=101):
    count = 1
    total_latency = 0
        
    with open("tests.txt", "a") as f:
        while count < max_tests:
            try:
                output = check_output(['ping', '-c', '1', target_host], universal_newlines=True)
                
                """ ping test above is properly formatted for Mac and Linux. If using Windows,
                comment out line 14 and use this instead: """
                # output = check_output(['ping', '-n', '1', target_host], universal_newlines=True)
                
                latency = output.split("time=")[-1].split(" ")[0]
                
                """ Extracts numeric latency value and strips everything else
                
                Line above works on Mac and Linux b/c they separate latency value 
                and unit with a space, i.e. time=16 ms. This is not the case on Windows,
                which uses the format time=16ms. 
                
                # If using Windows, use the following line:  """
                # latency = output.split("time=")[-1].split("ms")[0]
                
                total_latency += float(latency)
                
                # Converts latency value to a floating point number
                
                print(f"Test #{count} --> Latency: {latency} ms")
                count += 1
                sleep(0.01)
            except Exception:
                print("---------------------------------------")
                print(f"ADDRESS NOT FOUND --> {target_host}")
                print("---------------------------------------\n")
                exit(1)
                
                """  Instead of printing the lengthy error message when an
                     address is not found, we just print the target host.   """

            average_latency = round(total_latency / (max_tests - 1), 1)
        
        if count == max_tests:
            print(f"\nAverage latency: ~{average_latency} ms")
            print("-------------------------------------------------")
            print("                TEST COMPLETE")
            print("-------------------------------------------------\n")
        
        f.write("---------------------------------------------------------\n")
        f.write(f"Date: {strftime('%m/%d/%Y')}\nTo target: {target_host}")
        f.write(f"\nAverage latency: {average_latency} ms\n")
       
        """ Writes the average latency result to a file tests.txt, appending
            each successive test. So tests.txt displays 1. The date the test
            occurred  2. The target host  3. The average latency     """

if __name__ == '__main__':
    default_target = "fountaindale.org"
    target = input("Y/n: Specify a target address?\n")
    
    if target.lower() in('y', 'yes'):
        to_be_pinged = input("Enter an address to be pinged: ")
        print(f"\nTarget: {to_be_pinged}")
        pinger(to_be_pinged)
    else:
        print("Default Target: fountaindale.org")
        pinger(default_target)
