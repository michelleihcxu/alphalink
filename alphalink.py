import psutil
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

class AlphaLink:
    def __init__(self, root):
        self.root = root
        self.root.title("AlphaLink - Memory Usage Manager")
        self.create_widgets()
        self.update_memory_info()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Process", "Memory Usage"), show="headings")
        self.tree.heading("Process", text="Process")
        self.tree.heading("Memory Usage", text="Memory Usage (MB)")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self.root, text="Refresh", command=self.update_memory_info)
        self.refresh_button.pack(pady=5)

        self.plot_button = ttk.Button(self.root, text="Plot Memory Usage", command=self.plot_memory_usage)
        self.plot_button.pack(pady=5)

    def update_memory_info(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
            try:
                memory_usage_mb = proc.info['memory_info'].rss / 1024 / 1024
                self.tree.insert('', 'end', values=(proc.info['name'], f"{memory_usage_mb:.2f}"))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    
    def plot_memory_usage(self):
        process_names = []
        memory_usages = []

        for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']):
            try:
                memory_usage_mb = proc.info['memory_info'].rss / 1024 / 1024
                process_names.append(proc.info['name'])
                memory_usages.append(memory_usage_mb)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        plt.figure(figsize=(10, 6))
        plt.barh(process_names, memory_usages, color='skyblue')
        plt.xlabel('Memory Usage (MB)')
        plt.title('Memory Usage by Process')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlphaLink(root)
    root.mainloop()