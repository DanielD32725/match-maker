import subprocess

print("Add Commit Push")

# Print the output
print("Executing \"git status\":")
print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)

# Print the output
print("Executing \"git status\":")
print("")

# Run the git add command
resultGitAdd = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)

# Print the output
print("Executing \"git add\":")
print("")

# Run the git commit command
resultGitCommit = subprocess.run(["git", "commit"], capture_output=True, text=True)

# Print the output
print("Executing \"git status\":")
print("")

# Run the git push command
resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)

print(resultGitStatus.stdout)
# print("STDERR:")
# print(result.stderr)
