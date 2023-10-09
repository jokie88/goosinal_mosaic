import os
from lxml import etree
import cairosvg

# Path to the directory containing SVG files
svg_directory = './collectioncopy'

# Iterate through all SVG files in the directory
for filename in os.listdir(svg_directory):
    if filename.endswith(".svg"):
        filepath = os.path.join(svg_directory, filename)

        # Parse the SVG
        tree = etree.parse(filepath)
        root = tree.getroot()

        # Read width and height attributes
        width = root.attrib.get('width', '1122')  # default to 1122 if not present
        height = root.attrib.get('height', '1122')  # default to 1122 if not present

        # Set those values as the viewBox
        desired_viewbox = f"0 0 {width} {height}"
        root.attrib['viewBox'] = desired_viewbox

        # Remove width and height attributes
        if 'width' in root.attrib:
            del root.attrib['width']
        if 'height' in root.attrib:
            del root.attrib['height']

        # Save the modified SVG
        with open(filepath, 'wb') as f:
            f.write(etree.tostring(root))

        # Convert SVG to PNG
        png_filename = os.path.splitext(filename)[0] + '.png'
        png_filepath = os.path.join(svg_directory, png_filename)
        cairosvg.svg2png(url=filepath, write_to=png_filepath)

print("Processing complete!")
