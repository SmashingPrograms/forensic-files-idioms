episodes = open("forensic_files.txt", "r")

episode_parse = episodes.readlines()

episodes = []

for line in episode_parse:
    if line.startswith("|\""):
        if line.startswith("|\"The "):
            x = line[6:-2]
        else:
            x = line[2:-2]
        x = x.lower()
        x = "# [[" + x + "]]"
        print(x)
