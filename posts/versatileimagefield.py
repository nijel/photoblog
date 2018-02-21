import os.path
from django.conf import settings
from versatileimagefield.datastructures.filteredimage import FilteredImage
from versatileimagefield.registry import versatileimagefield_registry
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


class Watermark(FilteredImage):
    def process_image(self, image, image_format, save_kwargs={}):
        """
        Returns a BytesIO instance of `image` with inverted colors
        """
        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        txt = Image.new('RGBA', image.size, (255,255,255,0))

        height = image.size[1]
        fontsize = int(image.size[1] * 0.1)

        # get a font
        fnt = ImageFont.truetype(
            os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'font', 'conthrax-sb.ttf'
            ),
            fontsize,
        )
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text(
            (10 + fontsize * .2, height - 10 - fontsize - fontsize * .2),
            settings.WATERMARK_TEXT,
            font=fnt,
            fill=(255,255,255,70)
        )

        out = Image.alpha_composite(image, txt)
        out = out.convert('RGB')
        imagefile = BytesIO()
        out.save(
            imagefile,
            **save_kwargs
        )
        return imagefile

versatileimagefield_registry.register_filter('watermark', Watermark)
