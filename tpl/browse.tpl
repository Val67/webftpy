% from utils import *
<!DOCTYPE html>
<html>
<head>
<title>Webftpy - {{path}}</title>
<meta name="robots" content="noarchive" />
<link rel="stylesheet" href="/static/style.css" />
</head>
<body>
	<h1>Webftpy</h1>
	<h2>Exploring {{path}}</h2>
	<form method="post" action="/mcd">
		<table>
		<tr>
		<th></th>
		<th></th>
		<th>Name</th>
		<th>Type</th>
		<th>Size</th>
		<th>Date Modified</th>
		</tr>
		% for f in files:
			% if f[1]["type"] != 'cdir':
				<tr>
				% if f[1]["type"] == 'pdir':
				<td></td>
				<td><img src="/static/up.png" /></td>
				<td><a href="/?p={{parent_folder(path)}}">{{f[0]}}</a></td>
				<td>{{f[1]["type"]}}</td>
				<td>-</td>
				% elif f[1]["type"] == 'dir':
				<td><input type="checkbox" name="{{f[0]}}" /></td>
				<td><img src="/static/folder.png" /></td>
				<td><a href="/?p={{make_path(path, f[0])}}">{{f[0]}}</a></td>
				<td>{{f[1]["type"]}}</td>
				<td>-</td>
				% else:
				<td><input type="checkbox" name="{{f[0]}}" /></td>
				<td><img src="/static/file.png" /></td>
				<td><a href="/download?f={{make_path(path, f[0])}}">{{f[0]}}</a></td>
				<td>{{f[1]["type"]}}</td>
				<td>{{f[1]["size"]}}</td>
				% end

				<td>{{format_date(f[1]["modify"])}}</td>
				</tr>
			% end
		% end
		</table><br />
		Selected files :
		<select name="action">
			<option>Move</option>
			<option>Copy</option>
			<option>Delete</option>
		</select>
		<input type="hidden" name="path" value="{{path}}" />
		<input type="submit" />
	</form>
	
	<form action="/upload" method="post" enctype="multipart/form-data">
		<input type="hidden" name="path" value="{{path}}" />
		<input type="file" name="file" />
		<input type="submit" value="Upload" />
	</form>
	<form action="/newdir" method="post">
		<input type="hidden" name="path" value="{{path}}" />
		<input type="text" name="name" />
		<input type="submit" value="New directory" />
	</form>
</form>
</body>
</html>