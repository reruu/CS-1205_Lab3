import time
from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self, tool_name, material, weight):
        self.tool_name = tool_name
        self.material = material
        self.weight = weight

    @abstractmethod
    def use_tool(self):
        pass
    
    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 

    # getter/setter for weight (para di maging negative)
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("Weight must be positive.")

class Hammer(Tool):
    def __init__(self, tool_name, material, weight, hammer_type):
        super().__init__(tool_name, material, weight)
        self.hammer_type = hammer_type
        self.nails_driven = 0  # Optional: to track how many nails

    def use_tool(self):
        return f"Using {self.tool_name}, a {self.hammer_type} hammer weighing {self.weight}kg."

    def add_nail(self):
        self.nails_driven += 1
        return f"Nail driven using {self.tool_name}. Total nails: {self.nails_driven}"

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 

    
class Chisel(Tool):
    def __init__(self, tool_name, material, weight, chisel_type):
        super().__init__(tool_name, material, weight)
        self.chisel_type = chisel_type

    def use_tool(self):
        return f"Using {self.tool_name}, a {self.chisel_type} chisel weighing {self.weight}kg."

    def sharpen(self):
        return f"{self.tool_name} has been sharpened."

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 

    
    
class Screwdriver(Tool):
    def __init__(self, tool_name, material, weight, screwdriver_type):
        super().__init__(tool_name, material, weight)
        self.screwdriver_type = screwdriver_type

    def use_tool(self):
        return f"Using {self.tool_name}, a {self.screwdriver_type} screwdriver weighing {self.weight}kg."
    
    def change_bit(self, new_bit):
        return f"Changed the bit of {self.tool_name} to {new_bit}."

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 
    
class Wrench(Tool):
    def __init__(self, tool_name, material, weight, wrench_type):
        super().__init__(tool_name, material, weight)
        self.wrench_type = wrench_type

    def use_tool(self):
        return f"Using {self.tool_name}, an {self.wrench_type} wrench weighing {self.weight}kg."
    
    def adjust(self, new_size):
        return f"Adjusted the size of {self.tool_name} to {new_size}."

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 
    
class Handsaw(Tool):
    def __init__(self, tool_name, material, weight, saw_type):
        super().__init__(tool_name, material, weight)
        self.saw_type = saw_type

    def use_tool(self):
        return f"Using {self.tool_name}, a {self.saw_type} saw weighing {self.weight}kg."
    
    def cut(self):
        return f"{self.tool_name} has cut through the material."

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 
    
class Sandpaper(Tool):
    def __init__(self, tool_name, material, weight, grit_size):
        super().__init__(tool_name, material, weight)
        self.grit_size = grit_size

    def use_tool(self):
        return f"Using {self.tool_name}, a sandpaper with grit size {self.grit_size} weighing {self.weight}kg."
    
    def smooth(self):
        return f"{self.tool_name} has smoothed the surface."

    def clean_tool(self):
        return f"{self.tool_name} made of {self.material} has been cleaned."
    
    def return_tool(self):
        return f"Returning {self.tool_name} to the toolbox." 
  
def main():
    print("Opening toolbox...")
    time.sleep(2)  # Simulate time taken to open toolbox
    print("Toolbox opened.")
    time.sleep(.5)
    print("~~~~~~~~~~~~~~TOOLS~~~~~~~~~~~~~~~~~")
    hammer_tool = Hammer("Hammer", "steel", 1.5, "claw type")
    print(hammer_tool.use_tool())
    time.sleep(.5)
    print(hammer_tool.add_nail())
    time.sleep(.5)
    print(hammer_tool.add_nail())  #drive another nail
    time.sleep(.5)
    print(hammer_tool.clean_tool())
    time.sleep(.5)
    print(hammer_tool.return_tool())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    chisel_tool = Chisel("Chisel", "iron", 2, "flat")
    print(chisel_tool.use_tool())
    time.sleep(.5)
    print(chisel_tool.sharpen())
    time.sleep(.5)
    print(chisel_tool.clean_tool())
    time.sleep(.5)
    print(chisel_tool.return_tool())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    screwdriver_tool = Screwdriver("Screwdriver", "plastic", 0.5, "flathead")
    print(screwdriver_tool.use_tool())
    time.sleep(.5)
    print(screwdriver_tool.change_bit("Phillips"))
    time.sleep(.5)
    print(screwdriver_tool.clean_tool())
    time.sleep(.5)
    print(screwdriver_tool.return_tool())
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    wrench_tool = Wrench("Wrench", "aluminum", 1, "adjustable")
    print(wrench_tool.use_tool())
    time.sleep(.5)
    print(wrench_tool.adjust("10mm"))
    time.sleep(.5)
    print(wrench_tool.clean_tool())
    time.sleep(.5)
    print(wrench_tool.return_tool())
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    handsaw_tool = Handsaw("Handsaw", "metal", 1.2, "crosscut")
    print(handsaw_tool.use_tool())
    time.sleep(.5)
    print(handsaw_tool.cut())
    time.sleep(.5)
    print(handsaw_tool.clean_tool())
    time.sleep(.5)
    print(handsaw_tool.return_tool())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    sandpaper_tool = Sandpaper("Sandpaper", "paper", 0.1, "medium")
    print(sandpaper_tool.use_tool())
    time.sleep(.5)
    print(sandpaper_tool.smooth())
    time.sleep(.5)
    print(sandpaper_tool.clean_tool())
    time.sleep(.5)
    print(sandpaper_tool.return_tool())

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Closing toolbox...")
    time.sleep(2)
    print("All tools have been maintained and returned to the toolbox.")

if __name__ == "__main__":
    main()
