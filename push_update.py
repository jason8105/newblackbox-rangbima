import os
import datetime
import subprocess

def run_git_push():
    # Prompt the user for a custom commit message
    user_msg = input("[?] Enter your commit message (or press Enter for default timestamp): ").strip()
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Use the custom message if provided; otherwise, use the default timestamp message
    if user_msg:
        commit_msg = user_msg
    else:
        commit_msg = f"Automated update: {timestamp}"
    
    print("[*] Adding all changes...")
    subprocess.run(["git", "add", "."], capture_output=True, text=True)
    
    print(f"[*] Committing with message: '{commit_msg}'")
    subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
    
    print("[*] Pushing to GitHub (main branch)...")
    result = subprocess.run(["git", "push", "origin", "main", "--force"], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("==================================================")
        print(" SUCCESS! Code pushed successfully.")
        print("==================================================")
    else:
        print("[!] Push failed or nothing to commit:")
        print(result.stdout + result.stderr)

if __name__ == "__main__":
    run_git_push()
