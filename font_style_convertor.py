#!/usr/bin/env python3
"""
Unicode Font Style Converter
Converts regular text to various Unicode font styles including:
- Mathematical Script (like 𝑀𝒾 𝒜𝓂𝑜𝓇)
- Bold, Italic, Bold Italic
- Sans-serif variants
- Monospace
- And more!
"""

class UnicodeStyleConverter:
    def __init__(self):
        # Unicode ranges for different font styles
        self.styles = {
            'script': {
                'A': 0x1D49C, 'B': 0x212C, 'C': 0x1D49E, 'D': 0x1D49F, 'E': 0x2130, 'F': 0x2131,
                'G': 0x1D4A2, 'H': 0x210B, 'I': 0x2110, 'J': 0x1D4A5, 'K': 0x1D4A6, 'L': 0x2112,
                'M': 0x2133, 'N': 0x1D4A9, 'O': 0x1D4AA, 'P': 0x1D4AB, 'Q': 0x1D4AC, 'R': 0x211B,
                'S': 0x1D4AE, 'T': 0x1D4AF, 'U': 0x1D4B0, 'V': 0x1D4B1, 'W': 0x1D4B2, 'X': 0x1D4B3,
                'Y': 0x1D4B4, 'Z': 0x1D4B5,
                'a': 0x1D4B6, 'b': 0x1D4B7, 'c': 0x1D4B8, 'd': 0x1D4B9, 'e': 0x212F, 'f': 0x1D4BB,
                'g': 0x210A, 'h': 0x1D4BD, 'i': 0x1D4BE, 'j': 0x1D4BF, 'k': 0x1D4C0, 'l': 0x1D4C1,
                'm': 0x1D4C2, 'n': 0x1D4C3, 'o': 0x2134, 'p': 0x1D4C5, 'q': 0x1D4C6, 'r': 0x1D4C7,
                's': 0x1D4C8, 't': 0x1D4C9, 'u': 0x1D4CA, 'v': 0x1D4CB, 'w': 0x1D4CC, 'x': 0x1D4CD,
                'y': 0x1D4CE, 'z': 0x1D4CF
            },
            'bold': {
                **{chr(ord('A') + i): 0x1D400 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D41A + i for i in range(26)},  # a-z
                **{str(i): 0x1D7CE + i for i in range(10)}  # 0-9
            },
            'italic': {
                **{chr(ord('A') + i): 0x1D434 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D44E + i for i in range(26)},  # a-z
            },
            'bold_italic': {
                **{chr(ord('A') + i): 0x1D468 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D482 + i for i in range(26)},  # a-z
            },
            'sans_serif': {
                **{chr(ord('A') + i): 0x1D5A0 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D5BA + i for i in range(26)},  # a-z
                **{str(i): 0x1D7E2 + i for i in range(10)}  # 0-9
            },
            'sans_serif_bold': {
                **{chr(ord('A') + i): 0x1D5D4 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D5EE + i for i in range(26)},  # a-z
                **{str(i): 0x1D7EC + i for i in range(10)}  # 0-9
            },
            'monospace': {
                **{chr(ord('A') + i): 0x1D670 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D68A + i for i in range(26)},  # a-z
                **{str(i): 0x1D7F6 + i for i in range(10)}  # 0-9
            },
            'double_struck': {
                **{chr(ord('A') + i): 0x1D538 + i for i in range(26)},  # A-Z
                **{chr(ord('a') + i): 0x1D552 + i for i in range(26)},  # a-z
                **{str(i): 0x1D7D8 + i for i in range(10)}  # 0-9
            }
        }
    
    def convert_text(self, text: str, style: str = 'script') -> str:
        """
        Convert text to the specified Unicode style.
        
        Args:
            text (str): The text to convert
            style (str): The style to apply ('script', 'bold', 'italic', etc.)
        
        Returns:
            str: The converted text
        """
        if style not in self.styles:
            available_styles = ', '.join(self.styles.keys())
            raise ValueError(f"Style '{style}' not available. Choose from: {available_styles}")
        
        style_map = self.styles[style]
        converted_chars = []
        
        for char in text:
            if char in style_map:
                converted_chars.append(chr(style_map[char]))
            else:
                # Keep spaces, punctuation, and other characters unchanged
                converted_chars.append(char)
        
        return ''.join(converted_chars)
    
    def get_available_styles(self) -> list:
        """Return a list of available styles."""
        return list(self.styles.keys())
    
    def demonstrate_all_styles(self, text: str) -> dict:
        """
        Show the input text in all available styles.
        
        Args:
            text (str): The text to demonstrate
        
        Returns:
            dict: Dictionary with style names as keys and converted text as values
        """
        results = {}
        for style in self.styles.keys():
            results[style] = self.convert_text(text, style)
        return results


def main():
    """Main function to demonstrate the converter."""
    converter = UnicodeStyleConverter()
    
    # Example text
    example_text = "Mi Amor"
    
    print("Unicode Font Style Converter")
    print("=" * 40)
    print(f"Original text: {example_text}")
    print()
    
    # Show all styles
    print("Available styles:")
    styles_demo = converter.demonstrate_all_styles(example_text)
    
    for style_name, converted_text in styles_demo.items():
        print(f"{style_name:15}: {converted_text}")
    
    print("\n" + "=" * 40)
    
    # Interactive section
    while True:
        user_input = input("\nEnter text to convert (or 'quit' to exit): ").strip()
        if user_input.lower() == 'quit':
            break
        
        if not user_input:
            print("Please enter some text.")
            continue
        
        print(f"\nAvailable styles: {', '.join(converter.get_available_styles())}")
        style = input("Choose a style (default: script): ").strip().lower()
        
        if not style:
            style = 'script'
        
        try:
            converted = converter.convert_text(user_input, style)
            print(f"\nOriginal:  {user_input}")
            print(f"Converted: {converted}")
            
            # Show how to use it programmatically
            print(f"\nCode to reproduce:")
            print(f"converter.convert_text('{user_input}', '{style}')")
            
        except ValueError as e:
            print(f"Error: {e}")


# Example usage as a module
def convert_to_script(text: str) -> str:
    """Convenience function to convert text to script style."""
    converter = UnicodeStyleConverter()
    return converter.convert_text(text, 'script')


def convert_to_bold(text: str) -> str:
    """Convenience function to convert text to bold style."""
    converter = UnicodeStyleConverter()
    return converter.convert_text(text, 'bold')


if __name__ == "__main__":
    main()