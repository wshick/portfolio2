from shutil import copytree

import markdown
# official_extensions = ['extra', 'admonition', 'meta', 'nl2br', 'smarty']
# thirdparty_extensions = ['markdown_sub_sup', 'markdown_del_ins', 'markdown_mark', 'markdown_gfm_admonition', ~~'mdx_outline',~~ 'mdx_truly_sane_lists', 'mdx_wikilink_plus', 'python-tableau-parser']
# all_extensions = [official_extensions + thirdparty_extensions]
all_extensions = ['extra', 'admonition', 'meta', 'nl2br', 'smarty', 'markdown_sub_sup', 'markdown_del_ins', 'markdown_mark', 'markdown_gfm_admonition', 'mdx_truly_sane_lists', 'mdx_wikilink_plus', 'python-tableau-parser']

# Copy static files to the build directory
copytree("static/", "build/", dirs_exist_ok=True)

# Load the template and content
template: str
content: str

with open("templates/index.html") as file:
	template = file.read()

with open("content/index.md") as file:
	content = file.read()

# Convert the markdown to HTML
html = markdown.markdown(content, extensions=all_extensions)

# Insert the HTML content into the template
output: str = template.replace("{{content}}", html)

# Write the output to the build directory
with open("build/index.html", "w") as file:
	file.write(output)
