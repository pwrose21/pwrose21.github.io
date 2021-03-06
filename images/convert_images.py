import os, commands

thumb_height = 120.*2.5
#______________________________________________________________________________
def convert_eps_to_gif(eps):
    assert eps.endswith('.eps')
    name = eps[:-3] + 'gif'
#    os.system('convert -resize x%i -antialias -colors 64 -format gif %s %s' % (img_height, eps, name) )
#    os.system('convert -size x%i -format gif %s %s' % (img_height, eps, name) )
#    os.system('convert -format gif %s[x%i] %s' % (eps, img_height, name) )
    os.system('convert -format gif -antialias %s[x%i] %s' % (eps, img_height, name) )
    if not quiet:
        print '  Created %s' % name
    return name

#______________________________________________________________________________
def convert_eps_to_thumb_gif(eps):
    assert eps.endswith('.eps')
    name = eps[:-3] + 'thumb.gif'
#    os.system('convert -resize x%i -antialias -colors 64 -format gif %s %s' % (thumb_height, eps, name) )
    os.system('convert -format gif -antialias %s[x%i] %s' % (eps, thumb_height, name) )
    if not quiet:
        print '  Created %s' % name
    return name

#______________________________________________________________________________
def convert_eps_to_png(eps):
    assert eps.endswith('.eps')
    name = eps[:-3] + 'png'
    os.system('convert -resize x%i -antialias -colors 64 -format png %s %s' % (img_height, eps, name) )
    if not quiet:
        print '  Created %s' % name
    return name

#______________________________________________________________________________
def convert_eps_to_thumb_png(eps):
    assert eps.endswith('.eps')
    name = eps[:-3] + 'thumb.png'
    os.system('convert -resize x%i -antialias -colors 64 -format png %s %s' % (thumb_height, eps, name) )
    if not quiet:
        print '  Created %s' % name
    return name

def convert_jpg_to_thumb_jpg(jpg):
    assert jpg.lower().endswith('.jpg')
    name = jpg[:-3] + 'thumb.jpg'
    os.system('convert -resize x%i -antialias -colors 64 -format jpg %s %s' % (thumb_height, jpg, name) )
    return name

def convert_all():
    files = commands.getoutput('ls .')
    files = files.split('\n')
    for iFile in files:
        if 'convert_images' in iFile: continue
        if not 'jpg' in iFile.lower():
            print 'WARNING:', iFile, 'not a JPG file. Skipping.'
            continue
        if 'thumb' in iFile: continue

        convert_jpg_to_thumb_jpg(iFile)
        
convert_all()
