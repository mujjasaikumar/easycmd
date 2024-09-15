
# EasyCmd

**EasyCmd** is a simple command-line tool that allows you to store and manage complex commands using shortcuts. You can add, edit, delete, list, and run these commands easily through a single tool.

## Features
- Add, edit, and delete command shortcuts.
- Run complex commands with a simple shortcut.
- Manage shortcuts easily with a few commands.
- Option to add the executable to your system `PATH`.

## Installation

### 1. Direct Download and Run

1. Download the application.zip file, extract and install the latest version of the `EasyCmdInstaller.exe`.
2. Save it in your preferred directory.

### 2. Add to PATH (Optional)

If you want to run **easycmd** globally from any command prompt or terminal, follow these steps:

1. Download the `EasyCmdInstaller.exe` file and save it in any folder on your computer.
2. Double-click the setup file and check add to path.
   - This will add `easycmd` to your system's `PATH` environment variable, allowing you to run `easycmd` from any terminal window.
   
## Usage

Once **EasyCmd** is installed and added to your system's `PATH` (if desired), you can use it from any command line by typing `easycmd` followed by the desired action.

### Available Commands:
```bash
easycmd add <shortcut_name> <command>       # Add a new shortcut
easycmd edit <shortcut_name>                # Edit an existing shortcut
easycmd delete <shortcut_name>              # Delete an existing shortcut
easycmd list                                # List all saved shortcuts
easycmd run <shortcut_name>                 # Run the command associated with the shortcut
```

### Examples

- **Add a shortcut**:
  ```bash
  easycmd add "build" "npm run build"
  ```

- **Edit a shortcut**:
  ```bash
  easycmd edit "build"
  ```

- **Delete a shortcut**:
  ```bash
  easycmd delete "build"
  ```

- **List all shortcuts**:
  ```bash
  easycmd list
  ```

- **Run a shortcut**:
  ```bash
  easycmd run "build"
  ```

## Uninstall

To uninstall, simply delete the `easycmd.exe` file from your system. If you added it to your `PATH`, you can remove it manually from the environment variables.

