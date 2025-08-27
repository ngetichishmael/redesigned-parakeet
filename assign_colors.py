#!/usr/bin/env python3
"""
Simple Color Assignment Script

This script demonstrates how to use the ColorAssigner to assign colors
to your directory structure.
"""

from color_assigner import ColorAssigner

def main():
    # Initialize the color assigner
    assigner = ColorAssigner("data/data.json")
    
    # Your tree output (replace this with your actual tree output)
    tree_output = """
ISH:tree -L 2
.
├── 1 GAN Masters
│   ├── 0. Final Research Paper.md
│   ├── 1. Final Research Paper.md
│   ├── 1. Youtube Sources.md
│   ├── 2. Github Sources.md
│   ├── 3. References.md
│   ├── 4. PDF Reading.md
│   ├── 5. Prof Mwathi Changes.md
│   ├── 6. Problem Illustration - Library Analogy.md
│   ├── GAN_Blockchain_Security_Presentation.md
│   ├── GAN_Blockchain_Security_Presentation.pptx
│   ├── GAN_Blockchain_Security_Speaker_Notes.md
│   ├── List_of_Abbreviations.docx
│   ├── List_of_Abbreviations.md
│   ├── changes
│   ├── images
│   ├── pdf
│   └── prof
├── Automata
│   ├── Course Outline.md
│   ├── Topics
│   ├── assignment
│   ├── images
│   └── pdf
├── BiasharaLink
│   └── errors.md
├── Calendar
│   ├── daily
│   ├── monthly
│   ├── quarterly
│   ├── weekly
│   └── yearly
├── Cursor
│   ├── Rules.md
│   └── cursor.md
├── Excalidraw
│   ├── automata.md
│   ├── convert_to_deal.md
│   ├── design.md
│   └── salam.md
├── Exercism
│   └── Configuration.md
├── Go
│   ├── Comments.md
│   ├── Conditions.md
│   ├── Floating-point numbers.md
│   ├── Learning Go.md
│   ├── Pointers.md
│   ├── Range Iteration.md
│   ├── Regex.md
│   ├── String Formating.md
│   ├── boolean.md
│   ├── deployment.md
│   ├── functions.md
│   ├── gin-service.md
│   ├── loop.md
│   ├── maps.md
│   ├── methods.md
│   ├── nginx-config.md
│   ├── randomness.md
│   ├── runes.md
│   ├── slice.md
│   ├── strings.md
│   ├── structs.md
│   ├── switch.md
│   ├── time.md
│   └── weather.md
├── Machine Learning
├── Nuxt
│   └── Format.md
├── Obsidian
│   └── Obsidian Technical Writing Cheat Sheet.md
├── Python
│   └── env.md
├── RSA
│   ├── Asili
│   ├── Deal House
│   ├── KYC
│   ├── Liz
│   ├── Server
│   └── realsourcesafrica.com
├── Salam Logistics
│   ├── Scope of Work.md
│   ├── flow.canvas
│   └── pull.md
├── Shi
│   ├── Profile Picture.md
│   ├── beautiful_mt_fugi.png
│   └── concern.png
├── Washamba
│   ├── Appointment.md
│   └── Lead Full-Stack Engineer & Platform Architect – Washamba Application.md
├── anime
│   └── Release Date.md
├── bases
│   └── Database.base
├── dataview
│   └── 0-dataview.md
└── scripts
    └── insert_see_also_links.py

40 directories, 61 files
ISH:
"""
    
    print("🎨 Color Assignment Tool")
    print("=" * 50)
    
    # Process the tree output
    print("Processing your directory tree...")
    new_assignments = assigner.process_directory_tree(tree_output)
    
    print(f"✅ Generated {len(new_assignments)} color assignments")
    
    # Show some examples
    print("\n📋 Example color assignments:")
    print("-" * 30)
    for i, assignment in enumerate(new_assignments[:8]):
        assigner.print_color_info(assignment['path'])
        print()
    
    # Update file colors (merge with existing)
    assigner.update_file_colors(new_assignments, merge_existing=True)
    
    # Save the updated data
    assigner.save_data()
    
    print(f"💾 Total color assignments saved: {len(assigner.file_colors)}")
    print("\n✨ Done! Your file colors have been updated.")

if __name__ == "__main__":
    main()
