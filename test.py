import subprocess

def commit(date,i):
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "test", "--date", "{} 12:0{}:00".format(date,str(i))])
    subprocess.run(["git", "push"])
    
def reverse_date(date):
    str_date = date.split("/")
    return f"{str_date[1]}/{str_date[0]}/{str_date[2]}"

def change_data():
    with open("data.txt", "r+") as f:
        data = f.readlines()
        if data == "a":
            f.write("b")
        else:
            f.write("a")

with open("dates.txt", "r") as f:
    dates = f.readlines()
    for date in dates:
        for i in range(10):
            date_2 = reverse_date(date)
            change_data()
            commit(reverse_date(date),i)