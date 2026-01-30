class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} connected by {self.connected_by}"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by) ## Call the parent class constructor
        self.capacity = capacity # Total page capacity  
        self.remaining_pages = capacity # Pages left to print   

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"        

    def print(self, pages):
        if not self.connected:
            print("Printer is not connected.")  
            return
        if pages > self.remaining_pages: 
            print("Not enough pages remaining to print.")
        else:
            self.remaining_pages -= pages
            print(f"Printed {pages} pages. {self.remaining_pages} pages remaining.") 


printer = Printer("Office Printer", "USB", 100)
printer.print(200)
print(printer)  
printer.disconnect()
printer.print(95)