import os, sys
from datetime import datetime

template_dir = sys.argv[1]
template = ""

print(f"Template: {template_dir}")

with open(template_dir, "r") as t:
    template = t.read()

end_pad = template.find("<!--CONTENT-INSERTION-->")

if end_pad == -1:
    print("Unable to find the template content begin point")
    exit()

insert_point1 = template.rfind('\n', 0, end_pad) + 1
insert_point2 = end_pad + len("<!--CONTENT-INSERTION-->") + 1

for root, dirs, files in os.walk("."):
    for f in files:
        if ".html" not in f or f == sys.argv[1]:
            continue

        fname = os.path.join(root, f)

        html_str = ""
        with open(fname, "r") as html:
            html_str = html.read()

        begin = html_str.find("<!--CONTENT-BEGIN-->") + 1
        end = html_str.find("<!--CONTENT-END-->")

        if begin == -1:
            print(f"File {fname} doesn't have a content begin mark, skipping")
            continue

        if end == -1:
            print(f"File {fname} doesn't have a content end mark, skipping")
            continue

        begin += len("<!--CONTENT-BEGIN-->")

        real_content = html_str[begin:end - 1]

        content_lines = real_content.split('\n')

        modified_content = template[:insert_point1] + "<!--CONTENT-BEGIN-->\n"

        for line in content_lines:
            modified_content += line
            modified_content += '\n'

        modified_content +=  "<!--CONTENT-END-->\n" + template[insert_point2:]

        edit_time = datetime.fromtimestamp(os.path.getmtime(fname))
        modified_content = modified_content.replace("$EDITDATE$", edit_time.strftime("%H:%M %d. %B %Y"))

        #print(f"File {fname}:\n-> Real Content:\n{real_content}\n-> Modified Content:\n{modified_content}")

        with open(fname, "w") as html:
            html.write(modified_content)

