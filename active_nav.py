import os
import re

files = [
    'properties.html',
    'contact.html'
]

for file in files:
    filepath = os.path.join(os.getcwd(), file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if file == 'properties.html':
        content = content.replace(
            '<a href="properties.html"\n          class="nav-link group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">',
            '<a href="properties.html"\n          class="nav-link nav-active group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">'
        )
    elif file == 'contact.html':
        content = content.replace(
            '<a href="contact.html"\n          class="nav-link group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">',
            '<a href="contact.html"\n          class="nav-link nav-active group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1">'
        )
        
    # Let's also add active styling to mobile nav just in case! 
    # Usually active mobile link text color is gold text-[#D4A017] instead of text-[#061838]
    if file == 'properties.html':
        content = content.replace(
            '<a href="properties.html"\n          class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">',
            '<a href="properties.html"\n          class="mobile-nav-link flex items-center gap-2.5 text-[#D4A017] font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">'
        )
    elif file == 'contact.html':
        content = content.replace(
            '<a href="contact.html"\n          class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">\n          <i data-lucide="phone-call" class="w-4 h-4 text-[#D4A017]"></i>\n          <span>Contact</span>\n        </a>',
            '<a href="contact.html"\n          class="mobile-nav-link flex items-center gap-2.5 text-[#D4A017] font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">\n          <i data-lucide="phone-call" class="w-4 h-4 text-[#D4A017]"></i>\n          <span>Contact</span>\n        </a>'
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Active classes applied to Properties and Contact.')
