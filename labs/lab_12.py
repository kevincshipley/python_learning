class computer:
    def __init__(self, processor, ram):
        # creating an instance variable name processor
        # and assigning it the value of the parameter named processor
        self.processor = processor
        
        # create an instance variable named ram
        # and assign it the value of the parameter named ram
        self.ram = ram

    # defining a setter for the processor instance variable
    def set_processor(self, processor):
        self.processor = processor

    # define a setter for the ram instance variable
    def set_ram(self, ram):
        self.ram = ram

    # defining a getter for the processor instance variable
    def get_processor(self):
        return self.processor

    # define a getter for the ram instance variable
    def get_ram(self):
        return self.ram


# Construct a computer object
myPC = computer("3.6 GHz", "16 GB")

# Use getters to display the processor and ram for the computer you constructed
print("My computer's processor is:", myPC.get_processor())
print("My computer's RAM is:", myPC.get_ram())
