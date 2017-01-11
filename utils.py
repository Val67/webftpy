import datetime

# Return the parent folder of a given directory
def parent_folder(path):
	return "/".join(path.split("/")[:-1])

def make_path(current_dir, subdir):
	if current_dir == "/":
		return "/" + subdir
	else:
		return current_dir + "/" + subdir

# Format the date from raw FTP format to human-readable format
def format_date(date):
	return datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%x %X')