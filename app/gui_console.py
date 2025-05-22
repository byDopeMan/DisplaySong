
import queue
import tkinter as tk
from tkinter import ttk, scrolledtext
import time
import threading
from PIL import Image, ImageTk
import os
import sys
import webbrowser

def get_script_type():
    if getattr(sys, 'frozen', False):
        return ".exe"
    else:
        return ".py"

class SystemTrayIntegration:
    def __init__(self, gui_console):
        # Reference to parent console
        self.gui_console = gui_console
        self.setup_tray_thread = None
        
    def start_tray(self):
        """Start the system tray in a separate thread"""
        self.setup_tray_thread = threading.Thread(target=self.setup_tray, daemon=True)
        self.setup_tray_thread.start()
    
    def setup_tray(self):
        try:
            # Import here to avoid importing at the module level
            from pystray import Icon, Menu, MenuItem
            from PIL import Image
            
            # Create menu items
            def open_console(icon, item):
                self.gui_console.show()
            
            def open_selection_url(icon, item):
                webbrowser.open("http://127.0.0.1:5000/select")
                self.gui_console.write("Opening selection page...", "success")
            
            def on_restart(icon, item):
                icon.visible = False
                self.gui_console.write("Restarting program...", "warning")
                python = sys.executable
                os.execl(python, python, *sys.argv)
            
            def on_exit(icon, item):
                self.gui_console.write("Closing program...", "warning")
                icon.stop()
                os._exit(0)
            
            # Create tray icon
            icon = Icon('DisplaySong Tray')
            
            if not getattr(sys, 'frozen', False):
                icon.icon = Image.open("app.ico")
            else:
                icon.icon = Image.open('_internal/app.ico')
            
            # Set up menu
            icon.menu = Menu(
                MenuItem("Open Console", open_console),
                MenuItem("Open Selection Page", open_selection_url),
                Menu.SEPARATOR,
                MenuItem("Restart Program", on_restart),
                MenuItem("Exit Program", on_exit),
            )
            
            # Run the icon in the current thread
            icon.run()
            
        except ImportError as e:
            self.gui_console.write(f"Error setting up system tray: {e}", "error")
            self.gui_console.write("Make sure pystray and pillow are installed", "warning")

class ModernGuiConsole:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DisplaySong Console")
        self.root.geometry("800x500")
        self.root.minsize(600, 400)
        
        # Set theme colors
        self.bg_color = "#1e1e2e"
        self.fg_color = "#cdd6f4"
        self.accent_color = "#89b4fa"
        self.secondary_color = "#f38ba8"
        self.success_color = "#a6e3a1"
        self.warning_color = "#f9e2af"
        self.error_color = "#f38ba8"
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TButton', 
                             background=self.accent_color, 
                             foreground='black', 
                             padding=6, 
                             relief="flat")
        self.style.map('TButton', 
                       background=[('active', self.secondary_color)])
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create main layout
        self._create_header()
        self._create_console()
        self._create_stats_panel()
        self._create_bottom_controls()
        
        # Queue for thread-safe console updates
        self.queue = queue.Queue()
        self.poll_queue()
        
        # Custom tags for colored text
        self.text_area.tag_config("info", foreground=self.fg_color)
        self.text_area.tag_config("success", foreground=self.success_color)
        self.text_area.tag_config("warning", foreground=self.warning_color)
        self.text_area.tag_config("error", foreground=self.error_color)
        self.text_area.tag_config("accent", foreground=self.accent_color)
        
        # Event bindings
        self.root.bind("<Unmap>", self.on_minimize)
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        
        # Initialize system tray integration
        self.tray = SystemTrayIntegration(self)
        
    def _create_header(self):
        """Create the header section with logo and title"""
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        

        if not getattr(sys, 'frozen', False):
            print("Python")
            logo = Image.open('app.ico')
        else:
            logo = Image.open('_internal/app.ico')
        
        logo = logo.resize((32, 32), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo)
        
        # Display the logo
        self.logo_label = tk.Label(self.header_frame, image=self.logo_img, bg=self.bg_color)
        self.logo_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Also set as window icon
        self.root.iconphoto(True, self.logo_img)
        
        # Title label
        self.title_label = tk.Label(self.header_frame, 
                                    text="DisplaySong Console", 
                                    font=("Segoe UI", 18, "bold"), 
                                    bg=self.bg_color, 
                                    fg=self.accent_color)
        self.title_label.pack(side=tk.LEFT)
        
        # Status indicator
        self.status_frame = ttk.Frame(self.header_frame)
        self.status_frame.pack(side=tk.RIGHT)
        
        self.status_label = tk.Label(self.status_frame, 
                                     text="● Running", 
                                     font=("Segoe UI", 10), 
                                     bg=self.bg_color, 
                                     fg=self.success_color)
        self.status_label.pack(side=tk.RIGHT)
    
    def _create_console(self):
        """Create the main console area"""
        # Console and stats container
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Console frame (70% of width)
        self.console_frame = ttk.Frame(self.content_frame)
        self.console_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Console header
        self.console_header = tk.Label(self.console_frame, 
                                      text="Console Output", 
                                      font=("Segoe UI", 10, "bold"), 
                                      bg=self.bg_color, 
                                      fg=self.fg_color)
        self.console_header.pack(anchor="w", pady=(0, 5))
        
        # Text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(self.console_frame, 
                                                  wrap=tk.WORD, 
                                                  font=("Consolas", 10),
                                                  bg="#282a36", 
                                                  fg=self.fg_color, 
                                                  insertbackground=self.fg_color)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.configure(state='disabled')
    
    def _create_stats_panel(self):
        """Create the statistics panel on the right side"""
        # Stats frame (30% of width)
        # Create a frame with a specific width
        self.stats_frame = ttk.Frame(self.content_frame, width=200)
        self.stats_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        # Prevent the frame from shrinking smaller than its requested width
        self.stats_frame.pack_propagate(False)
        
        # Stats header
        self.stats_header = tk.Label(self.stats_frame, 
                                    text="Status", 
                                    font=("Segoe UI", 10, "bold"), 
                                    bg=self.bg_color, 
                                    fg=self.fg_color)
        self.stats_header.pack(anchor="w", pady=(0, 5))
        
        # Stats content frame with darker background
        self.stats_content = tk.Frame(self.stats_frame, bg="#282a36")
        self.stats_content.pack(fill=tk.BOTH, expand=True)
        
        # Server status
        self.server_frame = tk.Frame(self.stats_content, bg="#282a36")
        self.server_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(self.server_frame, text="Server:", bg="#282a36", fg=self.fg_color).pack(anchor="w")
        self.server_status = tk.Label(self.server_frame, 
                                     text="● Running on port 5000", 
                                     bg="#282a36", 
                                     fg=self.success_color)
        self.server_status.pack(anchor="w", padx=(10, 0))
        
        # Spotify status
        self.spotify_frame = tk.Frame(self.stats_content, bg="#282a36")
        self.spotify_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(self.spotify_frame, text="Spotify:", bg="#282a36", fg=self.fg_color).pack(anchor="w")
        self.spotify_status = tk.Label(self.spotify_frame, 
                                      text="○ Waiting for auth", 
                                      bg="#282a36", 
                                      fg=self.warning_color)
        self.spotify_status.pack(anchor="w", padx=(10, 0))
        
        # Current track
        self.track_frame = tk.Frame(self.stats_content, bg="#282a36")
        self.track_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(self.track_frame, text="Track:", bg="#282a36", fg=self.fg_color).pack(anchor="w")
        self.track_info = tk.Label(self.track_frame, 
                                  text="No track playing", 
                                  bg="#282a36", 
                                  fg=self.fg_color,
                                  wraplength=180,
                                  justify=tk.LEFT)
        self.track_info.pack(anchor="w", padx=(10, 0))
        
        # Quick actions section
        self.actions_frame = tk.Frame(self.stats_content, bg="#282a36")
        self.actions_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(self.actions_frame, text="Quick Actions:", bg="#282a36", fg=self.fg_color).pack(anchor="w")
        
        # Button styles for quick actions
        self.style.configure("Action.TButton", padding=4, font=("Segoe UI", 9))
        
        # Quick action buttons
        self.restart_button = ttk.Button(self.actions_frame, 
                                        text="Restart Program", 
                                        style="Action.TButton",
                                        command=self.restart_func)
        self.restart_button.pack(anchor="w", padx=(10, 0), pady=(5, 0), fill=tk.X)
                                 
        self.auth_button = ttk.Button(self.actions_frame, 
                                     text="Re-Authenticate", 
                                     style="Action.TButton",
                                     command=self.reauth_spotify)
        self.auth_button.pack(anchor="w", padx=(10, 0), pady=(5, 0), fill=tk.X)
    
    def _create_bottom_controls(self):
        """Create the bottom control bar"""
        # Bottom frame for buttons
        self.bottom_frame = ttk.Frame(self.main_frame)
        self.bottom_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Create buttons
        self.clear_button = ttk.Button(self.bottom_frame, text="Clear Console", command=self.clear_console)
        self.clear_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.open_button = ttk.Button(self.bottom_frame, text="Open Selection Page", command=self.open_selection_page)
        self.open_button.pack(side=tk.LEFT, padx=5)
        
        self.minimize_button = ttk.Button(self.bottom_frame, text="Minimize to Tray", command=self.minimize)
        self.minimize_button.pack(side=tk.RIGHT)
    
    def poll_queue(self):
        """Check for new console messages in the queue"""
        while not self.queue.empty():
            msg, tag = self.queue.get()
            self.text_area.configure(state='normal')
            
            # Add timestamp to each message
            timestamp = f"[{time.strftime('%H:%M:%S')}] "
            self.text_area.insert('end', timestamp, "accent")
            
            # Insert the actual message with the specified tag
            self.text_area.insert('end', msg + '\n', tag)
            self.text_area.configure(state='disabled')
            self.text_area.see('end')
            
        self.root.after(100, self.poll_queue)  # Check every 100ms
    
    def write(self, msg, tag="info"):
        """Write a message to the console with optional tag for styling"""
        self.queue.put((msg, tag))
    
    def clear_console(self):
        """Clear the console text area"""
        self.text_area.configure(state='normal')
        self.text_area.delete(1.0, tk.END)
        self.text_area.configure(state='disabled')
        self.write("Console cleared", tag="accent")
    
    def open_selection_page(self):
        """Open the selection page in browser"""
        webbrowser.open("http://127.0.0.1:5000/select")
        self.write("Opening selection page...", tag="success")
    
    def restart_func(self):
        """Refresh the current track information"""
        self.write("Restarting program...", "warning")
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
    def reauth_spotify(self):
        """Re-authenticate with Spotify"""
        self.write("Initiating Spotify re-authentication...", tag="info")
        webbrowser.open("http://127.0.0.1:5000/auth")
        # Again, this is a placeholder for the actual implementation
    
    def update_spotify_status(self, connected=False, track_info=None):
        """Update the Spotify connection status and track info"""
        if connected:
            self.spotify_status.config(text="● Connected", fg=self.success_color)
            if track_info:
                self.track_info.config(text=track_info)
        else:
            self.spotify_status.config(text="○ Disconnected", fg=self.warning_color)
            self.track_info.config(text="No track playing")
    
    def show(self):
        """Show the console window"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.write("Console window restored", tag="accent")
    
    def minimize(self):
        """Minimize to system tray"""
        self.root.withdraw()
    
    def on_minimize(self, event):
        """Handle minimize event"""
        if self.root.state() == 'iconic':
            self.root.after(0, self.minimize)
    
    def on_close(self):
        """Handle close button click"""
        self.minimize()
    
    def update_status(self, status, color=None):
        """Update the main status indicator"""
        self.status_label.config(text=f"● {status}")
        if color:
            self.status_label.config(fg=color)
    
    def mainloop(self):
        """Start the GUI main loop and system tray"""
        # Start the system tray in a separate thread
        self.tray.start_tray()
        self.root.minsize()
        
        # Start the main GUI loop
        self.root.mainloop()

gui_console = ModernGuiConsole()
