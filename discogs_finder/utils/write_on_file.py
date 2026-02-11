def write_on_file(url, file_path):
    with open(file_path, "a") as f:
        f.write(f'<a href="{url}" target="_blank">{url}</a><br>\n')
