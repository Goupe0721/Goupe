from pathlib import Path
import markdown
import datetime

contents = Path("contents")
blog = Path("blog_contents")
blog.mkdir(exist_ok=True)
template = Path("template.html")
home_template = Path("home_template.html")
h_t_content = home_template.read_text(encoding="utf-8")
template_content = template.read_text(encoding="utf-8")
home = Path("index.html")
#定位以及創造文件夾

for content in contents.iterdir():
    if content.suffix in ['.txt','.md']:
        put_time = content.read_text(encoding='utf-8')
        if "{{no_time}}" in put_time:
            time = datetime.date.today().strftime("%Y年%m月%d日")
            blog_time = put_time.replace("{{no_time}}",time)
            content.write_text(blog_time,encoding='utf-8')
    
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
    blog_list += f'<a href="{blog_content}">{blog_content.stem}</a><br>'

home_content = h_t_content.replace("{blog_list}",blog_list)
home.write_text(home_content,encoding="utf-8")

