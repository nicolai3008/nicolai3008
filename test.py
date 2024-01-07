import subprocess

def commit():
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "test", "--date", "01/07/2024 12:00:00"])
    subprocess.run(["git", "push"])
    
commit()