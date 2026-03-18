from pathlib import Path
import markdown

contents = Path("contents")
blog = Path("blog_contents")
blog.mkdir(exist_ok=True)
template = Path("template.html")
home_template = Path("home_template.html")
h_t_content = home_template.read_text(encoding="utf-8")
template_content = template.read_text(encoding="utf-8")
home = Path("index.html")
#定位以及創造文件夾

    #此處需要寫入内容

for content in contents.iterdir():
    
    if content.suffix == ".txt":
        post_content = content.read_text(encoding="utf-8")
        html = blog/f"{content.stem}.html"
        html_content = template_content.replace("{content}",post_content)
        html_content = html_content.replace("{title}",content.stem)
        html.write_text(html_content,encoding="utf-8")

    elif content.suffix == ".md":
        html = blog/f"{content.stem}.html"
        post_content = content.read_text(encoding="utf-8")
        md_content = markdown.markdown(post_content)
        html_content = template_content.replace("{content}",md_content)
        html_content = html_content.replace("{title}",content.stem)
        html.write_text(html_content,encoding="utf-8")

blog_list = ""
for blog_content in blog.iterdir():
    blog_list += f'<p><a href="{blog_content}">{blog_content.stem}</a></p>\n'

home_content = h_t_content.replace("{blog_list}",blog_list)
home.write_text(home_content,encoding="utf-8")
