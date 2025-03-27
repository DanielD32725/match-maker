import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    print(result.stdout)

def automate_git_push(commit_message, branch="main"):
    try:
        print("Adding files to staging area...")
        run_command("git add -A")

        print("Committing changes...")
        run_command(f"git commit -m \"{commit_message}\"")

    print("Adding files to staging area...")
        run_command("git push")

        print(f"Pushing to branch {branch}...")
        run_command(f"git push origin {branch}")

        print("✅ GitHub push completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    commit_message = input("Enter your commit message: ").strip()
    branch = input("Enter branch name (default is 'main'): ").strip() or "main"
    automate_git_push(commit_message, branch)
