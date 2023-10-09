# goosinal_mosaic
Mosaic of Ringers 879 (The Goose) created using the Goosinals collection

Procedure:
1. Use inscriptions.json file to get all svg files from your local ord server using download_svg.py
2. Use convert_to_png.py to add a viewport and standardize the svg files and convert to png.
3. use image-collage-maker from github and the goose ringer img to generate the mosaic plus the goosinal number -> mosaic placement mapping. something like ``` python3 make_img.py --path ~/goosinals/png_normalized --dest_img ~/goosinals/goose.png --size 25 --dup 1 --out mosaic.png --tile_info_out ./map.txt ```
4. map the goosinal number back to the inscription id to create the mapped_output.txt

These are just high level outlines of the steps. feel free to file an issue if you need help!
