import commands


top_matter = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "xhtml11.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <title>photography</title>

    <!--
	1 ) Reference to the files containing the JavaScript and CSS.
	These files must be located on your server.
      -->

    <script type="text/javascript" src="./highslide-4.1.9/highslide/highslide-with-gallery.js"></script>
    <link rel="stylesheet" type="text/css" href="./highslide-4.1.9/highslide/highslide.css" />

    <!--
	2) Optionally override the settings defined at the top
	of the highslide.js file. The parameter hs.graphicsDir is important!
      -->

    <script type="text/javascript">
      hs.graphicsDir = './highslide-4.1.9/highslide/graphics/';
      hs.align = 'center';
      hs.transitions = ['expand', 'crossfade'];
      hs.wrapperClassName = 'dark borderless floating-caption';
      hs.fadeInOut = true;
      hs.dimmingOpacity = 0.75;

      // Add the controlbar
      if (hs.addSlideshow) hs.addSlideshow( {
      //slideshowGroup: 'group1',
      interval: 5000,
      repeat: false,
      useControls: true,
      fixedControls: 'fit',
      overlayOptions: {
      opacity: .6,
      position: 'bottom center',
      hideOnMouseOut: true
      }
      });
    </script>

  </head>

  <body>

    <!--                                                                                                                                                
        3) Put the thumbnails inside a div for styling                                                                                                  
      -->

    <div class="highslide-gallery">

      <!--                                                                                                                                              
          4) This is how you mark up the thumbnail image with an anchor tag around it.                                                                  
          The anchor's href attribute defines the URL of the full-size image                                                                            
        -->




"""

image_template = """
      <a href="./images/%s" class="highslide" onclick="return hs.expand(this)">
        <img src="./images/%s" alt="Highslide JS"
             title="Click to enlarge" />
      </a>

      <div class="highslide-caption">
        NEW CAPTION
      </div>
"""

f=open('photography.html', 'w')
f.write(top_matter + '\n\n')
files = commands.getoutput('ls images/')
files = files.split('\n')
for iFile in files:
    ifile = iFile.lower()
    if not ifile.endswith('.jpg'): continue
    if '.thumb.jpg' in ifile: continue
    f.write(image_template % (iFile, ifile.replace('.jpg', '.thumb.jpg')))

f.write("    </div>\n")
f.write("  </body>\n")
f.write("</html>\n")
f.close()
            

"""
<body>

  <!--
      3) Put the thumbnails inside a div for styling
    -->

  <div class="highslide-gallery">
    
    <!--
	4) This is how you mark up the thumbnail image with an anchor tag around it.
	The anchor's href attribute defines the URL of the full-size image
      -->
    <a href="./images/AlpsBlueberry.jpg" class="highslide" onclick="return hs.expand(this)">
      <img src="./images/AlpsBlueberry.thumb.jpg" alt="Highslide JS"
	   title="Click to enlarge" />
    </a>
    
    <!--
	5 (options). This is how you mark up the caption.  The correct class name is important.
      -->
    <div class="highslide-caption">
      yummy blueberry in the French Alps
    </div>

  </div>
</body>
</html>
"""



