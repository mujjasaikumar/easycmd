import os
import subprocess
import json
import argparse
import sys

class EasyCmd:
    def __init__(self):
        self.shortcuts = self.load_shortcuts()
    
    def load_shortcuts(self):
        try:
            if not os.path.exists('shortcuts.json'):
                with open('shortcuts.json', 'w') as f:
                    json.dump({}, f, indent=4)
                    return {}
            else:
                with open('shortcuts.json', 'r') as f:
                    return json.load(f)
        except Exception:
            print("An exception occurred while loading shortcuts. Try again")
            sys.exit(1)
            
    # Save shortcuts to the JSON file
    def save_shortcuts(self):
        with open('shortcuts.json', 'w') as f:
            json.dump(self.shortcuts, f, indent=4)

    def add_cmd(self, shortcut_name=None, command=None):
        if not shortcut_name and not command:
            shortcut_name = input("Enter the new shortcut_name: ")
            command = input("Enter the new command: ")
        elif not command:
            command = input("Enter the new command: ")

        if shortcut_name in self.shortcuts:
            print(f"\nShortcut '{shortcut_name}' already exists.")
        else:
            self.shortcuts[shortcut_name] = command
            self.save_shortcuts()
            print(f"\nAdded shortcut '{shortcut_name}'.")

    def edit_cmd(self, shortcut_name=None):
        self.list_cmd()
        if not shortcut_name:
            shortcut_name = input("Enter the shortcut_name to edit: ")
        if shortcut_name in self.shortcuts:
            # Display the current command
            current_command = self.shortcuts[shortcut_name]
            print(f"Current command for '{shortcut_name}': {current_command}")

            # Prompt the user to enter a new command
            new_command = input("Enter the new command (press Enter to keep the current command): ")

            # If the user provides a new command, update it
            if new_command.strip():
                self.shortcuts[shortcut_name] = new_command
                self.save_shortcuts()
                print(f"\nUpdated shortcut '{shortcut_name}' with new command.")
            else:
                print("\nNo changes made. The command remains the same.")
        else:
            print(f"\nShortcut '{shortcut_name}' does not exist.")


    def delete_cmd(self, shortcut_name=None):
        if shortcut_name is None:
            # Interactive mode: list all shortcuts and prompt for input
            self.list_cmd()
            print()
            shortcut_name = input("\nEnter the name of the shortcut to delete: ").strip()

        if shortcut_name in self.shortcuts:
            del self.shortcuts[shortcut_name]
            self.save_shortcuts()
            print(f"\nDeleted shortcut '{shortcut_name}'.")
        else:
            print(f"\nShortcut '{shortcut_name}' does not exist.")


    def list_cmd(self, *args):
        if args:
            print("Arguments are not required for list")
            sys.exit(1)
        if self.shortcuts:
            print("\nAvailable shortcuts:")
            print("(shortcut_name: command)\n")
            for shortcut_name, command in self.shortcuts.items():
                print(f"{shortcut_name}: {command}")
        else:
            print("No shortcuts available.")
    
    def run_cmd(self, shortcut_name=None):
        if not shortcut_name:
            shortcut_name = input("Enter the shortcut_name to run: ")
        if shortcut_name in self.shortcuts:
            command = self.shortcuts[shortcut_name]
            try:
                subprocess.run(command, shell=True, check=True, text=True)
            except subprocess.CalledProcessError as e:
                print(f"Error occurred while executing command: {e}")
        else:
            print(f"Shortcut '{shortcut_name}' not found")


def main():
    """ Arg parser"""
    parser = argparse.ArgumentParser(
        description="Run complex commands using shortcuts.")
    parser.add_argument('action', choices=['add', 'edit', 'delete', 'list', 'run'], help="Action to perform.")
    parser.add_argument('shortcut_name', nargs='?', help="Name of the shortcut.")
    parser.add_argument('command', nargs='?', help="Command associated with the shortcut.")
    
    args = parser.parse_args()

    easycmd = EasyCmd()

    try:
        if args.action == 'add':
            easycmd.add_cmd(args.shortcut_name, args.command)
            sys.exit(1)
        elif args.action == 'edit':
            easycmd.edit_cmd(args.shortcut_name)
            sys.exit(1)
        elif args.action == 'delete':
            easycmd.delete_cmd(args.shortcut_name)
            sys.exit(1)
        elif args.action == 'list':
            easycmd.list_cmd()
            sys.exit(1)
        elif args.action == 'run':
            easycmd.run_cmd(args.shortcut_name)
            sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
