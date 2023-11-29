import subprocess

# Install wget
subprocess.run(["apt", "install", "wget", "-y"])

# Install webdriver_manager
subprocess.run(["pip", "install", "webdriver_manager"])

# Upgrade webdriver_manager
subprocess.run(["pip", "install", "--upgrade", "webdriver_manager"])

# Download and add the Brave browser keyring
subprocess.run(["wget", "-O", "/usr/share/keyrings/brave-browser-archive-keyring.gpg", "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"])

# Add Brave browser repository to sources.list.d
repository_command = 'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list'
subprocess.run(repository_command, shell=True)

# Update the package list
subprocess.run(["sudo", "apt", "update"])

# Install Brave browser
subprocess.run(["sudo", "apt", "install", "brave-browser"])

