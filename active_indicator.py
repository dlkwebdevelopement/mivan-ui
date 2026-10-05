import os
import re

files = {
    'index.html': 'Home',
    'about.html': 'About Us',
    'properties.html': 'Properties',
    'contact.html': 'Contact'
}

for file, page_name in files.items():
    filepath = os.path.join(os.getcwd(), file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We need to find the desktop nav link for `page_name` and change `w-0` to `w-full` on its span
    # The desktop nav link looks like:
    # <a href="..." class="nav-link nav-active ...">
    #   <i ...></i>
    #   <span>{page_name}</span>
    #   <span class="absolute bottom-0 left-0 w-0 h-[2px] ..."></span>
    # </a>
    
    # We can use regex to find the active block and replace w-0 with w-full
    pattern = r'(<a[^>]*class="[^"]*nav-active[^"]*"[^>]*>.*?<span>' + re.escape(page_name) + r'</span>\s*<span[^>]*class="[^"]*)w-0([^"]*".*?</span>\s*</a>)'
    
    content = re.sub(pattern, r'\g<1>w-full\g<2>', content, flags=re.DOTALL)
    
    # Also for mobile, make sure the mobile link has active styling (text-[#D4A017])
    # <a href="..." class="mobile-nav-link ... text-[#061838] ...">
    #   <i ...></i>
    #   <span>{page_name}</span>
    # </a>
    mobile_pattern = r'(class="mobile-nav-link[^"]*)text-\[\#061838\]([^"]*"[^>]*>\s*<i[^>]*>\s*</i>\s*<span>' + re.escape(page_name) + r'</span>)'
    content = re.sub(mobile_pattern, r'\g<1>text-[#D4A017]\g<2>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Updated active page indicator (underline w-full and mobile text color).')
