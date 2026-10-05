import os
import re

files = ['index.html', 'about.html', 'properties.html', 'contact.html']

for file in files:
    filepath = os.path.join(os.getcwd(), file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to change w-full back to w-0 on the span that is inside the active link.
    # The active link span is: <span class="absolute bottom-0 left-0 w-full h-[2px] bg-[#F5C542] rounded-full transition-all duration-300 group-hover:w-full"></span>
    
    # We can just look for the specific span line that has w-full (since it's only the active link that got w-full)
    # Be careful not to replace w-full that might be used elsewhere (like the mobile Enquire button width).
    # The span we modified has exactly: w-full h-[2px] bg-[#F5C542]
    
    content = content.replace('w-full h-[2px] bg-[#F5C542]', 'w-0 h-[2px] bg-[#F5C542]')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Reverted active page underline from w-full to w-0.')
