from PIL import Image, ImageEnhance
image = Image.open(':\\Users\\omar\\Desktop\\Site\\Images\\obama.png')
scale_value=scale1.get()
contrast = ImageEnhance.Contrast(image)
contrast_applied=contrast.enhance(scale_value)
image.show()