Overview:  
---------  

The purpose of this package is to provide an out-of-the-box meme generator complete with DIY functionality and a selection of fonts.  
Feel free to add more fonts, pictures and quotes into the data directory - though you can input the latter two from the CLI and the web!  

How to run it:  
--------------  

From the CLI - python3 main.py --optional_args  
    Optional args:  
    --path  : the location in which you want your memes saved  
    --body  : the text you want quoted on your meme  
    --author: what legendary person supposedly said the aforementioned quote  

On the web - python3 app.py from the command line or using your favourite debugger  

Submodules:  
-----------  

engines.py  - consists of the classes used to hold the quote data neatly inside a class  
              and similarly to hold the entire meme (once it's been generated) inside a singe class  
importer.py - the main interface for reading the quotes files. Purpose is to handle a number of file types  
main.py     - module through which it's possible to generate memes and have them saved locally from the command line  
app.py      - module through which it's possible to generate memes in your default browser  
helpers.py  - some auxiliary functions to prevent repeated code  

Note to install pdftotext on Windows
----------
1. Download the Xpdf command line tools from https://www.xpdfreader.com/download.html
2. Extract the files
3. Put pdftotext wherever you'd like on your local machine
4. Add the location of pdftotext into your PATH env variables (if it's not there already)
5. Restart your IDE

Ensure to check requirements.txt for all other packages that require importing before the code can be run!  
