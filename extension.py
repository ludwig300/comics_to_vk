import os
import urllib.parse


def get_extension(urlstring):
    parsed_url = urllib.parse.urlsplit(urlstring, scheme='', allow_fragments=True)
    scheme, netloc, path_file, *others = parsed_url
    unquoted_filename = urllib.parse.unquote(path_file, encoding='utf-8', errors='replace')
    splited_filename = os.path.split(unquoted_filename)
    path, file = splited_filename
    split_file = os.path.splitext(file)
    filename, extension, = split_file
    return extension