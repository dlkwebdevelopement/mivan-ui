import os
import re

desktop_properties_simple = """        <a href="properties.html"
          class="nav-link group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">
          <i data-lucide="building-2" class="w-3.5 h-3.5 transition-colors group-hover:text-[#D4A017]"></i>
          <span>Properties</span>
          <span
            class="absolute bottom-0 left-0 w-0 h-[2px] bg-[#F5C542] rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>"""

mobile_properties_simple = """        <a href="properties.html"
          class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">
          <i data-lucide="building-2" class="w-4 h-4 text-[#D4A017]"></i>
          <span>Properties</span>
        </a>"""

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
    
    # Replace Desktop Properties Dropdown
    content = re.sub(
        r'\s*<!-- Properties Dropdown Menu -->.*?<!-- Subtle Separator -->',
        r'\n\n' + desktop_properties_simple + r'\n\n        <!-- Subtle Separator -->',
        content, flags=re.DOTALL
    )
    
    # Replace Mobile Properties Grouped Section
    content = re.sub(
        r'\s*<!-- Mobile Properties Grouped Section -->.*?<a href=\"(?:index\.html)?#managed-properties\"',
        r'\n\n' + mobile_properties_simple + r'\n        <a href="index.html#managed-properties"',
        content, flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Properties dropdown removed and converted to simple link in all files.')
