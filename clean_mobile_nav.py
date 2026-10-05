import os
import re

def get_mobile_nav(active_page):
    def get_color(page):
        return 'text-[#D4A017]' if page == active_page else 'text-[#061838]'
        
    return f"""      <div class="flex flex-col px-6 sm:px-12 py-6 gap-3.5 max-h-[80vh] overflow-y-auto">
        <a href="index.html"
          class="mobile-nav-link flex items-center gap-2.5 {get_color('index.html')} font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">
          <i data-lucide="home" class="w-4 h-4 text-[#D4A017]"></i>
          <span>Home</span>
        </a>
        <a href="about.html"
          class="mobile-nav-link flex items-center gap-2.5 {get_color('about.html')} font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">
          <i data-lucide="info" class="w-4 h-4 text-[#D4A017]"></i>
          <span>About Us</span>
        </a>
        <a href="properties.html"
          class="mobile-nav-link flex items-center gap-2.5 {get_color('properties.html')} font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">
          <i data-lucide="building-2" class="w-4 h-4 text-[#D4A017]"></i>
          <span>Properties</span>
        </a>
        <a href="contact.html"
          class="mobile-nav-link flex items-center gap-2.5 {get_color('contact.html')} font-semibold text-[15px] hover:text-[#D4A017] transition-colors uppercase tracking-wider">
          <i data-lucide="phone-call" class="w-4 h-4 text-[#D4A017]"></i>
          <span>Contact</span>
        </a>
        <div class="pt-3 border-t border-white/10">
          <a href="contact.html"
            class="mobile-nav-link flex items-center justify-center gap-2 w-full py-3.5 rounded-xl bg-gradient-to-r from-[#F5C542] to-[#D4A017] text-white font-bold text-[14px] uppercase tracking-wider shadow-md">
            <i data-lucide="phone" class="w-3.5 h-3.5 fill-[#030d20]"></i>
            <span>Enquire Now</span>
          </a>
        </div>
      </div>"""

files = ['index.html', 'about.html', 'properties.html', 'contact.html']

for file in files:
    filepath = os.path.join(os.getcwd(), file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace everything inside:
    # <div id="mobileMenu" ...>
    #   <div class="flex flex-col ...">...</div>
    # </div>
    # There is a closing </div> after the flex flex-col div.
    
    pattern = r'      <div class="flex flex-col px-6 sm:px-12 py-6 gap-3\.5 max-h-\[80vh\] overflow-y-auto">.*?</div>\s+</div>'
    
    new_mobile_nav = get_mobile_nav(file) + "\n    </div>"
    
    content = re.sub(pattern, new_mobile_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Mobile nav updated to only show the requested 5 items.')
