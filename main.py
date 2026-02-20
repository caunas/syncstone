# Libs
import os
import git

# Intern Libs

# Intern Variables
REPO_PATH = r"C:\Users\haonovi\Desktop\mods_test"
ORIGIN_REPO = "https://github.com/caunas/mods.git"

try:
	repo = git.Repo(REPO_PATH)
	origin = repo.remotes.origin
	print("Repositorio OK!")
except Exception as e:
	print(str(e))

# ja temos repo
try:
	origin.pull()
	print("MODS ATUALIZADOS")
except Exception as e:
	print(str(e))