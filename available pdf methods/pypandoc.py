import pypandoc

#this is a tricky one
# recommended solution to get as close to the original epub as possible 
# but to avoid for pdf

#could be an error from my side as I only tried MiKTex and TexLive
#I do not have enough .tex experience outside reading the documentation

#problems with pdflatex are common and it is easy to get mixed in .tex packages and forgeting to seet PATHs

#if you do decide to use this pandoc wrapper 
# recommendation is to use conda forge to install everything as needed
# it is easy to miss a step by yourself and later have a lot of trouble

# use format = '' as to force and be explicit it tends to help some errors
# use extra args as it also tends to fix some compiling errors
# use assert and don't skip as that is what tells pandoc that the compilation was successful

# LaTeX needs to compile, this is the most error prone way, go about it if you can or can't spare gigabytes of space
   
if arg == "pdf":
            output = pypandoc.convert_file(
                "wiki_page.html", "pdf",format='html', outputfile=f"{wiki_page.title}.pdf",
                extra_args=['--metadata', f'title="{wiki_page.title}.pdf"']
            )
            assert output == ""