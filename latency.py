from subprocess import check_output
from time import sleep, strftime
from datetime import date


def pinger(target_host, max_tests=11):
    count = 1
    total_latency = 0
        
    with open("tests.txt", "a") as f:
        print("\nDate: " + strftime('%m/%d/%Y' + "\n"))

        while count < max_tests:
            output = check_output(['ping', '-c', '1', target_host], universal_newlines=True)
            latency = output.split("time=")[-1].split(" ")[0]
            total_latency += float(latency)
            print(f"Test #{count} --> Latency: {latency} ms")
            count += 1
            sleep(0.02)

            average_latency_float = total_latency / (max_tests - 1)
            average_latency = round(average_latency_float, 1)
        
        if count == max_tests:
            print(f"\nAverage latency: ~{average_latency} ms")
            print("-------------------------------------------------")
            print("                TEST COMPLETE")
            print("-------------------------------------------------\n")
        
        f.write("---------------------------------------------------------\n")
        f.write(f"Date: {strftime('%m/%d/%Y')}\nAverage latency to target: {target_host}")
        f.write(f"\n{average_latency} ms\n")


if __name__ == '__main__':
    target = input("Y/n: Specify a target address?\n")
    
    if target.lower() in('y', 'yes'):
        to_be_pinged = input("Enter an address to be pinged: ")
        print(f"\nTarget:   {to_be_pinged}")
        pinger(to_be_pinged)

    else:
        print("Default target: fountaindale.org")
        pinger("fountaindale.org")