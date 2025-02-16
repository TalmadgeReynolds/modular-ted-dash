import os
import subprocess

def run_command(command):
    """Runs a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running command: {command}\n{e.stderr}")
        return None

def get_current_branch():
    """Fetches the current Git branch dynamically."""
    branch = run_command("git rev-parse --abbrev-ref HEAD")
    return branch if branch else "main"

def check_git_status():
    """Checks the Git status to see if there are changes."""
    print("🔍 Checking Git status...")
    status = run_command("git status --porcelain")
    return status if status else None  # Returns None if no changes

def stage_changes():
    """Stages all changes."""
    print("📂 Staging all changes...")
    return run_command("git add .")

def commit_changes():
    """Commits changes with a user-provided or default message."""
    commit_message = input("📝 Enter commit message (or press Enter for default): ") or "Auto-commit from script"
    print(f"💾 Committing changes with message: {commit_message}")
    return run_command(f'git commit -m "{commit_message}"')

def pull_latest_changes(branch):
    """Pulls latest changes before pushing to avoid conflicts."""
    print(f"🔄 Pulling latest changes from {branch}...")
    return run_command(f"git pull origin {branch} --rebase")

def push_changes(branch):
    """Pushes changes to GitHub."""
    print(f"🚀 Pushing changes to GitHub ({branch})...")
    return run_command(f"git push origin {branch}")

def main():
    """Runs the full Git automation process."""
    print("\n🚀 **Git Auto Sync Script for modular-ted-dash** 🚀\n")

    branch = get_current_branch()
    print(f"📌 Current Git branch: {branch}")

    # Check if there are changes before proceeding
    if not check_git_status():
        print("✅ No changes to commit. Exiting.")
        return

    # Git Operations
    stage_changes()
    commit_changes()
    pull_latest_changes(branch)
    push_changes(branch)

    print("\n✅ **All changes have been pushed to GitHub!** 🎉")

if __name__ == "__main__":
    main()
