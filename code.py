"""
Device Operating System (DevOS)
This module provides a simple implementation of a device operating system.
It includes basic functionalities such as process management, memory management, and file system.
"""

import os
import time

# Process Management
class Process:
    """
    Represents a process running on the device.
    
    Attributes:
        pid (int): The unique process ID.
        name (str): The name of the process.
        status (str): The current status of the process (e.g., "running", "blocked", "terminated").
    """
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.status = "running"

    def terminate(self):
        """
        Terminates the process.
        """
        self.status = "terminated"

# Memory Management
class MemoryManager:
    """
    Manages the device's memory.
    
    Attributes:
        total_memory (int): The total amount of memory available on the device.
        free_memory (int): The amount of free memory available.
    """
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory

    def allocate_memory(self, process, memory_required):
        """
        Allocates memory for a process.
        
        Args:
            process (Process): The process requesting memory.
            memory_required (int): The amount of memory required by the process.
        
        Returns:
            bool: True if the memory was successfully allocated, False otherwise.
        """
        if memory_required <= self.free_memory:
            self.free_memory -= memory_required
            return True
        else:
            return False

    def free_memory(self, process, memory_to_free):
        """
        Frees memory used by a process.
        
        Args:
            process (Process): The process releasing memory.
            memory_to_free (int): The amount of memory to be freed.
        """
        self.free_memory += memory_to_free

# File System
class FileSystem:
    """
    Manages the device's file system.
    
    Attributes:
        root_directory (str): The path to the root directory.
    """
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def create_file(self, file_path, content):
        """
        Creates a new file with the given content.
        
        Args:
            file_path (str): The path to the new file.
            content (str): The content to be written to the file.
        """
        with open(os.path.join(self.root_directory, file_path), "w") as file:
            file.write(content)

    def read_file(self, file_path):
        """
        Reads the content of a file.
        
        Args:
            file_path (str): The path to the file.
        
        Returns:
            str: The content of the file.
        """
        with open(os.path.join(self.root_directory, file_path), "r") as file:
            return file.read()

# Device Operating System
class DevOS:
    """
    Represents the device operating system.
    
    Attributes:
        process_manager (ProcessManager): The process manager for the operating system.
        memory_manager (MemoryManager): The memory manager for the operating system.
        file_system (FileSystem): The file system for the operating system.
    """
    def __init__(self, total_memory, root_directory):
        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager(total_memory)
        self.file_system = FileSystem(root_directory)

    def run_process(self, process):
        """
        Runs a process on the device.
        
        Args:
            process (Process): The process to be run.
        """
        if self.memory_manager.allocate_memory(process, 1024):
            self.process_manager.add_process(process)
            print(f"Running process: {process.name}")
        else:
            print(f"Unable to run process: {process.name} (insufficient memory)")

    def terminate_process(self, process):
        """
        Terminates a running process.
        
        Args:
            process (Process): The process to be terminated.
        """
        self.memory_manager.free_memory(process, 1024)
        self.process_manager.remove_process(process)
        process.terminate()
        print(f"Terminated process: {process.name}")

# Example usage
if __name__ == "__main__":
    # Create a new device operating system
    devos = DevOS(total_memory=4096, root_directory="/")

    # Create some processes
    process1 = Process(pid=1, name="Process 1")
    process2 = Process(pid=2, name="Process 2")

    # Run the processes
    devos.run_process(process1)
    devos.run_process(process2)

    # Terminate a process
    devos.terminate_process(process1)

    # Create a file and read its content
    devos.file_system.create_file("example.txt", "This is an example file.")
    content = devos.file_system.read_file("example.txt")
    print(f"File content: {content}")
