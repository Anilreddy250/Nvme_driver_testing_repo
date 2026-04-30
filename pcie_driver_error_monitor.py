import subprocess
import os

def monitor_pcie_error():
    #dmesg -w waits for new messages (tails the log)
    cmd = ["dmesg", "-w"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Monitoring systems logs for PCIe AER Fatal Errors..")
    try:
        for line in process.stdout:
            if "AER" in line and "Fatal Error" in line:
                print(f"CRITICAL: {line.strip()}")
                trigger_reboot()
    except KeyboardInterrupt:
        process.terminate()
    
def trigger_reboot():
    print("Initiating emergency systems reboot...")
    os.system("sudo reboot")
if __name__ == "__main__":
    monitor_pcie_error()    

#BaseNVNeCommand
#build_dw0()
# execute()
#multiprocessing
#threading
#mmap
#ctypes
#volatile
#memoryview
#numpy