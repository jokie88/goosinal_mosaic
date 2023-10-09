# goosinal mosaic
Mosaic of Ringers 879 (The Goose) created using the Goosinals collection

## To find your inscripiton in the picture:
1. click on the file mapped_output.txt.
2. Do a search to find your inscription id in the file.
3. Look at the line number for your inscription id. thats the position of your goosinal in the mosaic. its numbered 1-100 for the first row, 101-200 for the second and so on.   


Steps to Reproduce:
1. Use inscriptions.json file to get all svg files from your local ord server using download_svg.py
2. Use convert_to_png.py to add a viewport and standardize the svg files and convert to png.
3. use image-collage-maker from github and the goose ringer img to generate the mosaic plus the goosinal number -> mosaic placement mapping. something like ``` python3 make_img.py --path ~/goosinals/png_normalized --dest_img ~/goosinals/goose.png --size 25 --dup 1 --out mosaic.png --tile_info_out ./map.txt ``` if you have trouble outputting the map.txt you may need to edit the python script to increase the length of the datatype: ``` tile_info = np.full(grid, "background"*10, dtype='<U100')  # Allow up to 100 characters ```
4. map the goosinal number back to the inscription id to create the mapped_output.txt (if i was smart i would've just used the inscription_hash all the way through)

These are just high level outlines of the steps. feel free to file an issue if you need help!
