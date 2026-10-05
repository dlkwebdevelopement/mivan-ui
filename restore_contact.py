import os
import re

desktop_contact = """
        <a href="contact.html"
          class="nav-link group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">
          <i data-lucide="phone-call" class="w-3.5 h-3.5 transition-colors group-hover:text-[#D4A017]"></i>
          <span>Contact</span>
          <span
            class="absolute bottom-0 left-0 w-0 h-[2px] bg-[#F5C542] rounded-full transition-all duration-300 group-hover:w-full"></span>
        </a>

        <!-- Subtle Separator -->"""

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
    
    # 1. Restore the Desktop Contact Link right before the Subtle Separator
    # Note: right now, the separator looks like:
    #         <!-- Subtle Separator -->
    # We will replace it with the contact link + the separator
    if '<span>Contact</span>' not in content[:content.find('<!-- Subtle Separator -->')]:
        content = content.replace('        <!-- Subtle Separator -->', desktop_contact, 1)
        
    # 2. Fix the typo href=\"index.html#managed-properties\"
    content = content.replace('href=\\"index.html#managed-properties\\"', 'href="index.html#managed-properties"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Restored Desktop Contact link and fixed typos.')
