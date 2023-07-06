import img2pdf
input_image="/home/karthikeyan/Documents/python/image.jpg"
output_pdf="/home/karthikeyan/Documents/python/image.pdf"
with open(output_pdf,"wb") as ip:
    ip.write(img2pdf.convert(input_image))
    ip.close()