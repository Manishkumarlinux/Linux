#Object-oriented Python disk-monitoring script 
from subprocess import  Popen, PIPE
import re

class DiskMonitor():
    """Disk Monitoring Class"""
    def __init__(self, pattern="2[0-9]%", message="CAPACITY WARNING", cmd= "df -h"):
        self.pattern = pattern
        self.message = message
        self.cmd = cmd
     
    def disk_space(self):
        """Disk space capacity flag method"""
        ps = Popen(self.cmd, shell=True, stdout=PIPE, stderr=PIPE)
        output_lines = ps.stdout.readlines()
        for line in output_lines:
            line = line.strip()
            if re.search(self.pattern, line):
                print "%s %s" % (self.message)
                
#if __name__ == "__main__":
#    d = DiskMonitor()
#    d.disk_space()                
#using inheritance   
class MyDiskMonitor(DiskMonitor):
    """Customized Disk Monitoring Class"""
    
    def disk_space(self):
        ps = Popen(self.cmd, shell=True, stdout=PIPE, stderr=PIPE)
        print "DISK REPORT"
        print ps.stdout.read()
        
if __name__ == "__main__":
    d = MyDiskMonitor()
    d.disk_space()        
                  
        
