import os
import re

files = [
    'properties.html',
    'index.html',
    'contact.html',
    'about.html'
]

for file in files:
    filepath = os.path.join(os.getcwd(), file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Desktop Properties Dropdown
    content = re.sub(r'\s*<!-- Properties Dropdown Menu -->.*?<!-- Subtle Separator -->', r'\n\n        <!-- Subtle Separator -->', content, flags=re.DOTALL)
    
    # Remove Mobile Properties Grouped Section
    content = re.sub(r'\s*<!-- Mobile Properties Grouped Section -->.*?<a href=\"(?:index\.html)?#managed-properties\"', r'\n\n        <a href=\"index.html#managed-properties\"', content, flags=re.DOTALL)
    
    # Additionally, in about.html and properties.html, the `#managed-properties` link might just be `href=\"index.html#managed-properties\"` or `#managed-properties`.
    # Let's adjust the mobile regex slightly to handle different hrefs for managed-properties if any.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Properties menu removed from all files.')
