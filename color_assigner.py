#!/usr/bin/env python3
"""
Color Assigner for File Colors

This script assigns colors from a palette to file paths in a deterministic way.
It uses hash-based consistency to ensure the same path always gets the same color,
with additional logic for file extension-based color assignment.
"""

import json
import hashlib
import os
from typing import Dict, List, Optional
from pathlib import Path


class ColorAssigner:
    def __init__(self, data_file: str = "data/data.json"):
        """
        Initialize the ColorAssigner with palette data.
        
        Args:
            data_file: Path to the JSON file containing palette and fileColors
        """
        self.data_file = data_file
        self.palette = []
        self.file_colors = []
        self.load_data()
    
    def load_data(self) -> None:
        """Load palette and existing file colors from JSON file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.palette = data.get('palette', [])
                self.file_colors = data.get('fileColors', [])
            print(f"Loaded {len(self.palette)} colors from palette")
            print(f"Loaded {len(self.file_colors)} existing file color assignments")
        except FileNotFoundError:
            print(f"Warning: {self.data_file} not found. Creating new data structure.")
            self.palette = []
            self.file_colors = []
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            self.palette = []
            self.file_colors = []
    
    def get_color_by_hash(self, path: str) -> Optional[str]:
        """
        Get a color from palette based on hash of the path.
        
        Args:
            path: File or directory path
            
        Returns:
            Color ID from palette, or None if palette is empty
        """
        if not self.palette:
            return None
        
        # Create hash of the path
        path_hash = hashlib.md5(path.encode('utf-8')).hexdigest()
        
        # Use hash to select color index
        color_index = int(path_hash[:8], 16) % len(self.palette)
        
        return self.palette[color_index]['id']
    
    def get_color_by_extension(self, path: str) -> Optional[str]:
        """
        Get a color based on file extension for better visual organization.
        
        Args:
            path: File or directory path
            
        Returns:
            Color ID from palette, or None if no extension-based color found
        """
        if not self.palette:
            return None
        
        # Extension to color mapping
        extension_colors = {
            # Programming languages
            '.py': 'oYWH2nQ34jeifhwIwDR3la',  # Android green
            '.js': 'MEVGFmORZ8RGCd_bjjQnWu',  # Amber
            '.ts': 'MEVGFmORZ8RGCd_bjjQnWu',  # Amber
            '.go': '7CB9E8',  # Aero
            '.java': 'hgz4iwgUS0jg6lgah7Xs-T',  # Amethyst
            '.cpp': '72A0C1',  # Air superiority blue
            '.c': '72A0C1',  # Air superiority blue
            '.rs': 'C46210',  # Alloy orange
            
            # Markdown and documentation
            '.md': 'F0F8FF',  # Alice blue
            '.txt': 'EED9C4',  # Almond
            '.rst': 'EED9C4',  # Almond
            
            # Images
            '.png': 'FD3F92',  # French fuchsia
            '.jpg': 'FD3F92',  # French fuchsia
            '.jpeg': 'FD3F92',  # French fuchsia
            '.gif': 'FD3F92',  # French fuchsia
            '.svg': 'FD3F92',  # French fuchsia
            
            # Data files
            '.json': '9EFD38',  # French lime
            '.xml': '9EFD38',  # French lime
            '.yaml': '9EFD38',  # French lime
            '.yml': '9EFD38',  # French lime
            '.csv': '9EFD38',  # French lime
            
            # Archives
            '.zip': '665D1E',  # Antique bronze
            '.tar': '665D1E',  # Antique bronze
            '.gz': '665D1E',  # Antique bronze
            '.rar': '665D1E',  # Antique bronze
            
            # Documents
            '.pdf': 'C72C48',  # French raspberry
            '.doc': 'C72C48',  # French raspberry
            '.docx': 'C72C48',  # French raspberry
            '.ppt': 'C72C48',  # French raspberry
            '.pptx': 'C72C48',  # French raspberry
        }
        
        # Get file extension
        file_ext = Path(path).suffix.lower()
        
        # Return color ID if extension is mapped
        if file_ext in extension_colors:
            color_id = extension_colors[file_ext]
            # Verify the color exists in palette
            for color in self.palette:
                if color['id'] == color_id:
                    return color_id
        
        return None
    
    def assign_color(self, path: str, prefer_extension: bool = True) -> Optional[str]:
        """
        Assign a color to a path using the best available method.
        
        Args:
            path: File or directory path
            prefer_extension: Whether to prefer extension-based colors over hash-based
            
        Returns:
            Color ID from palette, or None if no color can be assigned
        """
        # Try extension-based color first if preferred
        if prefer_extension:
            ext_color = self.get_color_by_extension(path)
            if ext_color:
                return ext_color
        
        # Fall back to hash-based color
        return self.get_color_by_hash(path)
    
    def process_directory_tree(self, tree_output: str) -> List[Dict[str, str]]:
        """
        Process a directory tree output and assign colors to all paths.
        
        Args:
            tree_output: String output from tree command
            
        Returns:
            List of dictionaries with path and color assignments
        """
        assignments = []
        lines = tree_output.strip().split('\n')
        
        for line in lines:
            # Skip empty lines and summary lines
            if not line.strip() or line.strip().startswith('ISH:') or line.strip().endswith('directories,') or line.strip().endswith('files'):
                continue
            
            # Extract path from tree output
            # Remove tree symbols and indentation
            path = line.strip()
            if '├── ' in path:
                path = path.split('├── ')[1]
            elif '└── ' in path:
                path = path.split('└── ')[1]
            elif '│   ' in path:
                # This is a continuation line, skip
                continue
            
            # Skip if path is empty
            if not path:
                continue
            
            # Assign color
            color_id = self.assign_color(path)
            if color_id:
                assignments.append({
                    "path": path,
                    "color": color_id
                })
        
        return assignments
    
    def update_file_colors(self, new_assignments: List[Dict[str, str]], 
                          merge_existing: bool = True) -> None:
        """
        Update the file colors with new assignments.
        
        Args:
            new_assignments: List of new path-color assignments
            merge_existing: Whether to merge with existing assignments or replace
        """
        if merge_existing:
            # Create a set of existing paths for quick lookup
            existing_paths = {fc['path'] for fc in self.file_colors}
            
            # Add new assignments that don't already exist
            for assignment in new_assignments:
                if assignment['path'] not in existing_paths:
                    self.file_colors.append(assignment)
        else:
            # Replace all assignments
            self.file_colors = new_assignments
    
    def save_data(self, output_file: Optional[str] = None) -> None:
        """
        Save the updated data back to JSON file.
        
        Args:
            output_file: Output file path, uses original file if None
        """
        if output_file is None:
            output_file = self.data_file
        
        # Prepare data structure
        data = {
            "cascadeColors": True,
            "colorBackground": False,
            "palette": self.palette,
            "fileColors": self.file_colors
        }
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.file_colors)} color assignments to {output_file}")
    
    def print_color_info(self, path: str) -> None:
        """
        Print information about color assignment for a specific path.
        
        Args:
            path: File or directory path
        """
        color_id = self.assign_color(path)
        if color_id:
            # Find color details
            color_info = next((c for c in self.palette if c['id'] == color_id), None)
            if color_info:
                print(f"Path: {path}")
                print(f"Color: {color_info['name']} ({color_info['value']})")
                print(f"Color ID: {color_id}")
            else:
                print(f"Path: {path}")
                print(f"Color ID: {color_id} (details not found)")
        else:
            print(f"Path: {path}")
            print("No color assigned")


def main():
    """Main function to demonstrate usage."""
    # Initialize color assigner
    assigner = ColorAssigner()
    
    # Example tree output (you can replace this with your actual tree output)
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
    
    # Process the tree output
    print("Processing directory tree...")
    new_assignments = assigner.process_directory_tree(tree_output)
    
    print(f"Generated {len(new_assignments)} color assignments")
    
    # Show some examples
    print("\nExample color assignments:")
    for i, assignment in enumerate(new_assignments[:5]):
        assigner.print_color_info(assignment['path'])
        print()
    
    # Update file colors
    assigner.update_file_colors(new_assignments, merge_existing=True)
    
    # Save the updated data
    assigner.save_data()
    
    print(f"\nTotal color assignments: {len(assigner.file_colors)}")


if __name__ == "__main__":
    main()
