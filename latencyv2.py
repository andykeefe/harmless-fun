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
                latency = output.split("time=")[-1].split(" ")[0]
                total_latency += float(latency)
                print(f"Test #{count} --> Latency: {latency} ms")
                count += 1
                sleep(0.01)
            except Exception:
                print("---------------------------------------")
                print(f"ADDRESS NOT FOUND --> {target_host}")
                print("---------------------------------------\n")
                exit(1)

            average_latency_float = total_latency / (max_tests - 1)
            average_latency = round(average_latency_float, 1)
        
        if count == max_tests:
            print(f"\nAverage latency: ~{average_latency} ms")
            print("-------------------------------------------------")
            print("                TEST COMPLETE")
            print("-------------------------------------------------\n")
        
        f.write("---------------------------------------------------------\n")
        f.write(f"Date: {strftime('%m/%d/%Y')}\nTo target: {target_host}")
        f.write(f"\nAverage latency: {average_latency} ms\n")


if __name__ == '__main__':
    target = input("Y/n: Specify a target address?\n")
    
    if target.lower() in('y', 'yes'):
        to_be_pinged = input("Enter an address to be pinged: ")
        print(f"\nTarget:   {to_be_pinged}")
        pinger(to_be_pinged)
    else:
        print("Default target: fountaindale.org")
        pinger("fountaindale.org")
