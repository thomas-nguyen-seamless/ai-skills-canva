"""Turn the parchment engravings into ink-only RGBA art that sits cleanly on the slide background."""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

INK = (0x2F, 0x5A, 0x8C)  # engraving blue, readable on #F7F8FA

def ink_alpha(path, crop=None, gain=1.35, cut=0.06, floor=0):
    im = Image.open(path).convert("RGB")
    if crop:  # fractions l,t,r,b
        w, h = im.size
        im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    a = np.asarray(im, dtype=np.float32)
    lum = 0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2]
    bg = ndimage.maximum_filter(lum, size=21)
    bg = ndimage.gaussian_filter(bg, 9)
    d = np.clip((bg - lum) / np.maximum(bg - 40, 1), 0, 1)  # 0 paper .. 1 dark ink
    d = np.clip((d - cut) * gain, 0, 1)
    alpha = (d * 255).astype(np.uint8)
    alpha[alpha < floor] = 0
    out = np.zeros(alpha.shape + (4,), np.uint8)
    out[..., 0], out[..., 1], out[..., 2] = INK
    out[..., 3] = alpha
    img = Image.fromarray(out, "RGBA")
    bbox = img.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()
    return img.crop(bbox) if bbox else img

if __name__ == "__main__":
    A = "assets/"
    ink_alpha(A + "cover_nautilus.jpg", crop=(0.55, 0.0, 1.0, 1.0), cut=0.16, gain=1.5, floor=40).save(A + "ink_nautilus.png")
    ink_alpha(A + "silk_egg2.jpg", crop=(0.14, 0.14, 0.86, 0.86), cut=0.10, gain=1.4, floor=30).save(A + "ink_egg.png")
    for n in ("larva", "cocoon", "moth"):
        ink_alpha(A + f"silk_{n}.jpg", crop=(0.14, 0.14, 0.86, 0.86)).save(A + f"ink_{n}.png")
    ink_alpha(A + "rice3.jpg", crop=(0.02, 0.04, 0.98, 0.96)).save(A + "ink_rice3.png")
    for n in ("nautilus", "egg", "larva", "cocoon", "moth", "rice3"):
        print(n, Image.open(A + f"ink_{n}.png").size)
