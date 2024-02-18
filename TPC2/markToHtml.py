import os
import re
import sys


def markdownToHtml(line):

    # Headers
    line = re.sub(r'^#\s(.*?)$', r'<h1>\1</h1>', line)
    line = re.sub(r'^##\s(.*?)$', r'<h2>\1</h2>', line)
    line = re.sub(r'^###\s(.*?)$', r'<h3>\1</h3>', line)

    # Bold
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

    # Italic
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)

    # Blockquote
    line = re.sub(r'^>\s+(.*?)$', r'<blockquote>\1</blockquote>', line)

    # Link
    line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

    # Image
    line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" />', line)
    return line


def main(file):
    with open(file, "r") as markdown_file:
        base_name = os.path.splitext(file)[0]
        output_file_name = base_name + "_html.html"
        lines = markdown_file.readlines()
        print("Output file name:", output_file_name)

    with open(output_file_name, "w") as output_file:
        output_file.write("""
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <title>Markdown to HTML</title>
    <meta charset="utf-8">
</head>
<body>
""")

        for line in lines:
            html_line = markdownToHtml(line)
            output_file.write(html_line)

        output_file.write("""
</body>
</html>s
        """)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: specify the markdown file")
    else:
        main(sys.argv[1])

