import os
import re

desktop_properties_block = """        <!-- Properties Dropdown Menu -->
        <div class="relative group/dropdown py-1">
          <a href="properties.html"
            class="nav-link group relative flex items-center gap-1.5 font-semibold text-[15px] xl:text-[15px] uppercase tracking-[0.06em] py-1 cursor-pointer focus:outline-none">
            <i data-lucide="building-2" class="w-3.5 h-3.5 transition-colors group-hover/dropdown:text-[#D4A017]"></i>
            <span>Properties</span>
            <i data-lucide="chevron-down"
              class="w-3 h-3 transition-transform duration-300 group-hover/dropdown:rotate-180"></i>
            <span
              class="absolute bottom-0 left-0 w-0 h-[2px] bg-[#F5C542] rounded-full transition-all duration-300 group-hover/dropdown:w-full"></span>
          </a>

          <!-- Down side dropdown menu panel -->
          <div
            class="dropdown-menu absolute top-full left-0 pt-2.5 w-60 opacity-0 invisible group-hover/dropdown:opacity-100 group-hover/dropdown:visible transition-all duration-200 transform translate-y-1 group-hover/dropdown:translate-y-0 z-50 pointer-events-none group-hover/dropdown:pointer-events-auto">
            <div
              class="bg-white backdrop-blur-md rounded-2xl shadow-[0_18px_40px_rgba(6,24,56,0.12)] border border-gray-100 p-2 flex flex-col gap-1">
              <a href="index.html#commercial"
                class="dropdown-item group/item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[12.5px] font-semibold text-[#061838] hover:bg-amber-50/70 transition-all duration-150">
                <div
                  class="w-7 h-7 rounded-lg bg-[#F5C542]/15 flex items-center justify-center text-[#D4A017] shrink-0 group-hover/item:bg-[#F5C542]/25 group-hover/item:scale-105 transition-all">
                  <i data-lucide="building-2" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-[#061838] group-hover/item:text-[#D4A017] leading-tight transition-colors">
                    Commercial</div>
                  <div class="text-[15px] text-gray-500 font-normal">Retail & Business Hubs</div>
                </div>
              </a>
              <a href="properties.html"
                class="dropdown-item group/item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[12.5px] font-semibold text-[#061838] hover:bg-amber-50/70 transition-all duration-150">
                <div
                  class="w-7 h-7 rounded-lg bg-[#F5C542]/15 flex items-center justify-center text-[#D4A017] shrink-0 group-hover/item:bg-[#F5C542]/25 group-hover/item:scale-105 transition-all">
                  <i data-lucide="home" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-[#061838] group-hover/item:text-[#D4A017] leading-tight transition-colors">
                    Residential</div>
                  <div class="text-[15px] text-gray-500 font-normal">Villas & Apartments</div>
                </div>
              </a>
              <a href="index.html#offices"
                class="dropdown-item group/item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[12.5px] font-semibold text-[#061838] hover:bg-amber-50/70 transition-all duration-150">
                <div
                  class="w-7 h-7 rounded-lg bg-[#F5C542]/15 flex items-center justify-center text-[#D4A017] shrink-0 group-hover/item:bg-[#F5C542]/25 group-hover/item:scale-105 transition-all">
                  <i data-lucide="briefcase" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-[#061838] group-hover/item:text-[#D4A017] leading-tight transition-colors">
                    Offices</div>
                  <div class="text-[15px] text-gray-500 font-normal">Corporate & Workspace</div>
                </div>
              </a>
              <a href="index.html#hospitality"
                class="dropdown-item group/item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[12.5px] font-semibold text-[#061838] hover:bg-amber-50/70 transition-all duration-150">
                <div
                  class="w-7 h-7 rounded-lg bg-[#F5C542]/15 flex items-center justify-center text-[#D4A017] shrink-0 group-hover/item:bg-[#F5C542]/25 group-hover/item:scale-105 transition-all">
                  <i data-lucide="hotel" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-[#061838] group-hover/item:text-[#D4A017] leading-tight transition-colors">
                    Hospitality</div>
                  <div class="text-[15px] text-gray-500 font-normal">Hotels & Resorts</div>
                </div>
              </a>
              <a href="index.html#beach-properties"
                class="dropdown-item group/item flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-[12.5px] font-semibold text-[#061838] hover:bg-amber-50/70 transition-all duration-150">
                <div
                  class="w-7 h-7 rounded-lg bg-[#F5C542]/15 flex items-center justify-center text-[#D4A017] shrink-0 group-hover/item:bg-[#F5C542]/25 group-hover/item:scale-105 transition-all">
                  <i data-lucide="palmtree" class="w-4 h-4"></i>
                </div>
                <div>
                  <div class="font-bold text-[#061838] group-hover/item:text-[#D4A017] leading-tight transition-colors">
                    Beach</div>
                  <div class="text-[15px] text-gray-500 font-normal">Coastal & Waterfront</div>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- Subtle Separator -->"""

mobile_properties_block = """        <!-- Mobile Properties Grouped Section -->
        <div class="pt-2 pb-2 border-t border-b border-white/10">
          <div class="text-[14px] font-bold text-gray-500 uppercase tracking-widest mb-2.5 flex items-center gap-1.5">
            <i data-lucide="building" class="w-3.5 h-3.5 text-[#D4A017]"></i>
            <span>Properties</span>
          </div>
          <div class="pl-2 flex flex-col gap-2">
            <a href="index.html#commercial"
              class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-medium text-[14px] hover:text-[#D4A017] transition-colors py-1">
              <i data-lucide="building-2" class="w-4 h-4 text-[#D4A017]"></i>
              <span>Commercial</span>
            </a>
            <a href="properties.html"
              class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-medium text-[14px] hover:text-[#D4A017] transition-colors py-1">
              <i data-lucide="home" class="w-4 h-4 text-[#D4A017]"></i>
              <span>Residential</span>
            </a>
            <a href="index.html#offices"
              class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-medium text-[14px] hover:text-[#D4A017] transition-colors py-1">
              <i data-lucide="briefcase" class="w-4 h-4 text-[#D4A017]"></i>
              <span>Offices</span>
            </a>
            <a href="index.html#hospitality"
              class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-medium text-[14px] hover:text-[#D4A017] transition-colors py-1">
              <i data-lucide="hotel" class="w-4 h-4 text-[#D4A017]"></i>
              <span>Hospitality</span>
            </a>
            <a href="index.html#beach-properties"
              class="mobile-nav-link flex items-center gap-2.5 text-[#061838] font-medium text-[14px] hover:text-[#D4A017] transition-colors py-1">
              <i data-lucide="palmtree" class="w-4 h-4 text-[#D4A017]"></i>
              <span>Beach</span>
            </a>
          </div>
        </div>

        <a"""

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
    
    # Restore Desktop Properties Dropdown
    content = content.replace('        <!-- Subtle Separator -->', desktop_properties_block, 1)
    
    # Restore Mobile Properties Grouped Section
    # Find the managed-properties tag using regex since the href might differ
    content = re.sub(r'\n\s+<a href=\"(?:index\.html)?#managed-properties\"', '\n' + mobile_properties_block + r' href="index.html#managed-properties"', content, count=1)
    # Note: wait, in about.html and properties.html the original href might be `#managed-properties` instead of `index.html#managed-properties`
    # The regex restores it exactly to the string `index.html#managed-properties`. This should be fine.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Properties menu restored to all files.')
