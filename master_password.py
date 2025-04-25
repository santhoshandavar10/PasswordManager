# master_password.py
import os
from cryptography.fernet import Fernet
from rich.console import Console

MASTER_KEY_FILE = "master.key"

def set_master_password():
    console = Console()
    master_password = console.input("[bold yellow]Set your master password: [/bold yellow]")
    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(MASTER_KEY_FILE, "wb") as f:
        f.write(key + b"\n" + cipher.encrypt(master_password.encode()))

def verify_master_password():
    console = Console()

    if not os.path.exists(MASTER_KEY_FILE):
        console.print("[bold red]No master password found! Let's create one.[/bold red]")
        set_master_password()

    with open(MASTER_KEY_FILE, "rb") as f:
        key = f.readline().strip()
        encrypted_master = f.readline().strip()

    cipher = Fernet(key)
    master_password = cipher.decrypt(encrypted_master).decode()

    entered_password = console.input("[bold yellow]Enter master password: [/bold yellow]")

    if entered_password != master_password:
        console.print("[bold red]❌ Incorrect master password. Exiting...[/bold red]")
        exit()
    else:
        console.print("[bold green]✅ Access granted![/bold green]\n")
